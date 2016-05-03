import RAKE.RAKE as rake
import operator
from flask import Flask, request, render_template
import json
from flask.ext.cors import CORS
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={"/*": {"origins": "*"}})


@app.route("/gettags/", methods=['GET'])
def gettags():
	text = request.args.get('text')
	text = text.replace("%22","")
	text = text.replace('"',"")
	text = text.replace("<"," ")
	text = text.replace("/"," ")
	text = text.replace("\n"," ")
	text = text.replace(">"," ")
	text = text.replace("&nbsp"," ")
	text = text.replace("&gt;", " ")
	text = text.replace("&lt;", " ")
	print text
	rake_object = rake.Rake("smartstoplist.txt")
	finalkeys = []
	keywords = rake_object.run(text)
	for a in keywords:
	    if ' ' not in a[0]:
	        finalkeys.append(a)
	tags=""
	counter = 0
	for i in xrange(len(finalkeys)):
		if i<3:
			tags += finalkeys[i][0]+" "
		else:
			break
	tags = tags.strip()
	print tags
	return tags


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port, debug = True)
    app.run(debug = True)
