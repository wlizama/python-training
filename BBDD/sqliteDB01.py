import sqlite3

micon = sqlite3.connect("DB01.db")
cursor = micon.cursor()
# cursor.execute()

micon.close()
