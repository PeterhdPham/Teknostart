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
    var random = Math.floor(Math.random() * 1000000); // generate a random number
    $('#re').attr('src', '/image.jpg?' + random); // update the image source with a random query string
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
