"""Pie Chart

Gráfico circular generado con reportlab
https://www.reportlab.com/docs/reportlab-userguide.pdf página:116
"""

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.piecharts import Pie

draw = Drawing(640, 320)

pc = Pie()
pc.x = 80
pc.y = 80
pc.width = 80
pc.height = 80
pc.data = [10, 20, 30, 40, 50, 60]
pc.labels = ['a', 'b', 'c', 'd', 'e', 'f']
pc.slices.strokeWidth = 0.5
pc.slices[3].popout = 10
pc.slices[3].strokeWidth = 2
pc.slices[3].strokeDashArray = [2, 2]
pc.slices[3].labelRadius = 1.75
pc.slices[3].fontColor = colors.red

draw.add(pc)

renderPDF.drawToFile(draw, "pdfs/chart03.pdf", "Gráficos - Pie Chart")
