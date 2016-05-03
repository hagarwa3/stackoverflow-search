import json, xmljson
from lxml.etree import fromstring
f = open("C:\Users\Harshit Agarwal\Desktop\stackoverflow.com-Posts\Postsnewjson4.txt", "w")
with open("C:\Users\Harshit Agarwal\Desktop\stackoverflow.com-Posts\Postsnew.xml") as fileobject:
    i = 0
    for i in xrange(5):
        fileobject.next()
    for line in fileobject:
        if len(line)>40:
            xml = fromstring(line)
            a = json.dumps(xmljson.badgerfish.data(xml))
            a= a[8:-1] + "\n"
            f.write(a)

f.close()