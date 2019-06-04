import sqlite3

miConexion=sqlite3.connect("BaseDeDatos")

miCursor=miConexion.cursor()


miCursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50) UNIQUE,PU INTEGER)")

def imprimirLista():
	miCursor.execute("SELECT * FROM PRODUCTOS")

	variosProductos=miCursor.fetchall()

	print (variosProductos)

imprimirLista()

miConexion.close()