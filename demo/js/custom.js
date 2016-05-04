var buttonTypes = ['btn-primary', 'btn-success', 'btn-info', 'btn-warning', 'btn-danger'];
var tags = [];
var chars = [" ", "?", "!", ".", ";", ":"];

function addTag(tag) {
  var randomButtonType = buttonTypes[Math.floor(Math.random() * buttonTypes.length)];
  $('#tags').append('<div class="btn-group"><button type="button" class="btn '+randomButtonType+' dropdown-toggle tag-btn" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> #'+tag+' <span class="glyphicon glyphicon-remove"></span></button></div> ');
  tags.push(tag);
}

function search() {
  var query = {
    query: {
      function_score: {
        query: {
          filtered: {
            query: {
              query_string: {
                query: $('#query').val()
              }
            },
            filter: {
              terms: {
                "@Tags": tags
              }
            }
          }
        },
        functions: [
          {
            script_score: {
              script: {
                params: {
                  a: 0.33,
                  view_count_normalizer: 110030,
                  score_normalizer: 500,
                  e: 2.71828
                },
                inline: "(1 - pow(e, -1*doc['@Score'].value/score_normalizer))*a+(1 - pow(e, -1*doc['@ViewCount'].value/view_count_normalizer))*pow(a, 2)"
              }
            }
          }
        ],
        boost_mode: "sum",
        score_mode: "sum"
      }
    }
  }

  $.ajax({
    url: 'http://localhost:9200/stackoverflowbig/question/_search',
    dataType: 'json',
    type: 'POST',
    contentType: 'application/json',
    crossDomain: true,
    data: JSON.stringify(query),
    success: function(data) {
      alert(JSON.stringify(data.hits.hits));
    }
  });
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
