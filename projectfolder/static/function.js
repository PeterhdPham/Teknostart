$(function () {
  $("a#button").on("click", function (e) {
    // window.location.reload();
    e.preventDefault();
    $.getJSON("/compare", function (data) {

    });
    readFile();
    return false;
  });
});

function readFile() {
  jQuery.get('result.txt', function (txt) {
    $('#outputBx').text(txt);
    refreshImage();
  });
}

function readFile() {
  jQuery.get('result.txt', function (txt) {
    $('#re').attr('src', '/image.jpg?' + new Date().getTime());
    $('#outputBx').text(txt);
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
