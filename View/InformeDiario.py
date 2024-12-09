import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class InformeDiario():

    def limpiarCampos(self, event):
        self.lblIdInformeValor.config(text="")
        self.lblFechaInformeValor.config(text="")
        self.lblCantidadComandasValor.config(text="")
        self.lblGananciaDiaValor.config(text="")
        self.lblPromedioDiaValor.config(text="")

    def salir(self, event):
        self.ventana.destroy()

    def actualizarValores(self, id_informe, fecha, cantidad, ganancia, promedio):
        self.lblIdInformeValor.config(text=id_informe)
        self.lblFechaInformeValor.config(text=fecha)
        self.lblCantidadComandasValor.config(text=cantidad)
        self.lblGananciaDiaValor.config(text=ganancia)
        self.lblPromedioDiaValor.config(text=promedio)

    def guardarInforme(self, event):
        messagebox.showinfo("Confirmación", "Los valores han sido actualizados correctamente.")

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Informe Diario")
        self.ventana.configure(width=400, height=400, bg="lightgray")
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        #iconos
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")

        self.lblTitulo = tk.Label(self.ventana, text="Registro de Informe Diario", font=("Times", 20, "bold"), bg="lightgray", fg="black")
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        # Etiquetas y valores dinámicos
        self.lblIdInforme = tk.Label(self.ventana, text="ID Informe*: ", bg="lightgray", fg="black")
        self.lblIdInforme.place(relx=0.10, rely=0.20, anchor="w")
        self.lblIdInformeValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=20)
        self.lblIdInformeValor.place(relx=0.60, rely=0.20, anchor="center")

        self.lblFechaInforme = tk.Label(self.ventana, text="Fecha*: ", bg="lightgray", fg="black")
        self.lblFechaInforme.place(relx=0.10, rely=0.30, anchor="w")
        self.lblFechaInformeValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=20)
        self.lblFechaInformeValor.place(relx=0.60, rely=0.30, anchor="center")

        self.lblCantidadComandas = tk.Label(self.ventana, text="Cantidad Comandas*: ", bg="lightgray", fg="black")
        self.lblCantidadComandas.place(relx=0.10, rely=0.40, anchor="w")
        self.lblCantidadComandasValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=20)
        self.lblCantidadComandasValor.place(relx=0.60, rely=0.40, anchor="center")

        self.lblGananciaDia = tk.Label(self.ventana, text="Ganancia del Día*: ", bg="lightgray", fg="black")
        self.lblGananciaDia.place(relx=0.10, rely=0.50, anchor="w")
        self.lblGananciaDiaValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=20)
        self.lblGananciaDiaValor.place(relx=0.60, rely=0.50, anchor="center")

        self.lblPromedioDia = tk.Label(self.ventana, text="Promedio del Día*: ", bg="lightgray", fg="black")
        self.lblPromedioDia.place(relx=0.10, rely=0.60, anchor="w")
        self.lblPromedioDiaValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=20)
        self.lblPromedioDiaValor.place(relx=0.60, rely=0.60, anchor="center")

        # Botón Salir
        self.btnSalir = tk.Button(self.ventana, text="Salir", width=185, image=self.iconoSalir, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.85, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)

        self.ventana.mainloop()

