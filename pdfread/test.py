import PyPDF2
from pyzbar.pyzbar import decode, _image_scanner
from PIL import Image
from io import BytesIO, StringIO
# from StringIO import StringIO
from pprint import pprint
import struct

# FILE_PDF = 'C:\\Users\\Wilder\\Downloads\\20100412447-01-F005-39776.pdf' # FAIL
# FILE_PDF = 'D:\\FElectronicaProveedor\\inbound\\20100010136_01_F001-3011_7488862_RN88960.PDF' # to check
FILE_PDF = 'D:\\FElectronicaProveedor\\inbound\\-01-F021-00010588.PDF'


def image1():
    filePDFReader = PyPDF2.PdfFileReader(open(FILE_PDF, 'rb'))
    pageObj =  filePDFReader.getPage(0)

    if '/XObject' in pageObj['/Resources']:
        xObject = pageObj['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                # data = xObject[obj].getData()
                data = xObject[obj]._data
                
                mode = ''
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB' or \
                   '/DeviceRGB' in xObject[obj]['/ColorSpace']:
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
                        img = Image.open(data)
                        # print("here 02")
                    elif xfilter == '/JPXDecode':
                        img = Image.open(data)
                        # print("here 03")
                    elif xfilter == '/CCITTFaxDecode':
                        img = Image.open(data)
                        # print("here 04")
                else:
                    img = Image.frombytes(mode, size, data)
                    # print("here 05")
                
                # print(decode(img))v
                # print(scanner.scan(img))
    else:
        print("No image found :/")


def image2():
    filePDFReader = PyPDF2.PdfFileReader(open(FILE_PDF, 'rb'))
    pageObj =  filePDFReader.getPage(0)
    extract_images(pageObj)


def tiff_header_for_CCITT(width, height, img_size, CCITT_group=4):
    tiff_header_struct = '<' + '2s' + 'h' + 'l' + 'h' + 'hhll' * 8 + 'h'
    return struct.pack(tiff_header_struct,
                       b'II',  # Byte order indication: Little indian
                       42,  # Version number (always 42)
                       8,  # Offset to first IFD
                       8,  # Number of tags in IFD
                       256, 4, 1, width,  # ImageWidth, LONG, 1, width
                       257, 4, 1, height,  # ImageLength, LONG, 1, lenght
                       258, 3, 1, 1,  # BitsPerSample, SHORT, 1, 1
                       259, 3, 1, CCITT_group,  # Compression, SHORT, 1, 4 = CCITT Group 4 fax encoding
                       262, 3, 1, 0,  # Threshholding, SHORT, 1, 0 = WhiteIsZero
                       273, 4, 1, struct.calcsize(tiff_header_struct),  # StripOffsets, LONG, 1, len of header
                       278, 4, 1, height,  # RowsPerStrip, LONG, 1, lenght
                       279, 4, 1, img_size,  # StripByteCounts, LONG, 1, size of image
                       0  # last IFD
                       )


def extract_images(page, filename_prefix="IMG_", start_index=0):
    img_modes = {'/DeviceRGB': 'RGB', '/DefaultRGB': 'RGB',
             '/DeviceCMYK': 'CMYK', '/DefaultCMYK': 'CMYK',
             '/DeviceGray': 'L', '/DefaultGray': 'L',
             '/Indexed': 'P'}
    
    xObject = page['/Resources']['/XObject'].getObject()

    i = start_index
    for obj in xObject:
        print("extracting to {}{:04}.xxx".format(filename_prefix, i))
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            color_space = xObject[obj]['/ColorSpace']
            if isinstance(color_space, PyPDF2.generic.ArrayObject) and color_space[0] == '/Indexed':
                color_space, base, hival, lookup = [v.getObject() for v in color_space] # pg 262
            mode = img_modes[color_space]

            if xObject[obj]['/Filter'] == '/FlateDecode':
                data = xObject[obj].getData()
                img = Image.frombytes(mode, size, data)
                if color_space == '/Indexed':
                    img.putpalette(lookup.getData())
                    img = img.convert('RGB')
                img.save("{}{:04}.png".format(filename_prefix, i))
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                data = xObject[obj]._data
                img = open("{}{:04}.jpg".format(filename_prefix, i), "wb")
                img.write(data)
                img.close()
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                data = xObject[obj]._data
                img = open("{}{:04}.jp2".format(filename_prefix, i), "wb")
                img.write(data)
                img.close()
#            The  CCITTFaxDecode filter decodes image data that has been encoded using
#            either Group 3 or Group 4 CCITT facsimile (fax) encoding. CCITT encoding is
#            designed to achieve efficient compression of monochrome (1 bit per pixel) image
#            data at relatively low resolutions, and so is useful only for bitmap image data, not
#            for color images, grayscale images, or general data.
#
#            K < 0 --- Pure two-dimensional encoding (Group 4)
#            K = 0 --- Pure one-dimensional encoding (Group 3, 1-D)
#            K > 0 --- Mixed one- and two-dimensional encoding (Group 3, 2-D)
            elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                if xObject[obj]['/DecodeParms']['/K'] == -1:
                    CCITT_group = 4
                else:
                    CCITT_group = 3
                width = xObject[obj]['/Width']
                height = xObject[obj]['/Height']
                data = xObject[obj]._data  # sorry, getData() does not work for CCITTFaxDecode
                img_size = len(data)
                tiff_header = tiff_header_for_CCITT(width, height, img_size, CCITT_group)
                img_name = "{}{:04}.tiff".format(filename_prefix, i)
                with open(img_name, 'wb') as img_file:
                    img_file.write(tiff_header + data)
            i += 1

    return i


def image3():
    pdf_file = open(FILE_PDF, 'rb')
    cond_scan_reader = PyPDF2.PdfFileReader(pdf_file)
    for i in range(0, cond_scan_reader.getNumPages()):
        page = cond_scan_reader.getPage(i)
        xObject = page['/Resources']['/XObject'].getObject()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                """
                The  CCITTFaxDecode filter decodes image data that has been encoded using
                either Group 3 or Group 4 CCITT facsimile (fax) encoding. CCITT encoding is
                designed to achieve efficient compression of monochrome (1 bit per pixel) image
                data at relatively low resolutions, and so is useful only for bitmap image data, not
                for color images, grayscale images, or general data.

                K < 0 --- Pure two-dimensional encoding (Group 4)
                K = 0 --- Pure one-dimensional encoding (Group 3, 1-D)
                K > 0 --- Mixed one- and two-dimensional encoding (Group 3, 2-D)
                """
                if xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                    if xObject[obj]['/DecodeParms']['/K'] == -1:
                        CCITT_group = 4
                    else:
                        CCITT_group = 3
                    width = xObject[obj]['/Width']
                    height = xObject[obj]['/Height']
                    data = xObject[obj]._data  # sorry, getData() does not work for CCITTFaxDecode
                    img_size = len(data)
                    tiff_header = tiff_header_for_CCITT(width, height, img_size, CCITT_group)
                    img_name = obj[1:] + '.tiff'
                    with open(img_name, 'wb') as img_file:
                        img_file.write(tiff_header + data)
                    #
                    # import io
                    # from PIL import Image
                    # im = Image.open(io.BytesIO(tiff_header + data))
    pdf_file.close()


if __name__ == "__main__":
    image2()