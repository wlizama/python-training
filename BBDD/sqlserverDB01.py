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

DELIMITADOR = "*" * 50

print(DELIMITADOR)
print(" ANTES de operaciones")
print(DELIMITADOR)
cursor.execute("SELECT * FROM Contactos")
misContactos_orig = cursor.fetchall()

for contacto in misContactos_orig:
    print(contacto)


# # Inserción multiple
# contactos = [
#     ('Pedro Mendoza', 'Pancho Fierro', '123654789', '05/08'),
#     ('Mary Lopez', 'Marimar', '#987456321', '03/11'),
#     ('Enrique Altarez', 'Quique', '#989654123', '01/02'),
#     ('Sebastian Estrada', 'Sebas', '896471235', '08/10'),
#     ('Aurora Duque', 'Auro', '9584123684', '10/04'),
#     ('Fernado Peralta', 'Ferd', '9236541879', '25/06')
# ]

# cursor.executemany("""INSERT INTO Contactos (nombre, apodo, numero, cumpleanhos) VALUES (
#     ?,?,?,?
#     )""", contactos)

# # Update
# cursor.execute("""UPDATE Contactos SET
#     Apodo = 'Ferni',
#     Cumpleanhos = '20/06'
#     WHERE ID = 6
#     """)

# Delete
cursor.execute("DELETE from Contactos WHERE ID = 6")

# Simple Select
print(DELIMITADOR)
print(" DESPUÉS de operaciones")
print(DELIMITADOR)
cursor.execute("SELECT * FROM Contactos")
misContactos_mod = cursor.fetchall()

for contacto in misContactos_mod:
    print(contacto)

con.commit()

con.close()
