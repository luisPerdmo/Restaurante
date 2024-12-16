_author_ = "Luis Perdomo"
_copyright_ = "Copyright 2022, CAPS"
_credits_ = ["LDM", "Luis Perdomo", "Otros"]
_license_ = "GPL"
_version_ = "0.70.10000"
_maintainer_ = "Equipo LDM"
_email_ = "luis.perdomo@correounivalle.edu.co"
_status_ = "Pruebas"

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class AgregarPlato():
    """
    Clase que maneja la interfaz gráfica y la lógica para agregar un plato en el sistema.
    """

    def mostrarAyuda(self, event):
        """
        Muestra una ventana de ayuda con los atajos de teclado disponibles.
        """
        messagebox.showinfo(
               "Ayuda", 
               "Atajos.\n\n"
               "- Presione 'F4' para guardar los datos de plato. \n"
               "- presione 'F3' para limpiar los campos. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n"
            )

    def guardarPlato(self, event):
        """
        Valida y guarda los datos del plato en el sistema.

        Se asegura de que los campos no estén vacíos, que el formato de los datos sea correcto,
        y luego registra el plato si no existe previamente en el sistema.

        Args:
            event: El evento que dispara la acción.
        """
        if not self.txtId.get() or not self.txtNombre.get() or not self.txtPrecio.get() or not self.txtCantidad.get() or not self.txtDescripcion.get("1.0", tk.END).strip():
            messagebox.showerror("Error", "Por favor ingrese todos los valores en los campos obligatorios.")
            return 
        for campo, nombreCampo in [(self.txtNombre.get(), "Nombre")]:
            if not campo.replace(" ", "").isalpha():
                messagebox.showerror("Error", f"El campo '{nombreCampo}' solo puede contener letras.")
                return
        if not self.txtId.get().isdigit():
            messagebox.showerror("Error", "El campo 'Id' solo puede contener números.")
            return
        if not self.txtCantidad.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cantidad' solo puede contener números.")
            return
        if not self.txtPrecio.get().isdigit():
            messagebox.showerror("Error", "El campo 'Precio' solo puede contener números.")
            return
        try:
            if self.usuario.existePlato(self.txtId.get()):
                messagebox.showerror("Error", f"La ID '{self.txtId.get()}' ya está registrada.")
                return
            self.usuario.crearPlato(self.txtId.get(), self.txtNombre.get(), self.txtPrecio.get(), self.txtCantidad.get(), self.txtDescripcion.get("1.0", tk.END).strip())
            messagebox.showinfo("Confirmación", "Plato registrada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la mesa. Detalles: {e}")
    
    def salir(self, event):
        """
        Cierra la ventana de registro de plato.

        Args:
            event: El evento que dispara la acción.
        """
        self.ventana.destroy()

    def limpiarCampos(self, event):
        """
        Limpia todos los campos de entrada en el formulario.

        Args:
            event: El evento que dispara la acción.
        """
        self.txtId.delete(0, tk.END)
        self.txtNombre.delete(0, tk.END)
        self.txtPrecio.delete(0, tk.END)
        self.txtCantidad.delete(0, tk.END)
        self.txtDescripcion.delete(1.0, tk.END)
        self.txtId.config(bg="#ffffff", fg="#000000")
        self.txtNombre.config(bg="#ffffff", fg="#000000")
        self.txtPrecio.config(bg="#ffffff", fg="#000000")
        self.txtCantidad.config(bg="#ffffff", fg="#000000")
        self.txtDescripcion.config(bg="#ffffff", fg="#000000")

    def soloNumeros(self, event):
        """
        Permite solo la entrada de números en los campos específicos.

        Cambia el color de fondo a rojo si se ingresa una letra en un campo numérico.

        Args:
            event: El evento que dispara la acción.
        """
        numeros = event.keysym
        if numeros.isalpha(): 
            if event.widget == self.txtId:
                self.txtId.config(bg="#F8D7DA", fg="#000000")
            elif event.widget == self.txtPrecio:
                self.txtPrecio.config(bg="#F8D7DA", fg="#000000")
            elif event.widget == self.txtCantidad:
                self.txtCantidad.config(bg="#F8D7DA", fg="#000000")
        else:
            if event.widget == self.txtId:
                self.txtId.config(bg="#ffffff", fg="#000000")
            elif event.widget == self.txtPrecio:
                self.txtPrecio.config(bg="#ffffff", fg="#000000")
            elif event.widget == self.txtCantidad:
                self.txtCantidad.config(bg="#ffffff", fg="#000000")
    
    def soloLetras(self, event):
        """
        Permite solo la entrada de letras en el campo de nombre del plato.

        Cambia el color de fondo a rojo si se ingresa un número en el campo de texto.

        Args:
            event: El evento que dispara la acción.
        """
        letras = event.keysym
        if event.widget == self.txtNombre:
            if letras.isdigit() or letras == "BackSpace":
                self.txtNombre.config(bg="#F8D7DA", fg="#000000")
            else:
                self.txtNombre.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        """
        Constructor de la clase que inicializa la ventana de registro de plato.

        Args:
            usuario: Objeto que representa al usuario actual del sistema.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro Platos")
        self.ventana.configure(width=320, height=480)
        self.ventana.resizable(0,0)

        self.usuario = usuario

        #Iconos
        self.iconoPlato = tk.PhotoImage(file=r"Restaurante/Src/plato.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Agregar Plato", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        #Textos
        self.lblId = tk.Label(self.ventana, text="Id*:")
        self.lblId.place(relx=0.28, rely=0.17, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nombre*:")
        self.lblNombre.place(relx=0.33, rely=0.27, anchor="center")

        self.lblPrecio = tk.Label(self.ventana, text="Precio*:")
        self.lblPrecio.place(relx=0.32, rely=0.37, anchor="center")

        self.lblCantidad = tk.Label(self.ventana, text="Cantidad Disponible*:")
        self.lblCantidad.place(relx=0.44, rely=0.48, anchor="center")

        self.lblDescripcion = tk.Label(self.ventana, text="Descripcion*:")
        self.lblDescripcion.place(relx=0.36, rely=0.59, anchor="center")

        #Campos de textos
        self.txtId = tk.Entry(self.ventana)
        self.txtId.place(relx=0.50, rely=0.22, anchor="center")
        self.txtId.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtId, "Ingrese el Id del plato. Solo se permiten números.")

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.50, rely=0.32, anchor="center")
        self.txtNombre.bind("<KeyPress>", self.soloLetras)
        Tooltip(self.txtNombre, "Ingrese el nombre del plato. Solo se permiten letras.")

        self.txtPrecio = tk.Entry(self.ventana)
        self.txtPrecio.place(relx=0.50, rely=0.42, anchor="center")
        self.txtPrecio.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtPrecio, "Ingrese el precio del plato. Solo se permiten números.")

        self.txtCantidad = tk.Entry(self.ventana)
        self.txtCantidad.place(relx=0.50, rely=0.53, anchor="center")
        self.txtCantidad.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCantidad, "Ingrese la cantidad disponible del plato. Solo se permiten números.")

        self.txtDescripcion = tk.Text(self.ventana, wrap="word", height=5, width=26)
        self.txtDescripcion.place(relx=0.50, rely=0.69, anchor="center")
        self.scrollbarDescripcion = tk.Scrollbar(self.ventana, command=self.txtDescripcion.yview)
        self.scrollbarDescripcion.place(relx=0.81, rely=0.69, height=69, width=10, anchor="center")
        self.txtDescripcion.config(yscrollcommand=self.scrollbarDescripcion.set)
        Tooltip(self.txtDescripcion, "Ingrese una descripción del plato.")

        #Botones
        self.btnGuardar = tk.Button(self.ventana, image=self.iconoPlato, text="Guardar", width=85, compound="left")
        self.btnGuardar.place(relx=0.34, rely=0.86, anchor="center")
        self.btnGuardar.bind("<Button-1>", self.guardarPlato)
        Tooltip(self.btnGuardar, "Guardar los datos del plato")

        self.btnLimpiar = tk.Button(self.ventana, image=self.iconoLimpiar, text="Limpiar", width=85, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.86, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.91, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de registro")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")
        
        # Atajo
        self.ventana.bind("<F4>", self.guardarPlato)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
