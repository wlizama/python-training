import xlsxwriter

workbook = xlsxwriter.Workbook("xls/filtros.xlsx")
worksheet1 = workbook.add_worksheet("Ficha con filtros por condición")
# worksheet2 = workbook.add_worksheet("Ficha con filtros por condicion")

# declaramos formatos a usar en celdas
bold = workbook.add_format({"bold": True})

# escribimos las cabeceras
worksheet1.write("A1", "Nombre", bold)
worksheet1.write("B1", "Nota 1", bold)
worksheet1.write("C1", "Nota 2", bold)
worksheet1.write("D1", "Nota 3", bold)

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

workbook.close()