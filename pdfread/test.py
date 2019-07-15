import PyPDF2
from pprint import pprint

FILE_PDF = 'D:\\my\\dir\\20100010217-01-F001-123.PDF'

if __name__ == "__main__":
    filePDFReader = PyPDF2.PdfFileReader(FILE_PDF)
    pageObj =  filePDFReader.getPage(0)

    xObject = pageObj['/Resources']['/XObject'].getObject()
    for obj in xObject:
        pprint(xObject[obj])
        # if xObject[obj]['/Subtype'] == '/Image':
        #     pprint(xObject[obj])