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

# Procedimiento sin parametros
# print("# Lista de Contactos")
# cursor.execute("{ CALL SP_ContactosLista }")

# result = cursor.fetchall()
# for contacto in result:
# print(contacto)


# # Procedimiento con parametros
# params = ("wilycolon")
# cursor.execute("{ CALL SP_ContactosBuscaXApodo ( ? ) }", params)

# result = cursor.fetchall()
# while result:
#     print(result)
#     if cursor.nextset():
#         result = cursor.fetchall()
#     else:
#         result = None


# Procedimiento con parametro de salida
params = (
    "Veronica Smith",
    "Vero",
    "#147852369",
    "12/05"
)

sql = """\
DECLARE @id int;
exec SP_ContactosInsertar @id OUTPUT, ?, ?, ?, ?;
SELECT @id;
"""

cursor.execute(sql, params)

returnId = cursor.fetchval()

print("Se insertó el registro ID: {}". format(returnId))


con.commit()

con.close()
