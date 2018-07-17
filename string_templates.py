from string import Template


print("""El método substitute() lanza KeyError cuando no se suministra ningún valor para un marcador mediante un
diccionario o argumento por nombre.""")
myTemp = Template("La ${fruta} es una fruta ${sabor} y cuesta $$15") # $$ genera un $
result1 = myTemp.substitute(fruta="pera", sabor="dulce")

print(result1)


myDict = dict(fruta="manzana")
result2 = myTemp.safe_substitute(myDict)
print(result2)

