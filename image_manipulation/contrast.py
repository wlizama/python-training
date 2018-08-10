from PIL import Image

image = Image.open("imagenes/imagen1.jpeg")
image = image.convert("L")
image.save("imagenes_proc/imagen1._contrast.jpeg")
