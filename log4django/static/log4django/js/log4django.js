$(document).ready(function() {
  $('tr.accordion-toggle').css('cursor', 'pointer').find('a span.glyphicon').on('click', function(event) {
    event.preventDefault();
  });
});