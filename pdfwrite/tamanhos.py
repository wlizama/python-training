"""
El tamaño por defecto es A4

Las dimensiones de una hoja están expresadas en puntos (points), no en píxeles, 
equivaliendo un punto a 1/72 pulgadas. Una hoja A4 está constituida por 595.2 puntos
de ancho (width) y 841.8 puntos de alto (height).

El módulo reportlab.lib.pagesizes provee las dimensiones de otros estándares

"""


# from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas

TAM_PERSONALIZADO = (280, 80) # A3

w, h = TAM_PERSONALIZADO
c = canvas.Canvas("pdfs/tamanho_diferene.pdf", pagesize=TAM_PERSONALIZADO)
c.drawString(50, h - 50, "¡Hola, mundo de Diferente tamaño!")
c.showPage()
c.save()