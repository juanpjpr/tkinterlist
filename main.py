from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------FIUNCOIENS------------------------
null_variable = None


def conexionBBDD():
	miCon=sqlite3.connect("Usuarios")
	miCur=miCon.cursor()

	try:
		miCur.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASS VARCHAR(50))
			''')
		messagebox.showinfo("BBDD","BBDD creada con exito")
	except:
		messagebox.showwarning("Warning","BBDD ya existente")


def limpiarCampos():
	miNombre.set("")
	miId.set("")
	miPass.set("")

def crear():
	limpiarCampos()
	miCon=sqlite3.connect("Usuarios")
	miCursor=miCon.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+miNombre.get()+"','"+miPass.get()+"')")
	miCon.commit()

	messagebox.showinfo("BBDD","Insertado con exito")

def leer():
	limpiarCampos()
	miCon=sqlite3.connect("Usuarios")
	miCursor=miCon.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+ miId.get())
	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])

	miCon.commit()

def actualizar():
	miCon=sqlite3.connect("Usuarios")
	miCursor=miCon.cursor()

	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='" + miNombre.get() + "', PASS='"+miPass.get()+"'WHERE ID="+miId.get())
	miCon.commit()

	messagebox.showinfo("BBDD","Actualizado con exito")

def delete():
	limpiarCampos()
	miCon=sqlite3.connect("Usuarios")
	miCursor=miCon.cursor()
	sel = listUsuario.curselection()
	if  miId.get() is None:
		miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ miId.get())
	else:
		miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ str(sel[0]))
	miCon.commit()

	messagebox.showinfo("BBDD","Eliminado")


def agregarList():
	listUsuario.delete(0, END)
	miCon=sqlite3.connect("Usuarios")
	miCursor=miCon.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS")
	elUsuario=miCursor.fetchall()
	
	for us in elUsuario:
		listUsuario.insert("end",us)
		

root=Tk()
root.title("Kiosko v 1.0")
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,  height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=delete)

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)


#------------------------------------------------------

crearFrame=Frame(root)
crearFrame.pack()

miusuario=StringVar()
miId=StringVar()
miNombre=StringVar()
miPass=StringVar()


cuadroId=Entry(crearFrame,textvariable=miId)
cuadroId.grid(row=0,column=1,padx=5,pady=5)

cuadroNombre=Entry(crearFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=5,pady=5)

cuadroPass=Entry(crearFrame,show="*",textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=5,pady=5)

#---------------LABELS-------------------------------

idLabel=Label(crearFrame,text="Id:")
idLabel.grid(row=0,column=0, padx=5,pady=5)

idNombre=Label(crearFrame,text="Nombre:")
idNombre.grid(row=1,column=0, padx=5,pady=5)

idPass=Label(crearFrame,text="Pass:")
idPass.grid(row=2,column=0, padx=5,pady=5)

#-------------------------list-----------------------

listaFrame=Frame(root)
listaFrame.pack()
listUsuario=Listbox(listaFrame)
listUsuario.grid(row=0,column=0,padx=5,pady=5)


#---------------------------Botones----------------------

botonesFrame=Frame(root)
botonesFrame.pack()

botonCrear=Button(botonesFrame,text="Crear",command=crear)
botonCrear.grid(row=1,column=0, padx=5, pady=5)

botonBuscar=Button(botonesFrame,text="Buscar",command=leer)
botonBuscar.grid(row=1,column=1, padx=5, pady=5)

botonActualizar=Button(botonesFrame,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=2, padx=5, pady=5)

botonBorrar=Button(botonesFrame,text="Borrar",command=delete)
botonBorrar.grid(row=1,column=3, padx=5, pady=5)

botonLista=Button(botonesFrame,text="Usuarios",command=agregarList)
botonLista.grid(row=1,column=4, padx=5, pady=5)


root.mainloop()