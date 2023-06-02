$(function () {
  $("a#button").on("click", function (e) {
    console.log("funcfunc function called");
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      // Only call readFile and refreshImage after receiving a response from the server
      if (data.status === "ok") {
        readFile();
      } else {
        console.error(data.message);
      }
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
  console.log("readFile function called");
  $.get('/result.txt', function (txt) {
    console.log("Reading file", txt);
    $('#outputBx').text(txt);
    refreshImage();
  });
}

function refreshImage() {
  var timestamp = new Date().getTime();
  var imagePath = '/image_' + timestamp + '.jpg'; 
  $('#re').attr('src', imagePath);
}

