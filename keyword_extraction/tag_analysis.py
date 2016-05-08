import RAKE.RAKE as rake
import operator
import json
import re
f1 = open('extratest/resultant.txt','w')
f = open('extratest/10000.json','r') 
rake_object = rake.Rake("smartstoplist.txt")
parsed_input = json.load(f)
#print parsed_input
results = parsed_input['results']
for elem in results:
	#print elem
	aa = elem
	source = aa['_source']
	b = source
	body = b['@Body']
	tags = b['@Tags']
	tags = tags[1:].replace(">","")
	tags = tags.replace("<"," ")
	tags = tags.split()
	text = body
	text = re.sub('(<pre><code>)((.|\n)*?)(<\/code><\/pre>)','',text)
	text = re.sub('<.*?>', '', text)
	#print text
	text = text.replace("<"," ")
	text = text.replace("/"," ")
	text = text.replace("\n"," ")
	text = text.replace(">"," ")
	text = text.replace("&nbsp"," ")
	text = text.replace("&gt;", " ")
	text = text.replace("&lt;", " ")
	finalkeys = []
	keywords = rake_object.run(text)
	for a in keywords:
	    if ' ' not in a[0] and len(a[0])>3:
	        finalkeys.append(a)
	stri = "question number "+str(b['@Id'])+"\n"
	keys =  "keywords: "+str(finalkeys)+"\n"
	tags =  "og tags: "+ str(tags)+"\n\n"
	f1.write(stri)
	f1.write(keys)
	f1.write(tags)
	#break