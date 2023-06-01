$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    readFile(); // Move readFile() inside the click event handler
    $.getJSON("/compare", function (data) {
      //Do nothing
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
  var imagePath = '/image_' + timestamp + '.jpg'; // Add a timestamp as part of the path to the image URL
  $('#re').attr('src', imagePath); // Update the image source with the new URL
}

