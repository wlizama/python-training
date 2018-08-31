"""Bar Chart

Gráfico de barras generado con reportlab
https://www.reportlab.com/docs/reportlab-userguide.pdf página:110
"""

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart

draw = Drawing(640, 320)

data = [
    (13, 25, 35,  4, 30, 35),
    (15, 15, 20, 25, 33, 38)
]

vbc = VerticalBarChart()
vbc.x = 120
vbc.y = 50
vbc.height = 125
vbc.width = 300
vbc.data = data
vbc.strokeColor = colors.black

vbc.valueAxis.valueMin = 0
vbc.valueAxis.valueMax = 50
vbc.valueAxis.valueStep = 10

vbc.categoryAxis.labels.boxAnchor = 'ne'
vbc.categoryAxis.labels.dx = 8
vbc.categoryAxis.labels.dy = -2
vbc.categoryAxis.labels.angle = 30
vbc.categoryAxis.categoryNames = ['Jan-99','Feb-99','Mar-99','Apr-99',
    'May-99','Jun-99','Jul-99','Aug-99']

draw.add(vbc)

renderPDF.drawToFile(draw, "pdfs/chart01.pdf", "Gráficos - Bar Chart")
