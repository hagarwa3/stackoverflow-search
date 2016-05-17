# stackoverflow-search
A system to automatically answer stack overflow / Piazza questions using the stackoverflow data dump + elastic search

Find the entire index of all questions till March 2016 (18GB) at https://goo.gl/aA7q8Q
This is the data indexed by elasticsearch, and while I am not sure about this, I believe that you can directly put this indexed data into the respective elasticsearch folder to have the same setup. I have chosen not to actually host the entire thing because of its huge size.

There are multiple parts to this entire project:
- Parsing the original data (xml files from StackOverflow data dump) and then indexing it into elasticsearch
- Testing multiple different queries to see which gives us the best results
- Building a keyword extraction algorithm for all questions, to do automatic tagging of question
- Integrate all of this in the frontend (HTML+JS+Bootstrap)
- Build extra analysis tools and experiment on questions from different languages/frameworks to see what programmers usually have questions about


## Parsing and Indexing the StackOverflow Data
The data was originally in XML format, which means it cannot be directly indexed into ELasticSearch. The task at hand required us to extract all questions only (that was what the search functionality was being built over), convert them to JSON, and then split all of these entries up to be easily indexed by ElasticSEarch's [__Bulk API__](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html).

A sample entry is as follows:
```json
{
	"@Id": 13, 
	"@PostTypeId": 1, 
	"@AcceptedAnswerId": 357, 
	"@CreationDate": "2008-08-01T00:42:38.903", 
	"@Score": 384, "@ViewCount": 111349, 
	"@Body": "<p>Is there a standard way for a Web Server to determine what time zone offset a user is in? </p>\n\n<p>Perhaps from a <code>HTTP</code> header? Or part of the user-agent string?</p>\n", "@OwnerUserId": 9, 
	"@LastEditorUserId": 2518525, 
	"@LastEditorDisplayName": "Rich B", 
	"@LastEditDate": "2015-06-05T06:26:25.383", 
	"@LastActivityDate": "2016-02-11T04:13:22.413", 
	"@Title": "Determining a web user's time zone", 
	"@Tags": "<html><browser><timezone><timezoneoffset>", 
	"@AnswerCount": 23, 
	"@CommentCount": 3, 
	"@FavoriteCount": 116
}
```
Each of the 11 million entries needs to be indexed into elasticsearch, so I had to split the entries into multiple files of 1000 entries each, followed by adding the requisite information before each entry to get it indexed successfully, and then using multiple calls through [cURL](https://curl.haxx.se/) to actually get the data indexed. Most repetitive bash scripts were set up using python. The additional data was as follows (teh id varied for each entry):
```json
{"index":{"_index":"stackoverflowbig","_type":"question","_id":9948026}}
```

Finally the data was all successfully indexed and then could be queried easily using [Sense](https://www.elastic.co/guide/en/sense/current/index.html) to test it. An example is shown as follows:

![alt-text](https://github.com/hagarwa3/stackoverflow-search/blob/master/demo/images/sense%2Bsimple%20query.png "Sense + Simple Query")



## Testing Different Queries
This was relatively more tricky, simply because it is a very subjective thing, and without a lot of user feedback, it's usually not possible to get a strong, statistically "good" query. We did however test different things, such as weighing most recent activity, date when question was posted, upvotes, number of responses etc. Our final query is [here](https://github.com/hagarwa3/stackoverflow-search/blob/master/query.json).



## Building a Keyword Extraction Algorithm
Currently the RAKE (Rapid Automatic Keyword Extraction) algorithm is the method being used. There is a [Python library](https://github.com/aneesha/RAKE) for the same that makes the task much easier. All possible keywords are extracted, and the top three single word keywords are the ones that are finally returned (because generally there are only three tags for most questions). This algorithm was further adapted for more of the analysis related sections of the project. There is still more work to be done in the keyword extraction, to see if the algorithm could perform better for more programming related terms. A demo of my setup (hosted on heroku) can be found [here](https://searchoverflow.herokuapp.com/gettags/?text=%22sample%20javascript%20stuff%20tbh%20javascript%20is%20great%22). The text part fo the request can be edited to your own query, which can then be sent forth to get the relevant tags.

##Front-End
The front end is styled with elements from Bootstrap. jquery was used to make requests for new automatically generated tag every time the user entered a new word, and the user could add more tags manually too. The request was finally made to an elasticsearch server running on localhost:9200
Upon sending the query, the top three results are returned, that are linked to the actual stackoverflow pages. Actual performance accuracy still has to be numerically evaluated, but it does pretty well on most general queries. A demo can be viewed [here](https://youtu.be/biQktl98i9o?t=364)
