import random


def run():
  numberFound = False
  randomNumber = random.randint(0, 20)

  while not numberFound:
    numberInput = int(input("intenta un número: "))

    if numberInput == randomNumber:
      print("¡¡¡Encontraste el número!!!")
      numberFound = True
    elif numberInput > randomNumber:
      print("el número es más pequeño")
    else:
      print("El número es mas grande")

if __name__ == '__main__':
  run()