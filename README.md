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


## Parsing the StackOverflow Data
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

