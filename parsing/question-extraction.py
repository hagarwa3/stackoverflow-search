f = open("C:\Users\Harshit Agarwal\Desktop\stackoverflow.com-Posts\Postsnew.xml", "w")
f.write('<?xml version="1.0" encoding="utf-8"?>\n<posts>')
i = 0
with open("C:\Users\Harshit Agarwal\Desktop\stackoverflow.com-Posts\Posts.xml") as fileobject:
    for line in fileobject:
        i +=1
        if 'PostTypeId="1"' in line:
            if i%100000 == 0:
                print i
            f.write(line)
f.write('</posts>')
f.close()