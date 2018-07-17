import re


def run():
  print("Buscar palabras que comiencen con la letra 't'")
  print(re.findall(r'\bt[a-z]*', 'tres felices tigres comen trigo'))

  print("\n")

  print("Cuando se necesita algo más sencillo solamente, se prefieren los\n"
  "métodos de las cadenas porque son más fáciles de leer y depurar.")
  print('te para tos'.replace('tos', 'dos'))

  print("\n")

  print("Los objetos coincidentes siempre tienen un valor booleano de True.\n"
  "Como match () y search () devuelven None cuando no coinciden, se puede\n"
  "probar si hubo una coincidencia con una instrucción if simple:")
  if(re.search(r"[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}", "super.email@valido.net")):
    print("e-mail correcto")
  else:
    print("e-mail incorrecto")


if __name__ == '__main__':
  run()