"""
Descargar MySQL Connector
https://dev.mysql.com/downloads/connector/python/

MySQL documentación
https://dev.mysql.com/doc/

Instalación connector por pip
pip install mysql-connector
"""
import mysql.connector
import configparser

config = configparser.ConfigParser()

config.read("dbconfig.ini")

micon = mysql.connector.connect(
    user=config["MYSQL"]["USER"],
    password=config["MYSQL"]["PASSWORD"],
    host=config["MYSQL"]["HOST"],
    database=config["MYSQL"]["DATABASE"]
)

cursor = micon.cursor()

# # Procedimiento sin parametros
# cursor.callproc("SP_ContactosLista")
# for result in cursor.stored_results():
#     print(result.fetchall())


# # Procedimiento con parametros de entrada y salida
# params = (
#     0,
#     "Alfonzo Palacios",
#     "Panchito Palacios",
#     "753162489",
#     "07/12"
# )
# result = cursor.callproc("SP_ContactosInsertar", params)
# print("Se insertó el registro ID: {}". format(result[0]))


# Procedimiento con entrada y resultado
params = ("WilyColon",)
cursor.callproc("SP_ContactosBuscaXApodo", params)
for result in cursor.stored_results():
    print(result.fetchall())

micon.commit()

micon.close()
