import os
from Lamp import Lamp

def run():
    myLamp = Lamp(False)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        os.system('clear') # linux o os x

        if command == 'p':
            myLamp.turnOn()
        elif command == 'a':
            myLamp.turnOff()
        else:
            break
            

if __name__ == '__main__':
    run()

