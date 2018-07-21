import xlsxwriter

workbook = xlsxwriter.Workbook("xls/cell_formats.xlsx")
worksheet = workbook.add_worksheet("Ficha Rasputina")

# declaramos formatos a usar en celdas
bold = workbook.add_format({"bold": True})
moneda = workbook.add_format({"num_format": "#,##0"})

# escribimos las cabeceras
worksheet.write("A1", "Item", bold)
worksheet.write("B1", "Costo", bold)

# data a escribir
gastos = (
  ["Alquiler", 600],
  ["Comida", 80],
  ["Gas", 30],
  ["Pasajes", 20],
  ["Internet", 120],
)

# las filas despues de las cabeceras
row = 1
col = 0

# iteramos para escribir las filas
for item, cost in (gastos):
  worksheet.write(row, col, item)
  worksheet.write(row, col + 1, cost, moneda)
  row += 1

# escribimos el total usando formula
worksheet.write(row, 0, "Total", bold)
worksheet.write(row, 1, "=SUM(B2:B6)", moneda)

workbook.close()