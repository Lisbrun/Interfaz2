from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class hola():
    def __init__(self) -> None:      
        self.Registro  = Tk()
        self.Registro .title("Registro")
        self.Registro .resizable(False,False)
        self.Registro .config(width=400, height=400)
        self.Registro_Frame= Frame(self.Registro , width=400, height=400,background="white")
        self.Registro_Frame.pack()

        self.grafica()
        self.Registro_Frame.mainloop()

    def grafica(self):
        Nombre_Label = Label(self.Registro_Frame,text="Nombre: ",background="white").place(x=30,y=50)
        Nombre_Entry = Entry(self.Registro_Frame,width=30).place(x=110,y=50)

        Apellid_Label = Label(self.Registro_Frame,text="Apellido: ",background="white").place(x=30,y=90)
        Apellid_Entry = Entry(self.Registro_Frame,width=30).place(x=110,y=90)

        Correo_Label = Label (self.Registro_Frame, text="Correo: ",background="white").place(x=30,y=130)
        Correo_Entry = Entry(self.Registro_Frame,width=30).place(x=110,y=130)

        Edad_Label = Label(self.Registro_Frame,text="Edad: ",background="white").place(x=30,y=170)
        Edad_Entry = Entry(self.Registro_Frame,width=30).place(x=110,y=170)

        Label_Carrera= Label ( self.Registro_Frame,text="Carrera: ",background="white").place(x=30,y=210)
        Carrera = ttk.Combobox(self.Registro_Frame, state="readonly", values=["Ingenieria", "Medicina", "Ciencias Basicas", "Ciencias Humanas"]).place(x=110,y=210)

        Label_contraseña=Label(self.Registro_Frame,text="Contraseña: ",background="white").place(x=30,y=250)
        Contraseña_Entry = Entry(self.Registro_Frame,width=30,show="*").place(x=110,y=250)

        Volver= Button(self.Registro_Frame, text="Back", background="white",height=1, width=8,command=lambda:self.volver()).place(x=30,y=350)
        Guardar = Button(self.Registro_Frame, text="Guardar", background="white",height=1, width=8).place(x=300,y=350)
        self.Registro_Frame .mainloop()

    def volver(self):
        self.Registro.destroy()
        pass
