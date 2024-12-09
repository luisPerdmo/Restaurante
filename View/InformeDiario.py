import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class InformeDiario():

    def limpiarCampos(self, event):
        self.txtIdInforme.delete(0, tk.END)
        self.txtFechaInforme.delete(0, tk.END)
        self.txtCantidadComandas.delete(0, tk.END)
        self.txtGananciaDia.delete(0, tk.END)
        self.txtPromedioDia.delete(0, tk.END)
        self.txtIdInforme.config(bg="#ffffff")
        self.txtFechaInforme.config(bg="#ffffff")
        self.txtCantidadComandas.config(bg="#ffffff")
        self.txtGananciaDia.config(bg="#ffffff")
        self.txtPromedioDia.config(bg="#ffffff")

    def salir(self, event):
        self.ventana.destroy()

    def guardarInforme(self, event):
        pass

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Informe Diario")
        self.ventana.configure(width=400, height=400)
        self.ventana.resizable(0, 0)

        self.Usuario=Usuario

        #iconos
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Registro de Informe Diario", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        # Etiquetas
        self.lblIdInforme = tk.Label(self.ventana, text="ID Informe*: ")
        self.lblIdInforme.place(relx=0.30, rely=0.20, anchor="center")

        self.lblFechaInforme = tk.Label(self.ventana, text="Fecha*: ")
        self.lblFechaInforme.place(relx=0.30, rely=0.30, anchor="center")

        self.lblCantidadComandas = tk.Label(self.ventana, text="Cantidad Comandas*: ")
        self.lblCantidadComandas.place(relx=0.37, rely=0.40, anchor="center")

        self.lblGananciaDia = tk.Label(self.ventana, text="Ganancia del Día*: ")
        self.lblGananciaDia.place(relx=0.37, rely=0.50, anchor="center")

        self.lblPromedioDia = tk.Label(self.ventana, text="Promedio del Día*: ")
        self.lblPromedioDia.place(relx=0.37, rely=0.60, anchor="center")

        # Campos de texto
        self.txtIdInforme = tk.Entry(self.ventana)
        self.txtIdInforme.place(relx=0.60, rely=0.20, anchor="center")
        Tooltip(self.txtIdInforme, "Ingrese el ID del informe.")

        self.txtFechaInforme = tk.Entry(self.ventana)
        self.txtFechaInforme.place(relx=0.60, rely=0.30, anchor="center")
        Tooltip(self.txtFechaInforme, "Ingrese la fecha del informe en formato YYYY-MM-DD.")

        self.txtCantidadComandas = tk.Entry(self.ventana)
        self.txtCantidadComandas.place(relx=0.60, rely=0.40, anchor="center")
        Tooltip(self.txtCantidadComandas, "Ingrese la cantidad de comandas del día.")

        self.txtGananciaDia = tk.Entry(self.ventana)
        self.txtGananciaDia.place(relx=0.60, rely=0.50, anchor="center")
        Tooltip(self.txtGananciaDia, "Ingrese la ganancia obtenida durante el día.")

        self.txtPromedioDia = tk.Entry(self.ventana)
        self.txtPromedioDia.place(relx=0.60, rely=0.60, anchor="center")
        Tooltip(self.txtPromedioDia, "Ingrese el promedio de ingresos por comanda.")

        # Botones
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", width=15)
        self.btnRegistrar.place(relx=0.35, rely=0.75, anchor="center")
        self.btnRegistrar.bind("<Button-1>", self.guardarInforme)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", width=85, image=self.iconoLimpiar, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.75, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=185, image=self.iconoSalir, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.85, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)

        self.ventana.mainloop()
