from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Logica import *
import sqlite3

Miconexion = sqlite3.connect("ProyectoU2")
micursor = Miconexion.cursor()

raiz = Tk()
barramenu= Menu(raiz)
raiz.title("Universidad")
raiz.resizable(False, False)
raiz.config(width=400, height=400, menu=barramenu)

frame= Frame(raiz, width=400, height=400,background="white")
frame.pack()

opcion=IntVar()
Nombre= StringVar()
Contraseña = StringVar()


Eleccion= Radiobutton(frame,text="Estudiante",variable=opcion,value=1,background="white").place(x=80,y=25)
Eleccion= Radiobutton(frame,text="Profesor",variable=opcion,value=2,background="white").place(x=225,y=25)

Nombre_Label = Label(frame,text="Nombre: ",background="white").place(x=80,y=100)
Nombre_Entry = Entry(frame,width=30,textvariable=Nombre).place(x=150,y=100)

Contraseña_Label = Label(frame,text="Contraseña: ",background="white").place(x=80,y=140)
Contraseña_Entry = Entry(frame,width=30,show="*",textvariable=Contraseña).place(x=150,y=140)

Ingresar = Button(frame, text="Ingresar", bg="white", fg="black", width=10, height=1, command=lambda:validacion()).place(x=150,y=190)

Registrarse = Label(frame,text="Registrate: ",background="white").place(x=40,y=350)
Registrarse_Button = Button(frame, text="Registrarse", bg="white", fg="black", height=1).place(x=120,y=350)


archivomenu=Menu(barramenu,tearoff=0)
archivomenu.add_command(label="Nuevo",background="white")
archivomenu.add_command(label="Guardar",background="white")
archivomenu.add_separator()
archivomenu.add_command(label="Salir",background="white")

acercade= Menu(barramenu, tearoff=0)
acercade.add_command(label="Acerca de",background="white")
acercade.add_command(label="Version", background="white")

barramenu.add_cascade(label="Archivo",menu=archivomenu)
barramenu.add_cascade(label="Info",menu=acercade)

def validacion():
    Usuario1=Usuario(str(Nombre.get()),Contraseña.get())
    Usuario1.extraer_informacion()
    Usuario1.conexion()




raiz.mainloop()