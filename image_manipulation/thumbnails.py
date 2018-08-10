from PIL import Image

size = (128, 128)

image = Image.open("imagenes/imagen1.jpeg")
image.thumbnail(size)
image.save("imagenes_proc/imagen1._thumbnail.jpeg")
