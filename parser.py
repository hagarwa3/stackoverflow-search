import xml.etree.ElementTree as ET
tree = ET.parse('Posts.xml')
root = tree.getroot()

rows = tree.findall(".//row[@PostTypeId='2']")
for elem in rows:
    root.remove(elem)

tree.write('cut.xml')
