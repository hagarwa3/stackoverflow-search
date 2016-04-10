import xml.etree.ElementTree as ET
tree = ET.parse('Posts.xml')
root = tree.getroot()

for row in root:
    text = row.text
    if 'PostTypeId="2"' in text:
        root.remove(row)
