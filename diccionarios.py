
calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 9
calificaciones['web'] = 7
calificaciones['bases_de_datos'] = 8
calificaciones['Fundamentos'] = 8

print("## Iterar llaves ##")
for key in calificaciones:
    print(key)

print("\n")

print("## Iterar Valores ##")
for value in calificaciones.values():
    print(value)

print("\n")

print("## Iterar en ítems ##")
for key, value in calificaciones.items():
    print("llave: {}, valor: {}".format(key, value))
