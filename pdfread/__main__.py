import PyPDF2

def findFile(fullNameFile):
    fileToFind = None
    try:
        fileToFind = open(fullNameFile, "rb")
    except FileNotFoundError:
        pass
    return fileToFind


def execute():

    _strRUCEmisor = "20123456789"
    _strTipoDocEmisor = "07"
    _strSerieDocEmisor = "F005"
    _filePDFNumDesde = 1
    _filePDFNumHasta = 999

    for num in list(range(_filePDFNumDesde, _filePDFNumHasta + 1)):
        strFileNameToFind = "%s-%s" %(_strSerieDocEmisor, str(num))
        filePDF = findFile("W:\\DIR\\TO\\SEARCH\\%s-%s-%s.PDF"
                           %(_strRUCEmisor, _strTipoDocEmisor, strFileNameToFind))
        if filePDF != None:
            filePDFReader = PyPDF2.PdfFileReader(filePDF)
            pageObj =  filePDFReader.getPage(0)
            fullTextPDF = pageObj.extractText()

            strIni = "RUC: 20987654321"
            strTextLimit = "SEÑORES: XXX"

            strFound = fullTextPDF[len(strIni)-1:fullTextPDF.find(strTextLimit)]
            strFound = strFound.replace(" ", "")

            if strFileNameToFind != strFound:
                print("strFileNameToFind: %s, strFound: %s" %(strFileNameToFind, strFound))



if __name__ == "__main__":
    execute()