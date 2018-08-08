"""
Ejemplo PDF con multiples paginas generadas por cantidad de parrafos,
se establece estilo en primera pagina y diferente para las que le siguen
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]

styles = getSampleStyleSheet()

Title = "Hello Platypus"
pageinfo = "platypus sample"


def myFirtsPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(
        PAGE_WIDTH / 2.0, PAGE_HEIGHT - 108, Title)  # x, y, texto
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" %
                      pageinfo)   # x, y, texto
    canvas.restoreState()


def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d / %s" % (doc.page, pageinfo))


def go():
    doc = SimpleDocTemplate('pdfs/platypus_sample.pdf')
    Story = [Spacer(1, 1 * inch)]  # espacio desde titulo
    style = styles['Normal']

    for i in range(100):
        bogustext = ("Este parrafo es número %s.  " % i) * 20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))  # espacio entre parrafo

    doc.build(Story, onFirstPage=myFirtsPage, onLaterPages=myLaterPages)


if __name__ == '__main__':
    go()
