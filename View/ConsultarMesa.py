import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class ConsultarMesa():

    def mostrarAyuda(self, event):
        ayuda = """
        Formulario de Consulta de Mesa:
        - ID de Mesa: Ingrese el ID de la mesa que desea consultar. Solo se permiten números.
        - Cantidad de Comensales: Se muestra automáticamente al buscar la mesa.
        - Estado: Muestra el estado de la mesa después de realizar la búsqueda.
        - Buscar: Presione para consultar los datos de la mesa por el ID ingresado.
        - Eliminar: Este botón se habilita si la mesa ha sido encontrada y permite eliminar la mesa seleccionada.

        Recuerde que los campos Cantidad de Comensales y Estado estarán deshabilitados hasta que realice la búsqueda.
        """
        messagebox.showinfo("Ayuda - Consultar Mesa", ayuda)

    def limpiarCampos(self, event):
        self.txtEstado.config(state="normal")
        self.txtCantidadComensales.config(state="normal")
        self.txtIdMesa.delete(0, tk.END)
        self.txtCantidadComensales.delete(0, tk.END)
        self.txtEstado.delete(0, tk.END)
        self.txtCantidadComensales.config(bg="#ffffff")
        self.txtEstado.config(bg="#ffffff")
        self.txtEstado.config(state="disabled")
        self.txtCantidadComensales.config(state="disabled")

    def salir(self, event):
        self.ventana.destroy()

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Consultar Mesa")
        self.ventana.configure(width=320, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        #iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Restaurante/Src/eliminarMesa.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Consultar Mesa", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.11, anchor="center")

        # Etiquetas
        self.lblIdMesa = tk.Label(self.ventana, text="ID de Mesa*: ")
        self.lblIdMesa.place(relx=0.36, rely=0.27, anchor="center")

        self.lblCantidadComensales = tk.Label(self.ventana, text="Cantidad Comensales: ")
        self.lblCantidadComensales.place(relx=0.45, rely=0.40, anchor="center")

        self.lblEstado = tk.Label(self.ventana, text="Estado: ")
        self.lblEstado.place(relx=0.32, rely=0.53, anchor="center")

        # Campos de texto
        self.txtIdMesa = tk.Entry(self.ventana)
        self.txtIdMesa.place(relx=0.50, rely=0.33, anchor="center")
        self.txtIdMesa.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtIdMesa, "Ingrese el ID de la mesa. Solo se permiten números.")

        self.txtCantidadComensales = tk.Entry(self.ventana)
        self.txtCantidadComensales.place(relx=0.50, rely=0.46, anchor="center")
        self.txtCantidadComensales.config(state="disabled")
        Tooltip(self.txtCantidadComensales, "La cantidad de comensales se muestra tras buscar la mesa.")

        self.txtEstado = tk.Entry(self.ventana)
        self.txtEstado.place(relx=0.50, rely=0.59, anchor="center")
        self.txtEstado.config(state="disabled")
        Tooltip(self.txtEstado, "El estado de la mesa se muestra tras buscarla.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=self.iconoBuscar, width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.74, anchor="center")
        #self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", image=self.iconoEliminar, width=85, state="disabled", compound="left")
        self.btnEliminar.place(relx=0.66, rely=0.74, anchor="center")
       # self.btnEliminar.bind("<Button-1>", self.eliminarMesa)
        Tooltip(self.btnEliminar, "Eliminar mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, width=185, compound="left")
        self.btnLimpiar.place(relx=0.5, rely=0.81, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", image=self.iconoSalir, width=185, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.88, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de eliminación de mesas")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()
