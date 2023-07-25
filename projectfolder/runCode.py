from doctest import FAIL_FAST
import os
from pickle import FALSE
import subprocess
from tkinter import LEFT, RIGHT
from turtle import down
import Pyro4
from core import WebMethod
import RPi.GPIO as GPIO



#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT) #UP/DRIVE
GPIO.setup(19, GPIO.OUT) #DOWN/REVERSE
GPIO.setup(13, GPIO.OUT) #LEFT
GPIO.setup(6, GPIO.OUT) #RIGHT



UP = False
DOWN = False
RIGHT = False
LEFT = False

#FORWARD DRIVING LIGHTS (WHITE)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT) 
#BACKWARDS DRIVING LIGHTS (RED)
GPIO.setup(2,GPIO.OUT) 
GPIO.setup(3,GPIO.OUT)

def control_motors():
    global UP, DOWN, LEFT, RIGHT

    with Pyro4.Proxy("PYRONAME:KeyManager") as keys:
        with Pyro4.Proxy("PYRONAME:ROVSyncer") as rov:
            while rov.run:
                if keys.state('K_UP'):
                    print('Forward')
                    UP = True
                else:
                    UP = False
                if keys.state('K_DOWN'):
                    print('Down')
                    DOWN = True
                else:
                    DOWN = False
                if keys.state('K_RIGHT'):
                    print('Rigth')
                    RIGHT = True
                else:
                    RIGHT = False
                if keys.state('K_LEFT'):
                    print('Left')
                    LEFT = True
                else:
                    LEFT = False
                if keys.state('K_SPACE'):
                    print('Compare')

                    
                
                FRONTLIGHTS = UP
                BACKLIGHTS = DOWN 

                GPIO.output(26, UP)    # UP/DRIVE
                GPIO.output(19, DOWN)  # DOWN/REVERSE
                GPIO.output(13, LEFT)  # LEFT
                GPIO.output(6, RIGHT)  # RIGHT

                GPIO.output(20, FRONTLIGHTS) # FORWARD DRIVING LIGHTS (WHITE)
                GPIO.output(21, FRONTLIGHTS) # FORWARD DRIVING LIGHTS (WHITE)
                GPIO.output(2, BACKLIGHTS)   # BACKWARDS DRIVING LIGHTS (RED)
                GPIO.output(3, BACKLIGHTS)   # BACKWARDS DRIVING LIGHTS (RED)



# Create the WebMethod class
web_method = WebMethod(
    index_file=os.path.join(os.path.dirname(__file__), 'index.html'),
    runtime_functions=control_motors
)
# Start serving the web page, blocks the program after this point
web_method.serve()
