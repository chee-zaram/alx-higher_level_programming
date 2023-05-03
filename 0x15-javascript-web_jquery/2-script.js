// Updates the text color of the 'header' element of an HTML document to #FF0000
// with jQuery when user clicks on `DIV#red_header`

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').css('color', '#FF0000');
  });
});
