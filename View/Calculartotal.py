__author__ = "Luis Perdomo"
__copyright__ = "Copyright 2022, CAPS"
__credits__ = ["LDM", "Luis Perdomo", "Otros"]
__license__ = "GPL"
__version__ = "0.70.10000"
__maintainer__ = "Equipo LDM"
__email__ = "luis.perdomo@correounivalle.edu.co"
__status__ = "Pruebas"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class Calculartotal:
    """
    Esta clase maneja la interfaz gráfica para calcular el total de una comanda en un restaurante.
    Incluye funcionalidades para calcular el total de una comanda, limpiar los campos, 
    salir de la ventana y mostrar ayuda sobre el uso de la aplicación.
    """

    def mostrarAyuda(self, event):
        """
        Muestra un mensaje de ayuda con los atajos de teclado disponibles para la ventana.
        """
        mensaje_Ayuda = (
               "Ayuda", 
               "Atajos.\n\n"
               "- Presione 'F4' para calcular el total de la comanda. \n"
               "- presione 'F3' para limpiar los campos. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def calcularTotal(self, event):
        """
        Calcula el total de la comanda basada en el ID proporcionado.
        Si el estado de la comanda no es 'Servido', muestra un mensaje de advertencia.
        Muestra el total calculado y otros detalles de la comanda.

        Args:
        - event: El evento asociado al botón o atajo de teclado que invoca esta función.
        """
        if not self.txtId.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la comanda.")
            return 
        if not self.txtId.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID' solo puede contener números.")
            return
        id_comanda = int(self.txtId.get())
        
        try:
            cedula_cliente, no_mesa, platos, total_precio, estado_comanda = self.Usuario.calcularTotal(id_comanda)
            
            self.txtCedulaCli.config(state="normal")
            self.txtCedulaCli.delete(0, tk.END)
            self.txtCedulaCli.insert(0, cedula_cliente)
            self.txtCedulaCli.config(state="disabled")
            
            self.txtMesa.config(state="normal")
            self.txtMesa.delete(0, tk.END)
            self.txtMesa.insert(0, no_mesa)
            self.txtMesa.config(state="disabled")
            
            self.txtPlatos.config(state="normal")
            self.txtPlatos.delete(0, tk.END)
            self.txtPlatos.insert(0, platos)
            self.txtPlatos.config(state="disabled")
            
            self.txtPrecioTo.config(state="normal")
            self.txtPrecioTo.delete(0, tk.END)
            self.txtPrecioTo.insert(0, f"{total_precio:.2f}")
            self.txtPrecioTo.config(state="disabled")

            self.txtEstado.config(state="normal")
            self.txtEstado.delete(0, tk.END)
            self.txtEstado.insert(0, estado_comanda)
            self.txtEstado.config(state="disabled")

            if estado_comanda != "Servido":
                messagebox.showwarning("Advertencia", f"El estado de la comanda es '{estado_comanda}'. Solo se pueden calcular comandas con estado 'Servido'.")
                return

            messagebox.showinfo("Información", f"Total de la comanda con ID {id_comanda} calculado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al calcular el total de la comanda. Detalles: {e}")

    def limpiarCampos(self, event):
        """
        Limpia todos los campos de entrada en la ventana para permitir ingresar una nueva comanda.

        Args:
        - event: El evento asociado al botón o atajo de teclado que invoca esta función.
        """
        self.txtId.delete(0, tk.END)
        self.txtCedulaCli.config(state="normal")
        self.txtCedulaCli.delete(0, tk.END)
        self.txtCedulaCli.config(state="disabled")
        
        self.txtMesa.config(state="normal")
        self.txtMesa.delete(0, tk.END)
        self.txtMesa.config(state="disabled")
        
        self.txtPlatos.config(state="normal")
        self.txtPlatos.delete(0, tk.END)
        self.txtPlatos.config(state="disabled")
        
        self.txtPrecioTo.config(state="normal")
        self.txtPrecioTo.delete(0, tk.END)
        self.txtPrecioTo.config(state="disabled")
        
        self.txtEstado.config(state="normal")
        self.txtEstado.delete(0, tk.END)
        self.txtEstado.config(state="disabled")

    def salir(self, event):
        """
        Cierra la ventana de la aplicación.

        Args:
        - event: El evento asociado al botón o atajo de teclado que invoca esta función.
        """
        self.ventana.destroy()

    def __init__(self, Usuario):
        """
        Cierra la ventana de la aplicación.

        Args:
        - event: El evento asociado al botón o atajo de teclado que invoca esta función.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Calcular Total")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoCalcular = tk.PhotoImage(file=r"Restaurante\Src\Calcular.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Calcular Total Comanda", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        # Textos
        self.lblId = tk.Label(self.ventana, text="Id*: ")
        self.lblId.place(relx=0.28, rely=0.18, anchor="center")

        self.lblCedulaCli = tk.Label(self.ventana, text="Cedula Cliente*: ")
        self.lblCedulaCli.place(relx=0.39, rely=0.29, anchor="center")

        self.lblMesa = tk.Label(self.ventana, text="Mesa*: ")
        self.lblMesa.place(relx=0.31, rely=0.40, anchor="center")

        self.lblPlatos = tk.Label(self.ventana, text="Platos*: ")
        self.lblPlatos.place(relx=0.32, rely=0.51, anchor="center")

        self.lblPrecioTo = tk.Label(self.ventana, text="Precio Total*: ")
        self.lblPrecioTo.place(relx=0.36, rely=0.63, anchor="center")

        self.lblEstado = tk.Label(self.ventana, text="Estado*: ")
        self.lblEstado.place(relx=0.32, rely=0.74, anchor="center")

        # Campos de texto
        self.txtId = tk.Entry(self.ventana) 
        self.txtId.place(relx=0.50, rely=0.23, anchor="center")
        Tooltip(self.lblId, "Ingrese el ID de la comanda. Solo se permiten números.")

        self.txtCedulaCli = tk.Entry(self.ventana, state="disabled")  
        self.txtCedulaCli.place(relx=0.50, rely=0.34, anchor="center")

        self.txtMesa = tk.Entry(self.ventana, state="disabled") 
        self.txtMesa.place(relx=0.50, rely=0.45, anchor="center")

        self.txtPlatos = tk.Entry(self.ventana, state='disabled')  
        self.txtPlatos.place(relx=0.50, rely=0.56, anchor="center")

        self.txtPrecioTo = tk.Entry(self.ventana, state='disabled')  
        self.txtPrecioTo.place(relx=0.50, rely=0.68, anchor="center")

        # Entry para el estado
        self.txtEstado = tk.Entry(self.ventana, state="disabled")
        self.txtEstado.place(relx=0.50, rely=0.79, anchor="center")

        # Botones
        self.btnCalcular = tk.Button(self.ventana, image=self.iconoCalcular, text="Calcular", width=85, compound="left")
        self.btnCalcular.place(relx=0.34, rely=0.89, anchor="center")
        self.btnCalcular.bind("<Button-1>", self.calcularTotal)
        Tooltip(self.btnCalcular, "Haga clic para calcular el total de la comanda.")

        self.btnLimpiar = tk.Button(self.ventana, image=self.iconoLimpiar, text="Limpiar", width=85, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.89, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Haga clic para limpiar los campos.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda, text="Ayuda")
        self.btnAyuda.place(relx=0.9, rely=0.2, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda.")


        # Atajo
        self.ventana.bind("<F4>", self.calcularTotal)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()