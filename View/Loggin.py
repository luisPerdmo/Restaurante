import tkinter as tk
from tkinter import *
from Tooltip import Tooltip
from Controller.Usuario import Usuario
from View.CrearRegistrador import CrearRegistrador
from tkinter import messagebox

class Loggin():

    def mostrarAyuda(self, event):
        mensaje_Ayuda = (
            "Atajos.\n\n"
            "- Presione 'F4' para ingresar. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
            "- Presione 'F3' para crear el registrador. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def crearRegistrador(self, event):
        CrearRegistrador(Usuario())

    def ingresar(self, event):
        miRegistrador = Usuario()
        miRegistrador.iniciarSesion(self.txtUsuario.get(), self.txtPassword.get(), self.ventana)


    def validarUsuario(self, event):
        caracter = event.keysym
        if(caracter.isalpha() or caracter == '.' or caracter == "BackSpace"):
            self.txtUsuario.config(bg="#ffffff", fg="#000000")
        else:
            self.txtUsuario.config(bg="#FF5252", fg="#000000")

    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.btnVer.config(image=self.iconoVer)
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(image=self.icononoVer)
            self.bandera = True

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesion")
        self.ventana.configure(width=320, height=300)
        self.ventana.resizable(0,0)

        self.bandera = False
        self.caracteresUsusario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.']
        self.caracteresPassword = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        #Iconos
        self.iconoVer = tk.PhotoImage(file=r"Restaurante/Src/ver.png")
        self.icononoVer = tk.PhotoImage(file=r"Restaurante/Src/noVer.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante\Src\ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Inicio de Sesion", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.14, anchor="center")

        #Textos
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(relx=0.34, rely=0.3, anchor="center")

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(relx=0.35, rely=0.47, anchor="center")

        #Campo de Texto
        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(relx=0.50, rely=0.38, anchor="center")
        self.txtUsuario.bind("<Key>", self.validarUsuario)
        Tooltip(self.txtUsuario, text="Ingrese su nombre de usuario. Debe tener entre 5 y 25 caracteres.")

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(relx=0.50, rely=0.55, anchor="center")
        Tooltip(self.txtPassword, text="Ingrese su contraseña. Debe tener entre 5 y 25 caracteres.")

        #Botones
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", width=6)
        self.btnIngresar.place(relx=0.34, rely=0.7, anchor="center")
        Tooltip(self.btnIngresar, text="Haga clic para iniciar sesión.")
        self.btnIngresar.bind("<Button-1>" , self.ingresar)

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=8)
        self.btnSalir.place(relx=0.64, rely=0.7, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, text="Haga clic para salir del programa.")

        self.btnCrear = tk.Button(self.ventana, text="Crear Registrador", width=18)
        self.btnCrear.place(relx=0.50, rely=0.8, anchor="center")
        Tooltip(self.btnCrear, text="Haga clic para crear un nuevo usuario.")
        self.btnCrear.bind("<Button-1>" , self.crearRegistrador)

        self.btnVer = tk.Label(self.ventana, image=self.iconoVer)
        self.btnVer.place(relx=0.85, rely=0.55, anchor="center")
        Tooltip(self.btnVer, text="Pase el cursor para mostrar u ocultar la contraseña.")
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        self.btnAyuda = tk.Label(self.ventana, text="Ayuda", image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.95, rely=0.05, anchor="ne") 
        Tooltip(self.btnAyuda, text="Haga clic para obtener ayuda.")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)

        # Atajos
        self.ventana.bind("<F4>", self.ingresar)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F3>", self.crearRegistrador)
        self.ventana.bind("<F1>", self.mostrarAyuda)
        
        self.ventana.mainloop()