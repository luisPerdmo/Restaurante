import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarCliente():

    def mostrarAyuda(self, event):
        ayuda = """
        Formulario de Eliminación de Cliente:
        - Cédula: Ingrese la cédula del cliente que desea eliminar. Solo se permiten números.
        - Nombre, Apellido, Teléfono y Email: Estos campos se llenarán automáticamente después de buscar al cliente con la cédula.
        - Buscar: Presione para buscar el cliente con la cédula ingresada.
        - Eliminar: Presione para eliminar al cliente seleccionado.

        Recuerde que los campos Nombre, Apellido, Teléfono y Email estarán deshabilitados hasta que se realice la búsqueda.
        """
        messagebox.showinfo("Ayuda - Eliminar Cliente", ayuda)

    def limpiarCampos(self, event):
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
        self.ventana.destroy()

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha(): 
            if event.widget == self.txtCedula:
                self.txtCedula.config(bg="#F8D7DA", fg="#000000")
        else:
            if event.widget == self.txtCedula:
                self.txtCedula.config(bg="#ffffff", fg="#000000")

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Cliente")
        self.ventana.configure(width=320, height=390)
        self.ventana.resizable(0,0)

        self.Usuario = Usuario

        # Iconos
        self.iconoEliminar = tk.PhotoImage(file=r"Restaurante/Src/eliminarMesa.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Cliente", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        # Textos
        self.lblCedula = tk.Label(self.ventana, text="Cédula*: ")
        self.lblCedula.place(relx=0.32, rely=0.19, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*: ")
        self.lblNombre.place(relx=0.33, rely=0.31, anchor="center")

        self.lblApellido = tk.Label(self.ventana, text="Apellido*: ")
        self.lblApellido.place(relx=0.33, rely=0.44, anchor="center")

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*: ")
        self.lblTelefono.place(relx=0.33, rely=0.57, anchor="center")

        self.lblEmail = tk.Label(self.ventana, text="Email*: ")
        self.lblEmail.place(relx=0.30, rely=0.70, anchor="center")

        # Campos de texto
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.50, rely=0.24, anchor="center")
        self.txtCedula.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCedula, "Ingrese su cédula. Solo se permiten números.")

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.50, rely=0.37, anchor="center")
        self.txtNombre.config(state="disabled")
        Tooltip(self.txtNombre, "Ingrese su nombre. Solo se permiten letras.")

        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.place(relx=0.50, rely=0.50, anchor="center")
        self.txtApellido.config(state="disabled")
        Tooltip(self.txtApellido, "Ingrese su apellido. Solo se permiten letras.")

        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.50, rely=0.63, anchor="center")
        self.txtTelefono.config(state="disabled")
        Tooltip(self.txtTelefono, "Ingrese su número de teléfono. Solo se permiten números.")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.50, rely=0.76, anchor="center")
        self.txtEmail.config(state="disabled")
        Tooltip(self.txtEmail, "Ingrese un correo electrónico válido en formato usuario@dominio.com.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.87, anchor="center")
        #self.btnBuscar.bind("<Button-1>", self.buscarMesero)
        Tooltip(self.btnBuscar, "Buscar un cliente para eliminar")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar, text="Eliminar", width=85, compound="left")
        self.btnEliminar.place(relx=0.65, rely=0.87, anchor="center")
        #self.btnEliminar.bind("<Button-1>", self.eliminarMesero)
        Tooltip(self.btnEliminar, "Eliminar al cliente seleccionado")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.93, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de gestión")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()
