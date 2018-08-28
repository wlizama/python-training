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

con = mysql.connector.connect(
    user=config["MYSQL"]["USER"],
    password=config["MYSQL"]["PASSWORD"],
    host=config["MYSQL"]["HOST"],
    database=config["MYSQL"]["DATABASE"]
)

con.close()
