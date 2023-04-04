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
  var url = '/image.jpg?' + new Date().getTime();
  $('#re').attr('src', url);
}

$(function () {
  $("a#stop").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/stop", function (data) {

    });
    return false;
  });
});