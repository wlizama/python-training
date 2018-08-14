from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

story.append(Paragraph('Esta es la cabecera', styleH))
story.append(Paragraph('Este es un parrafo en <i>Normal</i> style.', styleN))
story.append(Paragraph('''Lorem ipsum dolor sit amet, consectetur adipisicing
    elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
    voluptate velit ess cillum dolore eu fugiat nulla pariatur. Excepteur sint
    occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
    anim id est laborum.''', styleN))
canvas = Canvas('pdfs/frames_sample.pdf')
frame = Frame(inch, inch, 6 * inch, 9 * inch, showBoundary=1)  # dibujar frame
frame.addFromList(story, canvas)
canvas.save()
