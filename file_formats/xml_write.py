import xml.etree.ElementTree as ET

# la estructura XML
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# tree = ET.ElementTree(data)

# Creamos el archivo
mydata = ET.tostring(data)  
myfile = open("files/xml_sample_created1.xml", "w")  
myfile.write(mydata)