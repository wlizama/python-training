import xlsxwriter

workbook = xlsxwriter.Workbook("xls/filtros.xlsx")

"""
  Primera Hoja
"""

worksheet1 = workbook.add_worksheet("Ficha con filtros por condición")

# declaramos formatos a usar en celdas
bold1 = workbook.add_format({"bold": True})

# escribimos las cabeceras
worksheet1.write("A1", "Nombre", bold1)
worksheet1.write("B1", "Nota 1", bold1)
worksheet1.write("C1", "Nota 2", bold1)
worksheet1.write("D1", "Nota 3", bold1)

# anchos de columna
worksheet1.set_column("A:A", 20)
worksheet1.set_column("B:D", 8)

worksheet1.autofilter("A1:D10") # filtro automatico
worksheet1.filter_column("C", 'x > 5')

# data a escribir
datos = (
  [ "Wilder Lizama", 8, 5, 2 ],
  [ "Pancho Fierro", 7, 8, 4 ],
  [ "Elizabeth II", 4, 6, 5 ],
  [ "Oscan d Leon",5, 8, 7 ],
  [ "Jonathan Davis", 6, 6, 6 ],
  [ "Rafhael Nadal", 9, 9, 6 ],
  [ "Erick Zuktraosqli", 2, 3, 7 ],
  [ "Fatima Jeager", 5, 8, 7 ],
  [ "Kiori hayutaru", 8, 6, 4],
)

# las filas despues de las cabeceras
row = 1
col = 0

# iteramos para escribir las filas
for row_data in (datos):
  nota_2 = row_data[2]

  # compruebamos si hay filas que coincidan con el filtro
  if nota_2 > 5:
    # la fila coincide con el filtro, muestra la fila normalmente
    pass
  else:
    # ocultamos las filas que no coinciden con el filtro.
    worksheet1.set_row(row, options={'hidden': True})

  worksheet1.write_row(row, 0, row_data)

  row += 1

"""
  Segunda Hoja
"""

worksheet2 = workbook.add_worksheet("Ficha con filtros de lista")

# declaramos formatos a usar en celdas
bold2 = workbook.add_format({"bold": True})

# escribimos las cabeceras
worksheet2.write("A1", "Nro. Mes", bold1)
worksheet2.write("B1", "Mes", bold1)

# anchos de columna
worksheet2.set_column("A:A", 5)
worksheet2.set_column("B:B", 10)

meses_filtrados = [4, 8, 11]

worksheet2.autofilter("A1:B13") # filtro automatico
worksheet2.filter_column_list('A', meses_filtrados)

# data a escribir
meses = (
  [  1, "Enero" ],
  [  2, "Febrero" ],
  [  3, "Marzo" ],
  [  4, "Abril" ],
  [  5, "Mayo" ],
  [  6, "Junio" ],
  [  7, "Julio" ],
  [  8, "Agosto" ],
  [  9, "Septiembre" ],
  [ 10, "Octubre" ],
  [ 11, "Noviembre" ],
  [ 12, "Diciembre" ]
)

# las filas despues de las cabeceras
row = 1
col = 0

# iteramos para escribir las filas
for row_data in (meses):
  mes = row_data[0]

  # compruebamos si hay filas que coincidan con el filtro
  if mes in meses_filtrados:
    # la fila coincide con el filtro, muestra la fila normalmente
    pass
  else:
    # ocultamos las filas que no coinciden con el filtro.
    worksheet2.set_row(row, options={'hidden': True})

  worksheet2.write_row(row, 0, row_data)

  row += 1

workbook.close()