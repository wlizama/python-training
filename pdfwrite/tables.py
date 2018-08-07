from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc = SimpleDocTemplate("pdfs/simple_table.pdf", pagesize=A4)

# Contenedor para elementos 'Flowable'
elements = []

data = [
	[ '00', '01', '02', '03', '04' ],
	[ '10', '11', '12', '13', '14' ],
	[ '20', '21', '22', '23', '24' ],
	[ '30', '31', '32', '33', '34' ]
]

table = Table(data)

"""
La celda superior izquierda es (0, 0) la inferior derecha es (-1, -1)
"""
table.setStyle(TableStyle([
	('BACKGROUND', (1,1), (-2,-2), colors.green),
	('TEXTCOLOR', (0,0), (1,-3), colors.red),
	('TEXTCOLOR', (-2,0), (-1,-3), colors.red),
	('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), # lineas internas en grilla
	('BOX', (0,0), (-1,-1), 0.25, colors.black)        # Borde exterior de grilla
]))

elements.append(table)

doc.build(elements)