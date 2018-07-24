import xlsxwriter

workbook = xlsxwriter.Workbook("xls/filtros.xlsx")
worksheet = workbook.add_worksheet("Ficha con filtros")

# declaramos formatos a usar en celdas
bold = workbook.add_format({"bold": True})

# escribimos las cabeceras
worksheet.write("A1", "#", bold)
worksheet.write("B1", "Nombre", bold)
worksheet.write("C1", "Nota 1", bold)
worksheet.write("D1", "Nota 2", bold)
worksheet.write("E1", "Nota 3", bold)
worksheet.write("F1", "Promedio", bold)

# anchos de columna
worksheet.set_column("A:A", 3)
worksheet.set_column("B:B", 20)
worksheet.set_column("C:F", 8)

worksheet.autofilter("B1:F1") # filtro automatico

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
for nombre, nota_1, nota_2, nota_3 in (datos):
  worksheet.write(row, col, row)
  worksheet.write(row, col + 1, nombre)
  worksheet.write(row, col + 2, nota_1)
  worksheet.write(row, col + 3, nota_2)
  worksheet.write(row, col + 4, nota_3)
  worksheet.write(row, col + 5, (nota_1+nota_2+nota_3)/3)
  row += 1

worksheet.filter_column("B", "x == Oscan*")
workbook.close()