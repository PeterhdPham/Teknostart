$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {

    });
    readFile();
    return false;
  });
});

function readFile() {
  jQuery.get('result.txt', function (txt) {
    refreshImage();
    $('#outputBx').text(txt);
  });
}

function refreshImage() {
  var timestamp = new Date().getTime();
  var imagePath = '/image.jpg?' + timestamp;
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