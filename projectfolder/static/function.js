$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      readFile();
    });
    return false;
  });
});

function readFile() {
  jQuery.get('result.txt', function (txt) {
    $('#outputBx').text(txt);
    refreshImage('/image.jpg'); // Pass the image path as a parameter
  });
}

function refreshImage(imagePath) {
  var timestamp = new Date().getTime();
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
