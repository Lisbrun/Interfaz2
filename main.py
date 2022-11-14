from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Logica import *
import sqlite3

Miconexion = sqlite3.connect("ProyectoU2")
micursor = Miconexion.cursor()


class principal(Frame):
    def __init__(self,master,*args) -> None:    
        super().__init__(master,*args)
        
        self.barramenu= Menu(self.master)
        self.master.configure(menu=self.barramenu)
        self.frame_principal= Frame(self.master, width=400, height=400,background="white")
        self.frame_principal.pack()


        archivomenu=Menu(self.barramenu,tearoff=0)
        archivomenu.add_command(label="Nuevo",background="white")
        archivomenu.add_command(label="Guardar",background="white")
        archivomenu.add_separator()
        archivomenu.add_command(label="Salir",background="white")

        acercade= Menu(self.barramenu, tearoff=0)
        acercade.add_command(label="Acerca de",background="white")
        acercade.add_command(label="Version", background="white")

        self.barramenu.add_cascade(label="Archivo",menu=archivomenu)
        self.barramenu.add_cascade(label="Info",menu=acercade)
        self.opcion=IntVar()
        self.Nombre= StringVar()
        self.Contraseña = StringVar()
        self.Contraseña2 = StringVar()
        self.edad= StringVar()
        self.correo = StringVar()
        self.carrera = StringVar()
        self.grafica()
        



    def grafica(self):
        
        Eleccion= Radiobutton(self.frame_principal,text="Estudiante",variable=self.opcion,value=1,background="white").place(x=80,y=25)
        Eleccion= Radiobutton(self.frame_principal,text="Profesor",variable=self.opcion,value=2,background="white").place(x=225,y=25)

        Nombre_Label = Label(self.frame_principal,text="Nombre: ",background="white").place(x=80,y=100)
        Nombre_Entry = Entry(self.frame_principal,width=30,textvariable=self.Nombre).place(x=150,y=100)

        Contraseña_Label = Label(self.frame_principal,text="Contraseña: ",background="white").place(x=80,y=140)
        Contraseña_Entry = Entry(self.frame_principal,width=30,show="*",textvariable=self.Contraseña).place(x=150,y=140)

        Ingresar = Button(self.frame_principal, text="Ingresar", bg="white", fg="black", width=10, height=1, command=lambda:self.validacion()).place(x=150,y=190)

        Registrarse = Label(self.frame_principal,text="Registrate: ",background="white").place(x=40,y=350)
        Registrarse_Button = Button(self.frame_principal, text="Registrarse", bg="white", fg="black", height=1, command=lambda:self.graficar2()).place(x=120,y=350) 


    def graficar2(self):
        self.frame_principal.destroy()
        self.frame_registro= Frame(self.master, width=400, height=400,background="white")
        self.frame_registro.pack()
        Nombre_Label = Label(self.frame_registro,text="Nombre: ",background="white").place(x=30,y=50)
        Nombre_Entry = Entry(self.frame_registro,width=30,textvariable=self.Nombre).place(x=110,y=50)


        Correo_Label = Label (self.frame_registro, text="Correo: ",background="white").place(x=30,y=90)
        Correo_Entry = Entry(self.frame_registro,width=30,textvariable=self.correo).place(x=110,y=90)

        Edad_Label = Label(self.frame_registro,text="Edad: ",background="white").place(x=30,y=140)
        Edad_Entry = Entry(self.frame_registro,width=30,textvariable=self.edad).place(x=110,y=140)

        Label_Carrera= Label ( self.frame_registro,text="Carrera: ",background="white").place(x=30,y=180)
        ttk.Combobox(self.frame_registro,textvariable=self.carrera, state="readonly", values=["Ingenieria", "Medicina", "Ciencias Basicas", "Ciencias Humanas"]).place(x=110,y=180)
        

        Label_contraseña=Label(self.frame_registro,text="Contraseña: ",background="white").place(x=30,y=220)
        Contraseña_Entry = Entry(self.frame_registro,width=30,show="*",textvariable= self.Contraseña2).place(x=110,y=220)

        Label_contraseña2=Label(self.frame_registro,text="Repetir contra: ",background="white").place(x=30,y=270)
        Contraseña_Entry2 = Entry(self.frame_registro,width=30,show="*",textvariable=self.Contraseña).place(x=110,y=270)

        Volver= Button(self.frame_registro, text="Back", background="white",height=1, width=8,command=lambda:self.volver()).place(x=30,y=350)
        Guardar = Button(self.frame_registro, text="Registro", background="white",height=1, width=8,command=lambda:self.registro()).place(x=300,y=350)

        self.frame_principal.mainloop()

    def volver(self):
        self.frame_registro.destroy()
        self.frame_principal= Frame(self.master, width=400, height=400,background="white")
        self.frame_principal.pack()
        self.grafica()
        

    
    def validacion(self):
        
        Usuario1=Usuario(str(self.Nombre.get()),self.Contraseña.get())
        Usuario1.extraer_informacion()
        Usuario1.conexion()
        print(Usuario1.Conexion)

    def registro(self):
        if self.Contraseña.get() == self.Contraseña2.get():
            if self.Contraseña.get() != "":
                try:
                    Registro1 = Registrarse(self.Nombre.get(),self.Contraseña.get(),self.edad.get(),self.correo.get(),self.carrera.get())
                
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error","El usuario ya existe")
                
            
            else:
                messagebox.showinfo("Error","Contraseña vacia")
        else:
            messagebox.showerror("Error","Las contraseñas no coinciden")
    
if __name__ == "__main__":
    raiz = Tk()
    raiz.title("Universidad")
    raiz.resizable(False, False)
    raiz.iconbitmap("verificar.ico")
    raiz.config(width=400, height=400)
    app = principal(raiz)
    app.mainloop()
        

