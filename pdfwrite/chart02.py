"""Line Chart

Gráfico de Lineas generado con reportlab
https://www.reportlab.com/docs/reportlab-userguide.pdf página:113
"""

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.linecharts import HorizontalLineChart

draw = Drawing(640, 320)

data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (5, 20, 46, 38, 23, 21, 6, 14)
]

hlc = HorizontalLineChart()
hlc.x = 50
hlc.y = 50
hlc.height = 125
hlc.width = 300
hlc.data = data
hlc.joinedLines = 1

catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')

hlc.categoryAxis.categoryNames = catNames
hlc.categoryAxis.labels.boxAnchor = 'n'

hlc.valueAxis.valueMin = 0
hlc.valueAxis.valueMax = 60
hlc.valueAxis.valueStep = 15

hlc.lines[0].strokeWidth = 2
hlc.lines[1].strokeWidth = 1.5

draw.add(hlc)

renderPDF.drawToFile(draw, "pdfs/chart02.pdf", "Gráficos - Line Chart")
