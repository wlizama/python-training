import xml.etree.ElementTree as ET

# la estructura XML
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'Contenido del item 1'
item2.text = 'Contenido del item 2'

tree = ET.ElementTree(data)

# Creamos el archivo
tree.write("files/xml_sample_created1.xml")