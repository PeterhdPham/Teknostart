"""
Sever classes used in the web method
"""

from cgitb import html
import io
import glob
import json
import logging
import os
from pickle import FALSE, TRUE
import socketserver
import time
from http import server
import threading
from threading import Thread, Condition
from multiprocessing import Process
import Pyro4
from lobe import ImageModel
from utils import server_ip, detect_pi, warning
from flask import Flask, render_template, send_file, make_response, send_from_directory, request
from PIL import ImageFile
import RPi.GPIO as GPIO

ImageFile.LOAD_TRUNCATED_IMAGES = True

app = Flask(__name__)

@app.route('/image_<timestamp>.jpg')
def serve_image(timestamp):
    return send_from_directory('/home/pi/Teknostart/projectfolder', 'image.jpg')

# @app.route('/image.jpg')
# def get_image():
#     # open the image file
#     image = open('image.jpg', 'rb')

#     # create a response object
#     response = make_response(send_file(image, mimetype='image/jpeg'))

#     # set the cache-control header to prevent caching
#     response.headers['Cache-Control'] = 'no-store'

#     return response

# if __name__ == '__main__':
#     app.run(debug=True)

result = "ingenting"
@app.route('/index.html')
def index():
  return render_template('index.html', result=result)

@app.route('/compare')
def background_process_test():
    print ("Hello")
    return ("nothing")


model = ImageModel.load('/home/pi/Teknostart/Lobe')

def compare():
    res = model.predict_from_file('/home/pi/Teknostart/projectfolder/image.jpg')
    return res.prediction

def recognize(label):
    print("RESULT:  " + label)

if detect_pi():
    import picamera


class StreamingOutput(object):
    """Defines output for the picamera, used by request server"""

    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
        self.count = 0

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
            self.count += 1
        return self.buffer.write(buf)


class RequestHandler(server.BaseHTTPRequestHandler):
    """Request server, handles request from the browser"""
    output = None
    keys = None
    rov = None
    base_folder = None
    index_file = None
    custom_response = None

    def do_GET(self):
        if self.path == '/':
            self.redirect('/index.html', redir_type=301)
        elif self.path == '/stream.mjpg':
            self.serve_stream()
        elif self.path.startswith('/http') or self.path.startswith('/www'):
            self.redirect(self.path[1:])
        elif self.path.startswith('/keyup'):
            self.send_response(200)
            self.end_headers()
            self.keys.keyup(key=int(self.path.split('=')[1]))
        elif self.path.startswith('/keydown'):
            self.send_response(200)
            self.end_headers()
            self.keys.keydown(key=int(self.path.split('=')[1]))
        elif self.path.startswith('/sensor.json'):
            self.serve_rov_data('sensor')
        elif self.path.startswith('/actuator.json'):
            self.serve_rov_data('actuator')
        elif self.path.startswith('/stop'):
            self.send_response(200)
            self.end_headers()
            self.rov.run = False
        elif self.path.startswith('/compare'):
            result = compare()
            text_file = open('/home/pi/Teknostart/projectfolder/result.txt', "w")
            n = text_file.write(result)
            text_file.close()
            print("COMPARING...")
            recognize(result)
        elif self.path.startswith('/image_') and self.path.endswith('.jpg'):
            path = os.path.join(self.base_folder, 'image.jpg')
            self.serve_path(path)

        else:
            path = os.path.join(self.base_folder, self.path[1:])
            if os.path.isfile(path):
                self.serve_path(path)
            elif self.custom_response:
                response = self.custom_response(self.path)
                if response:
                    if response.startswith('redirect='):
                        new_path = response[response.find('=') + 1:]
                        self.redirect(new_path)
                    else:
                        self.serve_content(response.encode('utf-8'))
                else:
                    warning(message='Bad response. {}. custom '
                                    'response function returned nothing'
                            .format(self.requestline), filter='default')
                    self.send_404()
            else:
                warning(message='Bad response. {}. Could not find {}'
                        .format(self.requestline, path), filter='default')
                self.send_404()

    def do_POST(self):
        self.send_404()

    def serve_content(self, content, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)

    def serve_path(self, path):
        if '.css' in path:
            content_type = 'text/css'
        elif '.js' in path:
            content_type = 'text/javascript'
        else:
            content_type = 'text/html'
        with open(path, 'rb') as f:
            content = f.read()
        self.serve_content(content, content_type)

    def redirect(self, path, redir_type=302):
        self.send_response(redir_type)
        self.send_header('Location', path)
        self.end_headers()

    def send_404(self):
        self.send_error(404)
        self.end_headers()

    def serve_rov_data(self, data_type):
        values = ''
        if data_type == 'sensor':
            values = json.dumps(self.rov.sensor)
        elif data_type == 'actuator':
            values = json.dumps(self.rov.actuator)
        else:
            warning('Unable to process data_type {}'.format(data_type))
        content = values.encode('utf-8')
        self.serve_content(content, 'application/json')

    def serve_stream(self):
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Content-Type',
                         'multipart/x-mixed-replace; boundary=FRAME')
        self.end_headers()
        try:
            while True:
                with self.output.condition:
                    self.output.condition.wait()
                    frame = self.output.frame
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(frame))
                self.end_headers()
                self.wfile.write(frame)
                self.wfile.write(b'\r\n')
        except Exception as e:
            logging.warning(
                'Removed streaming client %s: %s',
                self.client_address, str(e))

    def log_message(self, format, *args):
        return


