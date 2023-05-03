// Toggle the class of the <header> element when the user clicks on the
// `DIV#toggle_header` tag. classes are red and green

$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass('red green');
  });
});
