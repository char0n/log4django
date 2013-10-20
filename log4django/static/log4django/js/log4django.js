$(document).ready(function() {
  // Links don't behave like links.
  $('tr.accordion-toggle').css('cursor', 'pointer').find('a span.glyphicon').on('click', function(event) {
    event.preventDefault();
  });
  // Expand collapsed table row content.
  $('[id^="logRecordDetail"] tr.accordion-toggle').trigger('click');
});