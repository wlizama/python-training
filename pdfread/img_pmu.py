import fitz
from pyzbar.pyzbar import decode
from PIL import Image

doc = fitz.open("Q:\\my\\dir\\F001-1048.PDF")
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None

if __name__ == "__main__":
    print(decode(Image.open("W:\\my\\images\\dir\\p0-7.png")))