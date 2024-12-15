import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarCliente():

    def mostrarAyuda(self, event):
        mensaje_Ayuda = (
            "Ayuda", 
            "Atajos.\n\n"
            "- Presione 'F4' para buscar el cliente para eliminar. \n"
            "- presione 'F3' para eliminar el cliente seleccionado. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

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

    def buscarCliente(self, event):
        if not self.txtCedula.get():
            messagebox.showerror("Error", "Por favor ingrese la cédula.")
            return
        if not self.txtCedula.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cédula' solo puede contener números.")
            return
        cedula = int(self.txtCedula.get())
        try:
            cliente = self.obtenerCliente(cedula)
            if cliente:
                self.txtNombre.config(state="normal")
                self.txtApellido.config(state="normal")
                self.txtTelefono.config(state="normal")
                self.txtEmail.config(state="normal")
                self.txtNombre.delete(0, tk.END)
                self.txtNombre.insert(0, cliente[1])  # Nombre
                self.txtApellido.delete(0, tk.END)
                self.txtApellido.insert(0, cliente[2])  # Apellido
                self.txtTelefono.delete(0, tk.END)
                self.txtTelefono.insert(0, cliente[3])  # Teléfono
                self.txtEmail.delete(0, tk.END)
                self.txtEmail.insert(0, cliente[4])  # Email
                self.txtNombre.config(state="disabled")
                self.txtApellido.config(state="disabled")
                self.txtTelefono.config(state="disabled")
                self.txtEmail.config(state="disabled") 
                messagebox.showinfo("Información", f"Cliente con cédula {cedula} encontrado.")
                self.btnEliminar.config(state="normal")
            else:
                messagebox.showinfo("Información", f"Cliente con cédula {cedula} no encontrado.")
                self.btnEliminar.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el cliente. Detalles: {e}")

    def obtenerCliente(self, cedula):
        return self.Usuario.buscarCliente(cedula)

    def eliminarCliente(self, event):
        if not self.txtCedula.get():
            messagebox.showerror("Error", "Por favor ingrese la cédula.")
            return
        if not self.txtCedula.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cédula' solo puede contener números.")
            return
        cedula = int(self.txtCedula.get())
        cliente = self.obtenerCliente(cedula)
        if not cliente:
            messagebox.showinfo("Información", f"Cédula {cedula} no encontrada.")
            return
        try:
            self.Usuario.eliminarCliente(cedula)
            messagebox.showinfo("Confirmación", f"Cédula {cedula} eliminada con éxito.")
            self.limpiarCampos(event)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el cliente. Detalles: {e}")

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
        Tooltip(self.txtNombre, "Nombre del cliente.")

        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.place(relx=0.50, rely=0.50, anchor="center")
        self.txtApellido.config(state="disabled")
        Tooltip(self.txtApellido, "Apellido del cliente.")

        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.50, rely=0.63, anchor="center")
        self.txtTelefono.config(state="disabled")
        Tooltip(self.txtTelefono, "Teléfono del cliente.")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.50, rely=0.76, anchor="center")
        self.txtEmail.config(state="disabled")
        Tooltip(self.txtEmail, "Email del cliente.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.87, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarCliente)
        Tooltip(self.btnBuscar, "Buscar un cliente para eliminar")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar, text="Eliminar", width=85, compound="left")
        self.btnEliminar.place(relx=0.65, rely=0.87, anchor="center")
        self.btnEliminar.bind("<Button-1>", self.eliminarCliente)
        Tooltip(self.btnEliminar, "Eliminar al cliente seleccionado")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.93, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de gestión")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        # Atajo
        self.ventana.bind("<F4>", self.buscarCliente)
        self.ventana.bind("<F3>", self.eliminarCliente)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
