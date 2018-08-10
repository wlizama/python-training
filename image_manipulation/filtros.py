from PIL import Image, ImageFilter

image_orig = Image.open("imagenes/imagen1.jpeg")

# BLUR
imBLUR = image_orig.filter(ImageFilter.BLUR)
imBLUR.save("imagenes_proc/filtros/imagen1.filtros_BLUR.jpeg")

# CONTOUR
imCONTOUR = image_orig.filter(ImageFilter.CONTOUR)
imCONTOUR.save("imagenes_proc/filtros/imagen1.filtros_CONTOUR.jpeg")

# DETAIL
imDETAIL = image_orig.filter(ImageFilter.DETAIL)
imDETAIL.save("imagenes_proc/filtros/imagen1.filtros_DETAIL.jpeg")

# EDGE_ENHANCE
imEDGE_ENHANCE = image_orig.filter(ImageFilter.EDGE_ENHANCE)
imEDGE_ENHANCE.save("imagenes_proc/filtros/imagen1.filtros_EDGE_ENHANCE.jpeg")

# EDGE_ENHANCE_MORE
imEDGE_ENHANCE_MORE = image_orig.filter(ImageFilter.EDGE_ENHANCE_MORE)
imEDGE_ENHANCE_MORE.save(
    "imagenes_proc/filtros/imagen1.filtros_EDGE_ENHANCE_MORE.jpeg")

# EMBOSS
imEMBOSS = image_orig.filter(ImageFilter.EMBOSS)
imEMBOSS.save("imagenes_proc/filtros/imagen1.filtros_EMBOSS.jpeg")

# FIND_EDGES
imFIND_EDGES = image_orig.filter(ImageFilter.FIND_EDGES)
imFIND_EDGES.save("imagenes_proc/filtros/imagen1.filtros_FIND_EDGES.jpeg")

# SHARPEN
imSHARPEN = image_orig.filter(ImageFilter.SHARPEN)
imSHARPEN.save("imagenes_proc/filtros/imagen1.filtros_SHARPEN.jpeg")

# SMOOTH
imSMOOTH = image_orig.filter(ImageFilter.SMOOTH)
imSMOOTH.save("imagenes_proc/filtros/imagen1.filtros_SMOOTH.jpeg")

# SMOOTH_MORE
imSMOOTH_MORE = image_orig.filter(ImageFilter.SMOOTH_MORE)
imSMOOTH_MORE.save("imagenes_proc/filtros/imagen1.filtros_SMOOTH_MORE.jpeg")
