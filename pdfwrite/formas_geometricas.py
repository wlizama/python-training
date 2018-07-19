from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("pdfs/formas_geometricas.pdf", pagesize=A4)

"""
El método setFillColoRGB(red,green,blue) establece el color de relleno de cualquier objeto dibujado en la hoja
"""
c.setFillColorRGB(1,0,0)

"""
El método setStrokeColorRGB(red,green,blue) establece el color del borde de las figuras.
"""
c.setStrokeColorRGB(0,1,0)

"""
Para alterar la fuente y el tamaño del texto dibujado vía drawString(), empleamos setFont(fontname, size).
"""
c.setFont("Helvetica", 15)

c.drawString(30, h - 50, "Línea")
x = 120
y = h - 45
# X punto inicio, Y punto inicio, X punto fin, Y punto fin
c.line(x, y, x + 100, y)

c.drawString(30, h - 100, "Rectángulo")
# X punto de inicio, Y punto de inicio, ancho, alto
c.rect(x, h - 120, 100, 50, fill=True)

c.setFillColorRGB(0,0,1)
c.setStrokeColorRGB(1,0,0)
c.setFont("Times-Roman", 20)

c.drawString(30, h - 170, "Círculo")
# X punto centro, Y punto centro, radio
c.circle(170, h - 165, 20)

c.drawString(30, h - 240, "Elipse")
# X punto inicio, Y punto inicio, X punto fin, Y punto fin
c.ellipse(x, y - 170, x + 100, y - 220, fill=True)

c.showPage()
c.save()