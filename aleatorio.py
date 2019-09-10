import random

RSTART = 0
RLIMIT = 1024
CNUMS = 1024


def adivinaAleatorio():
    numberFound = False
    randomNumber = random.randint(RSTART, RLIMIT)

    while not numberFound:
        numberInput = int(input("intenta un número: "))

        if numberInput == randomNumber:
            print("¡¡¡Encontraste el número!!!")
            numberFound = True
        elif numberInput > randomNumber:
            print("el número es más pequeño")
        else:
            print("El número es mas grande")


def randonList():
    rnd_list = [random.randint(RSTART, RLIMIT) for i in range(CNUMS)]
    print(rnd_list)


def randonListFnrandrange():
    rnd_list = [random.randrange(RSTART, RLIMIT) for i in range(CNUMS)]
    print(rnd_list)


def randonListNoRepeat():
    rnd_list = random.sample(range(RSTART, RLIMIT), CNUMS)
    print(rnd_list)


if __name__ == '__main__':
    option = int(input("""
    Prueba de %i números aleatorios generados desde %i hasta %i
    Seleccionar opcion:
    
    [1] Prueba adivinar aleatorio
    [2] Imprimir lista de aleatorios
    [3] Imprimir lista de aleatorios con funcion 'randrange'
    [4] Imprimir lista de aleatorios sin repetir
    """ % (CNUMS, RSTART, RLIMIT)))

    if option == 1:
        adivinaAleatorio()
    elif option == 2:
        randonList()
    elif option == 3:
        randonListFnrandrange()
    elif option == 4:
        randonListNoRepeat()
    else:
        print("No existe opción")
