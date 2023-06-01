$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      // Only call readFile and refreshImage after receiving a response from the server
      readFile();
    });
    return false;
  });

  $("a#stop").on("click", function (e) {
    e.preventDefault();
    // Add code for stopping the image updates, if needed
    $.getJSON("/stop", function (data) {
      //do nothing
    });

    return false;
  });
});

function readFile() {
  $.get('/result.txt', function (txt) {
    $('#outputBx').text(txt);
    refreshImage(); // Call refreshImage() inside the success callback
  });
}

function refreshImage() {
  var timestamp = new Date().getTime();
  var imagePath = '/image_' + timestamp + '.jpg'; 
  $('#re').attr('src', imagePath);
}