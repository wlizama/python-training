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
cursor.execute("""INSERT INTO Contactos VALUES (
'Wily Colon',
'Whale colon',
'123789456',
'12/12'
)""")

micon.commit()

micon.close()
