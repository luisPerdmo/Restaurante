import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarPlato():
    """
    Clase que permite gestionar la eliminación de un plato en el sistema.
    La clase incluye la búsqueda y eliminación de un plato, así como funcionalidades para limpiar campos, 
    mostrar ayuda y manejar la interfaz gráfica.
    """

    def mostrarAyuda(self, event):
        """
        Muestra una ventana emergente con los atajos de teclado disponibles.

        Parameters:
        event (tkinter.Event): El evento que dispara el método.
        """
        mensaje_Ayuda = (
            "Atajos.\n\n"
            "- Presione 'F4' para guardar los datos. \n"
            "- presione 'F3' para eliminar los campos. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"      
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def limpiarCampos(self, event):
        """
        Limpia todos los campos del formulario de entrada de datos.

        Los campos de texto se vacían y se reinicia el estado de los widgets.

        Parameters:
        event (tkinter.Event): El evento que dispara el método.
        """
        self.txtNombre.config(state="normal")
        self.txtPrecio.config(state="normal")
        self.txtCantidad.config(state="normal")
        self.txtDescripcion.config(state="normal")
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
        self.txtNombre.config(state="disabled")
        self.txtPrecio.config(state="disabled")
        self.txtCantidad.config(state="disabled")
        self.txtDescripcion.config(state="disabled")

    def buscarPlato(self, event):
        """
        Busca un plato en el sistema utilizando el ID ingresado en el formulario.

        Si el plato existe, llena los campos del formulario con la información del plato.

        Parameters:
        event (tkinter.Event): El evento que dispara el método.
        """
        if not self.txtId.get():
            messagebox.showerror("Error", "Por favor ingrese el id del palto.")
            return
        if not self.txtId.get().isdigit():
            messagebox.showerror("Error", "El campo 'Id' solo puede contener números.")
            return
        iD = int(self.txtId.get())
        try:
            plato = self.obtenerPlato(iD)
            if plato:
                self.txtNombre.config(state="normal")
                self.txtPrecio.config(state="normal")
                self.txtCantidad.config(state="normal")
                self.txtDescripcion.config(state="normal")
                self.txtNombre.delete(0, tk.END)
                self.txtNombre.insert(0, plato[1])
                self.txtPrecio.delete(0, tk.END)
                self.txtPrecio.insert(0, plato[2])
                self.txtCantidad.delete(0, tk.END)
                self.txtCantidad.insert(0, plato[3])
                self.txtDescripcion.delete(1.0, tk.END)
                self.txtDescripcion.insert(1.0, plato[4])
                self.txtNombre.config(state="disabled")
                self.txtPrecio.config(state="disabled")
                self.txtCantidad.config(state="disabled")
                self.txtDescripcion.config(state="disabled")
                messagebox.showinfo("Información", f"Plato con {iD} encontrado.")
                self.btnEliminar.config(state="normal")
            else:
                messagebox.showinfo("Información", f"El plato {iD} no es un plato.")
                self.btnEliminar.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el plato. Detalles: {e}")

    def obtenerPlato(self, plato):
        """
        Obtiene un plato desde la base de datos o sistema utilizando su ID.

        Parameters:
        plato (int): El ID del plato a obtener.

        Returns:
        tuple: Una tupla con la información del plato, o None si no se encuentra.
        """
        return self.usuario.buscarPlato(plato)
    
    def eliminarPlato(self, event):
        """
        Elimina un plato del sistema utilizando el ID ingresado en el formulario.

        Parameters:
        event (tkinter.Event): El evento que dispara el método.
        """
        if not self.txtId.get():
            messagebox.showerror("Error", "Por favor ingrese el plato.")
            return
        if not self.txtId.get().isdigit():
            messagebox.showerror("Error", "El campo 'id' solo puede contener números.")
            return
        iD = int(self.txtId.get())
        plato = self.obtenerPlato(iD)
        if not plato:
            messagebox.showinfo("Información", f"Plato {iD} no encontrada.")
            return
        try:
            self.usuario.eliminarPlato(iD)
            messagebox.showinfo("Confirmación", f"Plato {iD} eliminada con éxito.")
            self.limpiarCampos(event)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el Plato. Detalles: {e}")

    def soloNumeros(self, event):
        """
        Verifica si la tecla presionada es un número, y cambia el color de fondo del campo de texto.

        Parameters:
        event (tkinter.Event): El evento de la tecla presionada.
        """
        numeros = event.keysym
        if numeros.isalpha(): 
            if event.widget == self.txtId:
                self.txtId.config(bg="#F8D7DA", fg="#000000")
        else:
            if event.widget == self.txtId:
                self.txtId.config(bg="#ffffff", fg="#000000")

    def salir(self, event):
        """
        Cierra la ventana actual.

        Parameters:
        event (tkinter.Event): El evento que dispara el método.
        """
        self.ventana.destroy()

    def __init__(self, usuario):
        """
        Constructor de la clase EliminarPlato.

        Inicializa la ventana, los elementos de la interfaz, y las funcionalidades.

        Parameters:
        usuario (object): Un objeto que contiene los métodos necesarios para interactuar con la base de datos.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro Platos")
        self.ventana.configure(width=320, height=480)
        self.ventana.resizable(0,0)

        self.usuario = usuario

        #Iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Restaurante/Src/eliminarMesa.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Plato", font=("Times", 20, "bold"))
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
        self.txtNombre.config(state="disabled")
        Tooltip(self.txtNombre, "Ingrese el nombre del plato. Solo se permiten letras.")

        self.txtPrecio = tk.Entry(self.ventana)
        self.txtPrecio.place(relx=0.50, rely=0.42, anchor="center")
        self.txtPrecio.config(state="disabled")
        Tooltip(self.txtPrecio, "Ingrese el precio del plato. Solo se permiten números.")

        self.txtCantidad = tk.Entry(self.ventana)
        self.txtCantidad.place(relx=0.50, rely=0.53, anchor="center")
        self.txtCantidad.config(state="disabled")
        Tooltip(self.txtCantidad, "Ingrese la cantidad disponible del plato. Solo se permiten números.")

        self.txtDescripcion = tk.Text(self.ventana, wrap="word", height=5, width=26)
        self.txtDescripcion.place(relx=0.50, rely=0.69, anchor="center")
        self.scrollbarDescripcion = tk.Scrollbar(self.ventana, command=self.txtDescripcion.yview)
        self.scrollbarDescripcion.place(relx=0.81, rely=0.69, height=69, width=10, anchor="center")
        self.txtDescripcion.config(state="disabled")
        self.txtDescripcion.config(yscrollcommand=self.scrollbarDescripcion.set)
        Tooltip(self.txtDescripcion, "Ingrese una descripción del plato.")

        #Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.86, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarPlato)
        Tooltip(self.btnBuscar, "Guardar los datos del plato")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar, text="Eliminar", width=85, compound="left")
        self.btnEliminar.place(relx=0.65, rely=0.86, anchor="center")
        self.btnEliminar.bind("<Button-1>", self.eliminarPlato)
        Tooltip(self.btnEliminar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.91, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de registro")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")
        
        # Atajos
        self.ventana.bind("<F4>", self.buscarPlato)
        self.ventana.bind("<F3>", self.eliminarPlato)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)
        
        self.ventana.mainloop()
