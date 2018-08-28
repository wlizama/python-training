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

DELIMITADOR = "*" * 50

# Creación de tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos(
id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(250),
apodo VARCHAR(100),
numero VARCHAR(10),
cumpleanhos VARCHAR(5),
PRIMARY KEY (id)
)""")


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
#     %s, %s, %s, %s
#     )""", contactos)


# # Update
# cursor.execute("""UPDATE contactos SET
#     apodo = 'Ferni',
#     cumpleanhos = '20/06'
#     WHERE id = 6
#     """)

# Delete
# cursor.execute("DELETE from contactos WHERE id > 6")

# Simple Select
print(DELIMITADOR)
print(" DESPUÉS de operaciones")
print(DELIMITADOR)
cursor.execute("SELECT * FROM Contactos")
result = cursor.fetchall()

for contacto in result:
    print(contacto)

micon.commit()

micon.close()
