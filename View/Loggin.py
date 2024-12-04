import tkinter as tk
from tkinter import *

class Loggin():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesion")
        self.ventana.configure(width=340, height=350)
        self.ventana.resizable(0,0)

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Inicio de Sesion")
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor="center")

        #Textos
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(relx=0.34, rely=0.3, anchor="center")

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(relx=0.35, rely=0.45, anchor="center")

        #Campo de Texto
        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(relx=0.50, rely=0.36, anchor="center")

        self.txtPassword = tk.Entry(self.ventana)
        self.txtPassword.place(relx=0.50, rely=0.51, anchor="center")

        #Botones
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", width=7)
        self.btnIngresar.place(relx=0.34, rely=0.7, anchor="center")

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=8)
        self.btnSalir.place(relx=0.64, rely=0.7, anchor="center")

        self.btnCrear = tk.Button(self.ventana, text="Crear Usuario", width=19)
        self.btnCrear.place(relx=0.50, rely=0.79, anchor="center")


        self.ventana.mainloop()