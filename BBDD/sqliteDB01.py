import sqlite3

micon = sqlite3.connect("DB01.db")
cursor = micon.cursor()

# Creación de tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre VARCHAR(250),
Apodo VARCHAR(100),
Numero VARCHAR(10),
Cumpleanhos VARCHAR(5)
)""")

# Inserción de valores
# cursor.execute("""INSERT INTO Contactos VALUES (
# 'Wily Colon',
# 'Whale colon',
# '123789456',
# '12/12'
# )""")


# Inserción multiple
contactos = [
    ('Pedro Mendoza', 'Pancho Fierro', '123654789', '05/08'),
    ('Mary Lopez', 'Marimar', '#987456321', '03/11'),
    ('Enrique Altarez', 'Quique', '#989654123', '01/02'),
    ('Sebastian Estrada', 'Sebas', '896471235', '08/10'),
    ('Aurora Duque', 'Auro', '9584123684', '10/04'),
    ('Fernado Peralta', 'Ferd', '9236541879', '25/06')
]

cursor.executemany("""INSERT INTO Contactos VALUES (
NULL,?,?,?,?
)""", contactos)


# Simple Select
cursor.execute("SELECT * FROM Contactos")
misContactos = cursor.fetchall()

for contacto in misContactos:
    print(contacto)

micon.commit()

micon.close()
