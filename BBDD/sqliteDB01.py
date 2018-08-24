import sqlite3

micon = sqlite3.connect("DB01.db")
cursor = micon.cursor()

# Creación de tabla si no existe
cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos(
Nombre VARCHAR(250),
Apodo VARCHAR(100),
Numero VARCHAR(10),
Cumpleanhos VARCHAR(10)
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
    ('Pedro Mensoza', 'Pancho Fierro', '123654789', '05/08'),
    ('Mary Lopez', 'Marimar', '#987456321', '03/11'),
    ('Enrique Atarez', 'Quique', '#989654123', '01/02'),
    ('Sebastian Estrada', 'Sebas', '896471235', '08/10'),
    ('Aurora Duque', 'Auro', '9584123684', '10/04'),
    ('Fernado Peralta', 'Ferd', '9236541879', '25/06')
]

cursor.executemany("""INSERT INTO Contactos VALUES (
?,?,?,?
)""", contactos)

micon.commit()

micon.close()