class WebpageServer(socketserver.ThreadingMixIn, server.HTTPServer):
    """Threaded HTTP server, forwards request to the RequestHandlerClass"""
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, server_address, RequestHandlerClass, stream_output,
                 rov_proxy, keys_proxy, index_file=None, debug=False,
                 custom_response=None):
        self.start = time.time()
        self.debug = debug
        RequestHandlerClass.output = stream_output
        RequestHandlerClass.rov = rov_proxy
        RequestHandlerClass.keys = keys_proxy
        RequestHandlerClass.base_folder = os.path.abspath(
            os.path.dirname(index_file))
        RequestHandlerClass.index_file = index_file
        RequestHandlerClass.custom_response = custom_response
        super(WebpageServer, self).__init__(server_address,
                                            RequestHandlerClass)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Shutting down http server')
        if self.debug:
            finish = time.time()
            frame_count = self.RequestHandlerClass.output.count
            print('Sent {} images in {:.1f} seconds at {:.2f} fps'
                  .format(frame_count,
                          finish - self.start,
                          frame_count / (finish - self.start)))


def start_http_server(video_resolution, fps, server_port, index_file,
                      debug=False, custom_response=None):
    if debug:
        print('Using {} @ {} fps'.format(video_resolution, fps))

    with picamera.PiCamera(resolution=video_resolution,
                           framerate=fps) as camera, \
            Pyro4.Proxy("PYRONAME:ROVSyncer") as rov, \
            Pyro4.Proxy("PYRONAME:KeyManager") as keys:

        stream_output = StreamingOutput()
        s = WebpageServer(server_address=('', server_port),
                               RequestHandlerClass=RequestHandler,
                               stream_output=stream_output,
                               debug=debug,
                               rov_proxy=rov,
                               keys_proxy=keys,
                               index_file=index_file,
                               custom_response=custom_response)
        server_thread = Thread(target=s.serve_forever, daemon=True)
        camera.vflip = True
        camera.hflip = True
        camera.rotation = 180
        camera.start_recording(stream_output, format='mjpeg')

        try:            
            print('Visit the webpage at {}'.format(server_ip(server_port)))
            server_thread.start()
            while True:
                time.sleep(0.1)
                camera.capture('/home/pi/Teknostart/projectfolder/image.jpg', use_video_port=True, splitter_port=2)
                
        finally:
            print('closing web server')
            camera.stop_recording()
