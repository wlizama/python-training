"""
  https://docs.python.org/3.7/library/csv.html
"""
import csv, sys

def printCSV():
  """
   Imprimir cada una de las filas en el archivo
  """
  with open('files/FL_insurance_sample.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
      print(row)

def excepciones():
  """
  Manejo de excepciones
  """
  filename = 'files/FL_insurance_sample.csv'
  with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
      for row in reader:
        print(row)
    except csv.Error as e:
      sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

if __name__ == '__main__':
  opcion = int(input(
    """
    [1] Imprimir cada una de las filas en el archivo
    [2] Manejo de Excepciones
    """
    ))

  if opcion == 1:
    printCSV()
  if opcion == 2:
    excepciones()