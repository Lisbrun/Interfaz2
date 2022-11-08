
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

Miconexion = sqlite3.connect("ProyectoPersonal")
micursor= Miconexion.cursor()
raiz = Tk()
raiz.title("Base de datos")
raiz.iconbitmap("bloc.ico")
barramenu = Menu(raiz)
raiz.config(height=270, width=270, menu=barramenu)
Dibujo = Frame(raiz)
Dibujo.config(bg="white")
Dibujo.pack()
minota= StringVar()
miStringid= StringVar()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

Miid= Label(Dibujo,text="ID:", background="white")
Miid.grid(row=1,column=1)

mimateria = Label(
Dibujo, width=40, text="Selecciona la materia a implementar la nota", padx=4, pady=9, bg="white")
mimateria.config(justify="left")
mimateria.grid(row=2, column=1)

miNota = Label(Dibujo, width=40, text="Tipo de Nota:",background="white", justify="left", pady=9)
miNota.grid(row=3, column=1)

minum= Label(Dibujo,width=40,text="Ponga la nota ",background="white",justify="left")
minum.grid(row=4,column=1)

Observacion = Label(Dibujo, width=40, text="Observacion:",background="white", justify="left")
Observacion.grid(row=5, column=1)

Miobservacion = Text(Dibujo, width=15, height=8, pady=15, padx=10)
Miobservacion.grid(row=5, column=2)

Materias = ttk.Combobox(Dibujo, state="readonly", values=["Calculo", "Algebra", "Mecanica", "Programacion"])
Materias.grid(row=2, column=2)

Notas = ttk.Combobox(Dibujo, state="readonly", values=["Parciales", "Talleres", "Quices", "Informes"])
Notas.grid(row=3, column=2)


Entrynota= Entry(Dibujo,width=23,textvariable=minota)
Entrynota.grid(row=4,column=2)

Entryid= Entry ( Dibujo, width=23,textvariable=miStringid)
Entryid.grid(row=1,column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#micursor.execute("CREATE TABLE NOTAS(ID INTEGER PRIMARY KEY AUTOINCREMENT ,Materia VarChar (15), Tipo_Nota Varchar (20), Nota Float(3), Observacion Text)")

def agregar():

    global minota
    global Materias
    global Notas
    global Miobservacion
    
    Materia=Materias.get()
    Tipo_nota=Notas.get()
    Nota=minota.get()
    Observaciones= Miobservacion.get("1.0",END)
    minota.set("")
    Miobservacion.delete("1.0",END)
    micursor.execute("INSERT INTO NOTAS VALUES(NULL,'"+Materia+"','"+Tipo_nota+"','"+Nota+"','"+Observaciones+"')")
    Miconexion.commit()
    
    print(Materia,Tipo_nota,Nota,Observaciones)


def mostrarinfo():
    micursor.execute("SELECT * FROM NOTAS WHERE ID="+miStringid.get())
    informacion= micursor.fetchall()
    for datos in informacion:
        miStringid.set(datos[0])
        Materias.set(datos[1])
        Notas.set(datos[2])
        minota.set(datos[3])
        Miobservacion.insert("1.0", datos[4])

def actualizacion():
    datos = miStringid.get(),Materias.get(),Notas.get(),minota.get(),Miobservacion.get("1.0",END)
    micursor.execute("UPDATE NOTAS SET ID=?,Materia=?,Tipo_Nota=?,Nota=?,Observacion=?"+"WHERE ID="+ miStringid.get(),(datos))
    Miconexion.commit()
    pass

def eliminar():
    micursor.execute("DELETE FROM NOTAS WHERE ID="+miStringid.get())
    Miconexion.commit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

Boton = Button(Dibujo, text="Add",command=lambda:agregar(),background="white")
Boton.grid(row=6, column=1, pady=10)

mirarinfo =Button(Dibujo,text="Info",pady=4,command=lambda:mostrarinfo(),background="white")
mirarinfo.grid(row=6,column=2, pady=10 )

actualizarinfo = Button(Dibujo,text="Update",command=lambda:actualizacion(), background="white")
actualizarinfo.place(x=240,y=290)

eliminarinfo = Button(Dibujo,text="Delete",command=lambda:eliminar(), background="white")
eliminarinfo.place(x=50,y=290)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def salir():
    raiz.destroy()

archivomenu = Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Nuevo")
archivomenu.add_command(label="Guardar")
archivomenu.add_separator()
archivomenu.add_command(label="Salir",command=salir)

Editar = Menu(barramenu, tearoff=0)
Editar.add_cascade(label="copiar")
Editar.add_cascade(label="cortar")
Editar.add_cascade(label="pegar")
Editar.add_separator()
Editar.add_cascade(label="buscar")

def show():
    messagebox.showinfo("Programa de Notas","Creado por Lis :D")    
Acerca= Menu(barramenu,tearoff=0)
Acerca.add_command(label="Acerca de:",command=show)

barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Editar", menu=Editar)
barramenu.add_cascade(label="acerca de:",menu=Acerca)




raiz.mainloop()

Miconexion.commit()
Miconexion.close()