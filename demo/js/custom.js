var buttonTypes = ['btn-primary', 'btn-success', 'btn-info', 'btn-warning', 'btn-danger'];
var tags = [];
var chars = [" ", "?", "!", ".", ";", ":"];

function addTag(tag) {
  var randomButtonType = buttonTypes[Math.floor(Math.random() * buttonTypes.length)];
  $('#tags').append('<div class="btn-group"><button type="button" class="btn '+randomButtonType+' dropdown-toggle tag-btn" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> #'+tag+' <span class="glyphicon glyphicon-remove"></span></button></div> ');
  tags.push(tag);
}

function search() {
  alert("search");
}

$(document).ready(function() {
  $(document).on('click', '.tag-btn', function() {
    var tag = $(this).parent().text();
    tag = tag.slice(2, tag.length-1);
    $(this).parent().remove();
    var index = tags.indexOf(tag);
    if(index >= 0) {
      tags.splice(index, 1);
    }
  });

  $('.btn-add-tag').click(function() {
    var newTag = prompt("Enter a tag:", "tag");
    addTag(newTag);
  });

  $('#search').click(function() {
    search();
  });

  $('#query').on('input', function() {
    var queryText = $('#query').val();
    var lastChar = queryText.substr(queryText.length - 1);
    var index = chars.indexOf(lastChar);
    if(index > -1) {
      getTags();
    }
  })
});

function getTags() {
  var request = $.ajax({
    url: 'http://searchoverflow.herokuapp.com/gettags/',
    type: 'GET',
    data: {
      text: JSON.stringify($('#query').val())
    }
  });

  request.done(function(result) {
    $('#tags').empty();
    tags = [];
    var splitTags = result.split(" ");
    for(var i = 0; i < splitTags.length; i++) {
      var newTag = splitTags[i];
      if(newTag.length > 0) {
        addTag(splitTags[i]);
      }
    }
  });
}

addTag("javascript");
addTag("swift");
addTag("mysql");
