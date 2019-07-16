import PyPDF2
from pprint import pprint

FILE_PDF = 'D:\\FElectronicaProveedor\\inbound\\20109969452-01-F012-00015589.PDF'

if __name__ == "__main__":
    filePDFReader = PyPDF2.PdfFileReader(FILE_PDF)
    pageObj =  filePDFReader.getPage(0)

    xObject = pageObj['/Resources']['/XObject'].getObject()
    for obj in xObject:
        data = xObject[obj]._data
        print(data)
        # img = open("img_saved-%s.jpg" % obj.replace('/', ''), "wb")
        # img.write(data)
        # img.close()