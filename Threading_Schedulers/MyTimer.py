"""
Imprimir un mensaje despues de n segundos
"""

from threading import Timer

def sayHi(nm):
    print("Hi with Timer arg1:", nm)


def startTimer():
    t = Timer(5, sayHi, args=["Wily"])
    t.start()


if __name__ == "__main__":
    startTimer()