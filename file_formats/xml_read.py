import xml.etree.ElementTree as ET

tree = ET.parse("files/xml_sample1.xml")
root = tree.getroot()

print("# Raiz de XML", root, "con tag:", root.tag, ", atributos:", root.attrib)

print("\n# Elementos Hijos")
for child in root:
  print(child.tag, child.attrib)

print("\n# Búsqueda de elementos")
for neighbor in root.iter('neighbor'):
  print(neighbor.attrib)

print()
for country in root.findall('country'):
  rank = country.find('rank').text
  name = country.get('name')
  print(name, rank)

print()
print("# Búsqueda por XPath")
print(root.findall("./country[@name='Panama']")[0].attrib)