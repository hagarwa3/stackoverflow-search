var buttonTypes = ['btn-primary', 'btn-success', 'btn-info', 'btn-warning', 'btn-danger'];
var tags = [];

function addTag(tag) {
  var randomButtonType = buttonTypes[Math.floor(Math.random() * buttonTypes.length)];
  $('#tags').append('<div class="btn-group"><button type="button" class="btn '+randomButtonType+' dropdown-toggle tag-btn" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> #'+tag+' <span class="glyphicon glyphicon-remove"></span></button></div> ');
  tags.push(tag);
}

$(document).ready(function() {
  $('.tag-btn').click(function() {
    var tag = $(this).parent().text();
    tag = tag.slice(2, tag.length-1);
    $(this).parent().remove();
    var index = tags.indexOf(tag);
    if(index >= 0) {
      tags.splice(index, 1);
    }
  });
});

addTag("javascript");
addTag("swift");
addTag("mysql");
