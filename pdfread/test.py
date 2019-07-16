import PyPDF2
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
from pprint import pprint

FILE_PDF = 'C:\\Users\\Wilder\\Downloads\\20100412447-01-F005-39776.pdf'


if __name__ == "__main__":
    filePDFReader = PyPDF2.PdfFileReader(FILE_PDF)
    pageObj =  filePDFReader.getPage(0)

    if '/XObject' in pageObj['/Resources']:
        xObject = pageObj['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj]._data
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"
                
                img = None
                
                if '/Filter' in xObject[obj]:
                    xfilter = xObject[obj]['/Filter']
                    if xfilter == '/FlateDecode':
                        img = Image.frombytes(mode, size, data)
                        # print("here 01")
                    elif xfilter == '/DCTDecode':
                        img = Image.open(BytesIO(data))
                        # print("here 02")
                    elif xfilter == '/JPXDecode':
                        img = Image.open(BytesIO(data))
                        # print("here 03")
                    elif xfilter == '/CCITTFaxDecode':
                        img = Image.open(BytesIO(data))
                        # print("here 04")
                else:
                    img = Image.frombytes(mode, size, data)
                    # print("here 05")
                
                print(decode(img))
                print(img.info)
    else:
        print("No image found :/")