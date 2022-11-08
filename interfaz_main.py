from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

micursor = sqlite3.connect("ProyectoU2")
micursor = micursor.cursor()

#micursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), CONTRASEÑA INTEGER, CORREO VARCHAR(15), EDAD INTEGER )")

class Usuario():
    def __init__(self,nombre,contraseña):
        self.nombre= nombre
        self.contraseña= contraseña
        self.conectado= False
        self.intentos=3

    def conectado(self,contraseña):
        print("ingresa la contraseña para acceder al sitio web")
        if self.contraseña==contraseña:
            print("acceso concedido")
            self.conectado==True 
        else:
            print("acceso denegado")
            print("te qudan {} intentos".format(self.intentos-1))

    
    def desconectar(self):
        self.conectado= False
        print("tu secion ha terminado con exito, dale reintentar para volver a ingresar ")


class registro():
    def __init__(self,nombre,contraseña,correo,edad) :
        self.nombre= nombre
        self.contraseña= contraseña
        self.correo= correo
        self.edad = edad
    
    def registro(self):
        micursor.execute("INSERT INTO USUARIOS VALUES(NULL,{},{},{},{})".format(self.nombre,self.contraseña,self.correo,self.edad))



