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


DELIMITADOR = "*" * 50


print(DELIMITADOR)
print(" ANTES de operaciones")
print(DELIMITADOR)
cursor.execute("SELECT * FROM Contactos")
misContactos_orig = cursor.fetchall()

for contacto in misContactos_orig:
    print(contacto)


# # Inserción de valores
# cursor.execute("""INSERT INTO Contactos VALUES (
# 'Wily Colon',
# 'Whale colon',
# '123789456',
# '12/12'
# )""")


# # Inserción multiple
# contactos = [
#     ('Pedro Mendoza', 'Pancho Fierro', '123654789', '05/08'),
#     ('Mary Lopez', 'Marimar', '#987456321', '03/11'),
#     ('Enrique Altarez', 'Quique', '#989654123', '01/02'),
#     ('Sebastian Estrada', 'Sebas', '896471235', '08/10'),
#     ('Aurora Duque', 'Auro', '9584123684', '10/04'),
#     ('Fernado Peralta', 'Ferd', '9236541879', '25/06')
# ]

# cursor.executemany("""INSERT INTO Contactos VALUES (
# NULL,?,?,?,?
# )""", contactos)


# # Update
# cursor.execute("""UPDATE Contactos SET
# Apodo = 'Ferni',
# Cumpleanhos = '20/06'
# WHERE ID = 6
# """)


# Delete
cursor.execute("DELETE from Contactos WHERE ID = 4")


# Simple Select
print(DELIMITADOR)
print(" DESPUÉS de operaciones")
print(DELIMITADOR)
cursor.execute("SELECT * FROM Contactos")
misContactos_mod = cursor.fetchall()

for contacto in misContactos_mod:
    print(contacto)

micon.commit()

micon.close()
