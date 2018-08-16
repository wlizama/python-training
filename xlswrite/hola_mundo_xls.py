import xlsxwriter

"""
Al especificar un nombre de archivo, se recomienda que use una
extensión .xlsx o Excel generará una advertencia al abrir el archivo.
"""
workbook = xlsxwriter.Workbook("xls/hola_mundo_xls.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "Hola mundo excel desde Python")

workbook.close()
