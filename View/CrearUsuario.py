import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearUsuario():

    def salir(self, event):
        self.ventana.destroy()

    def mostrarAyuda(self, event):
        mensaje = (
            "Formulario de registro de usuarios:\n\n"
            "- Complete todos los campos obligatorios marcados con *.\n"
            "- Pulse 'Registrar' para guardar los datos.\n"
            "- Pulse 'Limpiar' para borrar los campos.\n"
            "- Pulse 'Salir' para cerrar esta ventana.")
        messagebox.showinfo("Ayuda", mensaje)


    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro de Usuarios")
        self.ventana.configure(width=320, height=350)
        self.ventana.resizable(0,0)

        #Iconos
        self.iconoRegistrar = tk.PhotoImage(file=r"Restaurante/Src/registrar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Registrarse", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor="center")

        #Textos
        self.lblNombres = tk.Label(self.ventana, text="Nombres*:")
        self.lblNombres.place(relx=0.36, rely=0.2, anchor="center")

        self.lblCedula = tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(relx=0.34, rely=0.34, anchor="center")

        self.lblEmail = tk.Label(self.ventana, text="Email*:")
        self.lblEmail.place(relx=0.32, rely=0.48, anchor="center")

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(relx=0.35, rely=0.62, anchor="center")

        #Campos de textos
        self.txtNombres = tk.Entry(self.ventana)
        self.txtNombres.place(relx=0.50, rely=0.26, anchor="center")

        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.50, rely=0.4, anchor="center")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.50, rely=0.54, anchor="center")

        self.txtPassword = tk.Entry(self.ventana)
        self.txtPassword.place(relx=0.50, rely=0.68, anchor="center")

        #Botones
        self.btnRegistart = tk.Button(self.ventana, image=self.iconoRegistrar, text="Registrar", width=85, compound="left")
        self.btnRegistart.place(relx=0.34, rely=0.83, anchor="center")
        Tooltip(self.btnRegistart, "Registrar un nuevo usuario")

        self.btnLimpiar = tk.Button(self.ventana, image=self.iconoLimpiar, text="Limpiar", width=85, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.83, anchor="center")
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.92, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de registro")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()