// Adds the class `red` to the <header> tag when user clicks `DIV#red_header`
// using jQuery

$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').addClass('red');
  });
});
