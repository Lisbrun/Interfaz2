from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

Miconexion = sqlite3.connect("ProyectoU2")
micursor = Miconexion.cursor()

#micursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), CONTRASEÑA INTEGER, CORREO VARCHAR(15), EDAD INTEGER )")
def validacion(nombre):
    micursor.execute("SELECT NOMBRE, CONTRASEÑA FROM USUARIOS WHERE NOMBRE = ?", (nombre,))
    print(micursor.fetchall())
class Usuario():
    def __init__(self,nombre,contraseña):
        self.nombre= nombre
        self.contraseña= int(contraseña)
        self.intentos=3
        self.ingreso= False
        

    def extraer_informacion(self):
        micursor.execute("SELECT NOMBRE,CONTRASEÑA FROM USUARIOS WHERE NOMBRE = ?", (self.nombre,))
        self.informacion = micursor.fetchall()
        for datos in self.informacion:
            self.nombre_sql=datos[0]
            self.contraseña_sql=datos[1]
            break

    def conexion(self):
        if self.nombre == self.nombre_sql and self.contraseña == self.contraseña_sql:
            print("Bienvenido")
            messagebox.showinfo("Bienvenido", "Bienvenido")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")



class registro():
    def __init__(self,nombre,contraseña,correo,edad) :
        self.nombre= nombre
        self.contraseña= contraseña
        self.correo= correo
        self.edad = edad
    
    def registro(self):
        micursor.execute("INSERT INTO USUARIOS VALUES(NULL,'{}','{}','{}','{}')".format(self.nombre,self.contraseña,self.correo,self.edad))      
        Miconexion.commit()



#usuario1= Usuario("juan",1212)
#usuario1.extraer_informacion()
#usuario1.conexion()


