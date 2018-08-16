"""
Ejemplo con los diferentes formatos de fecha y hora
"""
from datetime import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('xls/fechas_horas.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

# Darle mas ancho a las columnas
worksheet.set_column('A:B', 30)

worksheet.write('A1', 'Formatted date', bold)
worksheet.write('B1', 'Format', bold)

date_time = datetime.strptime('2018-07-20 12:30:05.123',
                              '%Y-%m-%d %H:%M:%S.%f')

date_formats = (
    'dd/mm/yy',
    'mm/dd/yy',
    'dd m yy',
    'd mm yy',
    'd mmm yy',
    'd mmmm yy',
    'd mmmm yyy',
    'd mmmm yyyy',
    'dd/mm/yy hh:mm',
    'dd/mm/yy hh:mm:ss',
    'dd/mm/yy hh:mm:ss.000',
    'hh:mm',
    'hh:mm:ss',
    'hh:mm:ss.000',
)

row = 1

for date_format_str in date_formats:

    date_format = workbook.add_format({'num_format': date_format_str,
                                       'align': 'left'})

    worksheet.write_datetime(row, 0, date_time, date_format)
    worksheet.write_string(row, 1, date_format_str)

    row += 1

workbook.close()
