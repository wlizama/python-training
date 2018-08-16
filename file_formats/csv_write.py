import csv
import random


def writeWithHeaders():
    with open('files/sample_write.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def writeSimple():
    with open('files/sample_write.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for x in range(1, 100):
            spamwriter.writerow(
                [str(x), 'Col 1 - fila ' + str(x), str(random.random())])


if __name__ == '__main__':
    opcion = int(input(
        """
    [1] Escritura simple
    [2] Escritura con cabeceras
    """
    ))

    if opcion == 1:
        writeSimple()
    if opcion == 2:
        writeWithHeaders()
