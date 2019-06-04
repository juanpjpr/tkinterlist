from tkinter import *


def agregar():
	listaProd.insert(END,entryAgregar.get())
	entryAgregar.delete(0,END)
def borrar():
	listaProd.delete(listaProd.curselection())

root=Tk()
root.title("Kiosko")
main=Frame(root)
main.pack()

def conexionBBDD():
	miCon=sqlite3.connect("Productos")
	miCur=miCon.cursor()

	try:
		miCur.execute('''
			CREATE TABLE DATOSPRODUCTOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOM VARCHAR(50),
			PU INTEGER)
			''')
		messagebox.showinfo("BBDD","BBDD creada con exito")
	except:
		messagebox.showwarning("Warning","BBDD ya existente")

def crear():
	miCon=sqlite3.connect("Productos")
	miCursor=miCon.cursor()

	miCursor.execute("INSERT INTO DATOSPRODUCTOS VALUES(NULL, '"+miNombre.get()+"','"+miPass.get()+"')")
	miCon.commit()

	messagebox.showinfo("BBDD","Insertado con exito")



listaProd=Listbox(main,width=50)
listaProd.pack()

miEntry=StringVar()

entryAgregar=Entry(main)
entryAgregar.pack()

botonFrame=Frame(main)
botonFrame.pack()

botonAgregar=Button(botonFrame,text="Agregar",command=agregar,width=10)
botonAgregar.pack()

botonConsultar=Button(botonFrame,text="Consultar",width=10)
botonConsultar.pack()



botonBorrar=Button(botonFrame,text="Borrar",command=borrar,width=10)
botonBorrar.pack()


botonFinalizar=Button(botonFrame,text="Finalizar",width=10)
botonFinalizar.pack()


root.mainloop()