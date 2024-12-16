_author_ = "Luis Perdomo"
_copyright_ = "Copyright 2022, CAPS"
_credits_ = ["LDM", "Luis Perdomo", "Otros"]
_license_ = "GPL"
_version_ = "0.70.10000"
_maintainer_ = "Equipo LDM"
_email_ = "luis.perdomo@correounivalle.edu.co"
_status_ = "Pruebas"

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from Tooltip import Tooltip

class InformeDiario():

    def mostrarAyuda(self, event):
        """
        Muestra un cuadro de diálogo con los atajos de teclado disponibles.
        """
        mensaje_ayuda = ( 
            "Atajos.\n\n"
            "- Presione 'F3' para generar un informe. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def generarInforme(self, event):
        """
        Genera el informe diario a través de la función correspondiente de la clase Usuario,
        y actualiza los valores mostrados en la interfaz con la información obtenida.
        """
        try:
            informe = self.Usuario.generarInformeDiario()
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            self.actualizarValores(
                informe["id_informe"],
                fecha_actual,
                informe["cantidad_comandas"],
                informe["ganancia_total"],
                informe["promedio_dia"]
            )
            messagebox.showinfo("Éxito", "Informe diario generado correctamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiarCampos(self, event):
        """
        Limpia todos los valores mostrados en los campos del informe.
        """
        self.lblIdInformeValor.config(text="")
        self.lblFechaInformeValor.config(text="")
        self.lblCantidadComandasValor.config(text="")
        self.lblGananciaDiaValor.config(text="")
        self.lblPromedioDiaValor.config(text="")

    def salir(self, event):
        """
        Cierra la ventana de la interfaz de informe diario.
        """
        self.ventana.destroy()

    def actualizarValores(self, id_informe, fecha, cantidad, ganancia, promedio):
        """
        Actualiza los campos de la interfaz con los nuevos valores del informe.
        """
        self.lblIdInformeValor.config(text=id_informe)
        self.lblFechaInformeValor.config(text=fecha)
        self.lblCantidadComandasValor.config(text=cantidad)
        self.lblGananciaDiaValor.config(text=ganancia)
        self.lblPromedioDiaValor.config(text=promedio)

    def guardarInforme(self, event):
        """
        Muestra un cuadro de confirmación indicando que los valores se han actualizado correctamente.
        """
        messagebox.showinfo("Confirmación", "Los valores han sido actualizados correctamente.")

    def __init__(self, Usuario):
        """
        Inicializa la interfaz gráfica, configurando los widgets y los atajos de teclado.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Informe Diario")
        self.ventana.configure(width=400, height=400, bg="lightgray")
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoInforme = tk.PhotoImage(file=r"Restaurante/Src/infrome.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante\Src\ayuda.png")

        self.lblTitulo = tk.Label(self.ventana, text="Registro de Informe Diario", font=("Times", 20, "bold"), bg="lightgray", fg="black")
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        # Etiquetas y valores dinámicos
        self.lblIdInforme = tk.Label(self.ventana, text="ID Informe*: ", bg="lightgray", fg="black")
        self.lblIdInforme.place(relx=0.10, rely=0.20, anchor="w")
        self.lblIdInformeValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=13)
        self.lblIdInformeValor.place(relx=0.60, rely=0.20, anchor="center")

        self.lblFechaInforme = tk.Label(self.ventana, text="Fecha*: ", bg="lightgray", fg="black")
        self.lblFechaInforme.place(relx=0.10, rely=0.30, anchor="w")
        self.lblFechaInformeValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=13)
        self.lblFechaInformeValor.place(relx=0.60, rely=0.30, anchor="center")

        self.lblCantidadComandas = tk.Label(self.ventana, text="Cantidad Comandas*: ", bg="lightgray", fg="black")
        self.lblCantidadComandas.place(relx=0.10, rely=0.40, anchor="w")
        self.lblCantidadComandasValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=13)
        self.lblCantidadComandasValor.place(relx=0.60, rely=0.40, anchor="center")

        self.lblGananciaDia = tk.Label(self.ventana, text="Ganancia del Día*: ", bg="lightgray", fg="black")
        self.lblGananciaDia.place(relx=0.10, rely=0.50, anchor="w")
        self.lblGananciaDiaValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=13)
        self.lblGananciaDiaValor.place(relx=0.60, rely=0.50, anchor="center")

        self.lblPromedioDia = tk.Label(self.ventana, text="Promedio del Día*: ", bg="lightgray", fg="black")
        self.lblPromedioDia.place(relx=0.10, rely=0.60, anchor="w")
        self.lblPromedioDiaValor = tk.Label(self.ventana, text="", bg="lightgray", fg="black", width=13)
        self.lblPromedioDiaValor.place(relx=0.60, rely=0.60, anchor="center")

        # Botón
        self.btnGenerarInforme = tk.Button(self.ventana, image=self.iconoInforme, text="Generar Informe", width=185, compound="left")
        self.btnGenerarInforme.place(relx=0.5, rely=0.77, anchor="center")
        self.btnGenerarInforme.bind("<Button-1>", self.generarInforme)

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=185, image=self.iconoSalir, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.85, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda, text="Ayuda", bg="lightgray")
        self.btnAyuda.place(relx=0.95, rely=0.12, anchor="ne")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)

        # Atajo
        self.ventana.bind("<F3>", self.generarInforme)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()