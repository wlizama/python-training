"""
Para insertar imagenes en un documento PDF ReportLab hace uso
de la librería Pillow, que se instala sencillamente vía pip install Pillow.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("pdfs/pdf_con_imagen.pdf")
c.drawString(240, h - 240, "PDF con imagen")
c.drawImage("imagen_para_pdf.jpg", 140, h - 500, width=320, height=240)
c.showPage()
c.save()
