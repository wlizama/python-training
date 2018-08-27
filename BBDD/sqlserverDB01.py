"""
Enlaces para solución de problemas

https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017#ubuntu-1404-1604-1710-and-1804

https://community.webfaction.com/questions/12976/im002-im002-unixodbcdriver-managerdata-source-name-not-found-and-no-default-driver-specified-0-sqldriverconnectw/17272
"""

import pyodbc
import configparser

# detect SQL Driver
# drivers_name = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
# drivers_name[1] if drivers_name else "SQL Server"
driver_name = "ODBC Driver 17 for SQL Server"

config = configparser.ConfigParser()

config.read("dbconfig.ini")

con = pyodbc.connect("DRIVER={};SERVER={};UID={};PWD={};DATABASE={};".format(
    driver_name,
    config["SQL_SERVER"]["SERVER"],
    config["SQL_SERVER"]["UID"],
    config["SQL_SERVER"]["PWD"],
    config["SQL_SERVER"]["DATABASE"]
))

cursor = con.cursor()

# Creación de tabla si no existe
cursor.execute("""IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Contactos' and TYPE='U')
    CREATE TABLE Contactos (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre VARCHAR(250),
        apodo VARCHAR(100),
        numero VARCHAR(10),
        cumpleanhos VARCHAR(5)
    )""")

con.commit()

con.close()
