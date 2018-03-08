
def escribir():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))


def leer():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))


def run():
    cmd = str(input('''Que desea hacer?

        [e]scribir
        [l]eer
    '''))

    if cmd == 'e':
        escribir()
    elif cmd == 'l':
        leer()
    else:
        print('Opcion no reconocida')


if __name__ == '__main__':
    run()