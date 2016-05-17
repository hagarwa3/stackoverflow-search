import json
import operator
d = {}
f1 = open('resultantPython.json','r')
f2 = open("pythonCounts.txt","w")
for line in f1:
	js = json.loads(line)
	#print js['keywords'][0][0]
	for a in js['words']:
		try:
			d[a]+=1
		except:
			d[a]=1

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
f2.write(str(sorted_d))

	#break