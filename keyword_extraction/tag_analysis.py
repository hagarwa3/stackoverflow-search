import RAKE.RAKE as rake
import operator
import json
import re
f1 = open('extratest/resultantPython.json','w')
f = open('extratest/python10000.json','r') 
rake_object = rake.Rake("smartstoplist.txt")
parsed_input = json.load(f)
stopwords = {}
f3 = open("smartstoplist.txt","r")
f4 = open("extratest/fullfilePython.txt","w")
for line in f3:
	stopwords[line[0:-1]]= 1
#print stopwords
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
	text2 = text
	finalkeys = []
	keywords = rake_object.run(text)
	for a in keywords:
	    if ' ' not in a[0] and len(a[0])>3:
	        finalkeys.append(a)
	text3 = re.sub('[^a-zA-Z0-9 \n\.]', ' ', text2)
	text3 = text3.lower()
	text3 = text3.split()
	text4 = []
	for word in text3:
		if word not in stopwords:
			text4.append(word)
	text5 = ' '.join(text4)
	f4.write(text5)
	f4.write("\n")
	curr = json.dumps({"question number": b['@Id'], "keywords": finalkeys, "og": tags , "words": text4})

	# stri = "question number "+str(b['@Id'])+"\n"
	# keys =  "keywords: "+str(finalkeys)+"\n"
	# tags =  "og tags: "+ str(tags)+"\n\n"
	# f1.write(stri)
	# f1.write(keys)
	# f1.write(tags)
	f1.write(curr)
	f1.write("\n")
	#break