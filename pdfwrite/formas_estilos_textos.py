from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

## Página 1

w, h = A4
c = canvas.Canvas("pdfs/formas_estilos_textos.pdf", pagesize=A4)

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

## Página 2

"""
Cuando cambiamos la hoja (showPage()), los estilos se pierden y ─de ser necesario─ deben ser establecidos nuevamente.
"""
c.drawString(30, h - 50, "Este es un texto en otra página") # no tiene los estilos de la página anterior

"""
ReportLab incluye text objects, una forma más especializada de dibujar texto.
"""
texto = c.beginText(50, h - 100)                              # Lugar donde empezará el texto
texto.setFont("Courier", 20)                                  # setFont() actúa sobre el objeto en particular y no sobre el resto de la hoja.
texto.textLine("Texto agregado con objeto texto")             # Añadimos líneas de texto a nuestro objeto.
texto.textLine("esto es un salto de linea")
texto.textLines("Este Texto\ntambien tiene salto de linea")   # El método textLines() soporta el carácter de salto de línea.
c.drawText(texto)                                             # Se dibuja en la hoja

c.save()