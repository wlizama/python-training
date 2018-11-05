"""
Consulta SOAP factura a SUNAT usando zeep con credenciales wsse UsernameToken

https://python-zeep.readthedocs.io/en/master/index.html
"""
import zeep
from zeep.wsse.username import UsernameToken

RUC = "12345678901"
SOL_USER = "panchofierro"
SOL_PASSWORD = "fierritopower"
TOKEN_USER = "{0}{1}".format(RUC, SOL_USER)
TOKEN_PASSWORD = SOL_PASSWORD


client = zeep.Client(
    "https://www.sunat.gob.pe/ol-it-wsconscpegem/billConsultService?wsdl",
    wsse=UsernameToken(TOKEN_USER, TOKEN_PASSWORD)
    )

print(client.service.getStatus(
    RUC,
    "01",
    "F001",
    "1"
))