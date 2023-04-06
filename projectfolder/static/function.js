$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      readFile(); // Move the call to readFile() inside the $.getJSON() function
    });
    return false;
  });
});

function readFile() {
  jQuery.get('result.txt', function (txt) {
    $('#outputBx').text(txt);
    refreshImage(); // Move the call to refreshImage() inside the $.get() function
  });
}

function refreshImage() {
  var timestamp = new Date().getTime();
  var imagePath = '/image.jpg';
  jQuery.get(imagePath, function() {
    $('#re').attr('src', imagePath);
  });
}

$(function () {
  $("a#stop").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/stop", function (data) {

    });
    return false;
  });
});
