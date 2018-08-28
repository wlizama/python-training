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

# Creación de tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos(
id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(250),
apodo VARCHAR(100),
numero VARCHAR(10),
cumpleanhos VARCHAR(5),
PRIMARY KEY (id)
)""")

micon.commit()

micon.close()
