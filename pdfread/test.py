import PyPDF2
from pprint import pprint

FILE_PDF = 'D:\\my\\dir\\20457896321-01-F111-1123.PDF'

if __name__ == "__main__":
    filePDFReader = PyPDF2.PdfFileReader(FILE_PDF)
    pageObj =  filePDFReader.getPage(0)

    xObject = pageObj['/Resources']['/XObject'].getObject()
    for obj in xObject:
        data = xObject[obj]._data
        img = open("img_saved-%s.jpg" % obj.replace('/', ''), "wb")
        img.write(data)
        img.close()
        # if xObject[obj]['/Subtype'] == '/Image':
        #     pprint(xObject[obj])