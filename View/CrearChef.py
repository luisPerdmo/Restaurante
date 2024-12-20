__author__ = "Luis Perdomo"
__copyright__ = "Copyright 2022, CAPS"
__credits__ = ["LDM", "Luis Perdomo", "Otros"]
__license__ = "GPL"
__version__ = "0.70.10000"
__maintainer__ = "Equipo LDM"
__email__ = "luis.perdomo@correounivalle.edu.co"
__status__ = "Pruebas"

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearChef():

    def mostrarAyuda(self, event):
        """ 
        Función que muestra una ventana de ayuda con los atajos de teclado.
        """
        mensaje_Ayuda = ( 
               "Atajos.\n\n"
               "- Presione 'F4' para registrar un nuevo usuario. \n"
               "- presione 'F3' para limpiar los campos. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n" 
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def limpiarCampos(self, event):
        """ 
        Función para limpiar los campos de texto del formulario de registro.
        """
        self.txtCedula.delete(0, tk.END)
        self.txtNombre.delete(0, tk.END)
        self.txtApellido.delete(0, tk.END)
        self.txtTelefono.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtCedula.config(bg="#ffffff")
        self.txtNombre.config(bg="#ffffff")
        self.txtApellido.config(bg="#ffffff")
        self.txtTelefono.config(bg="#ffffff")
        self.txtEmail.config(bg="#ffffff")

    def salir(self, event):
        """ 
        Función para limpiar los campos de texto del formulario de registro.
        """
        self.ventana.destroy()

    def guardarChef(self, event):
        """ 
        Función para limpiar los campos de texto del formulario de registro.
        """
        if not self.txtCedula.get() or not self.txtNombre.get() or not self.txtApellido.get() or not self.txtTelefono.get() or not self.txtEmail.get():
            messagebox.showerror("Error", "Por favor ingrese todos los valores en los campos obligatorios.")
            return 
        for campo, nombreCampo in [(self.txtNombre.get(), "Nombres"), (self.txtApellido.get(), "Apellido")]:
            if not campo.replace(" ", "").isalpha():
                messagebox.showerror("Error", f"El campo '{nombreCampo}' solo puede contener letras.")
                return
        if not self.txtCedula.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cédula' solo puede contener números.")
            return
        if not self.txtTelefono.get().isdigit():
            messagebox.showerror("Error", "El campo 'Teléfono' solo puede contener números.")
            return
        rol = "Chef"
        if self.Usuario.existeUsuario(self.txtCedula.get()):  
            messagebox.showerror("Error", f"La cédula '{self.txtCedula.get()}' ya está registrada.")
            return
        self.Usuario.crearChef(self.txtNombre.get(), self.txtApellido.get(), self.txtEmail.get(), self.txtTelefono.get(), self.txtCedula.get(), rol)
        messagebox.showinfo("Confirmación", "Nuevo Chef registrado con éxito.")
    
    def soloNumeros(self, event):
        """ 
        Función que permite solo la entrada de números en los campos de cédula y teléfono.
        """
        numeros = event.keysym
        if numeros.isalpha(): 
            if event.widget == self.txtCedula:
                self.txtCedula.config(bg="#F8D7DA", fg="#000000")
            elif event.widget == self.txtTelefono:
                self.txtTelefono.config(bg="#F8D7DA", fg="#000000")
        else:
            if event.widget == self.txtCedula:
                self.txtCedula.config(bg="#ffffff", fg="#000000")
            elif event.widget == self.txtTelefono:
                self.txtTelefono.config(bg="#ffffff", fg="#000000")
        
    def soloLetras(self, event):
        """ 
        Función que permite solo la entrada de letras en los campos de nombre y apellido.
        """
        letras = event.keysym
        if event.widget == self.txtNombre:
            if letras.isdigit() or letras == "BackSpace":
                self.txtNombre.config(bg="#F8D7DA", fg="#000000")
            else:
                self.txtNombre.config(bg="#ffffff", fg="#000000")
        elif event.widget == self.txtApellido:
            if letras.isdigit() or letras == "BackSpace":
                self.txtApellido.config(bg="#F8D7DA", fg="#000000")
            else:
                self.txtApellido.config(bg="#ffffff", fg="#000000")
        

    def __init__(self, Usuario):
        """ 
        Constructor que inicializa la ventana de registro del chef y sus componentes.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestion de Registador")
        self.ventana.configure(width=320, height=390)
        self.ventana.resizable(0,0)

        self.Usuario = Usuario

        #Iconos
        self.iconoRegistrar = tk.PhotoImage(file=r"Restaurante/Src/registrar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Registrar Chef", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        #Textos
        self.lblCedula = tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(relx=0.32, rely=0.19, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*:")
        self.lblNombre.place(relx=0.33, rely=0.31, anchor="center")

        self.lblApellido = tk.Label(self.ventana, text="Apellido*:")
        self.lblApellido.place(relx=0.33, rely=0.44, anchor="center")

        self.lblTelefono = tk.Label(self.ventana, text="Telefono*:")
        self.lblTelefono.place(relx=0.33, rely=0.57, anchor="center")

        self.lblEmail = tk.Label(self.ventana, text="Email*:")
        self.lblEmail.place(relx=0.30, rely=0.70, anchor="center")

        #Campos de textos
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.50, rely=0.24, anchor="center")
        self.txtCedula.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCedula, "Ingrese su cédula. Solo se permiten números.")

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.50, rely=0.37, anchor="center")
        self.txtNombre.bind("<KeyPress>", self.soloLetras)
        Tooltip(self.txtNombre, "Ingrese su nombre. Solo se permiten letras.")

        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.place(relx=0.50, rely=0.50, anchor="center")
        self.txtApellido.bind("<KeyPress>", self.soloLetras)
        Tooltip(self.txtApellido, "Ingrese su apellido. Solo se permiten letras.")

        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.50, rely=0.63, anchor="center")
        self.txtTelefono.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtTelefono, "Ingrese su número de teléfono. Solo se permiten números.")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.50, rely=0.76, anchor="center")
        Tooltip(self.txtEmail, "Ingrese un correo electrónico válido en formato usuario@dominio.com.")

        #Botones
        self.btnRegistrar = tk.Button(self.ventana, image=self.iconoRegistrar, text="Registrar", width=85, compound="left")
        self.btnRegistrar.place(relx=0.34, rely=0.87, anchor="center")
        self.btnRegistrar.bind("<Button-1>", self.guardarChef)
        Tooltip(self.btnRegistrar, "Registrar un nuevo usuario")

        self.btnLimpiar = tk.Button(self.ventana, image=self.iconoLimpiar, text="Limpiar", width=85, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.87, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.93, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de registro")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        # Atajo
        self.ventana.bind("<F4>", self.guardarChef)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()