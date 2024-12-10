import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class CambiarEstadoComanda():

    def mostrarAyuda(self, event):
        ayudaTexto = (
            "Instrucciones para usar la ventana:\n\n"
            "- ID: Ingrese el ID de la comanda. Solo se permiten números.\n"
            "- Cédula Cliente: Ingrese la cédula del cliente.\n"
            "- Mesa: Ingrese el número de la mesa.\n"
            "- Platos: Detalle los platos de la comanda.\n"
            "- Precio Total: Ingrese el precio total de la comanda.\n"
            "- Estado: Actualice el estado de la comanda (por ejemplo: Pendiente, En curso, Finalizado).\n\n"
            "Haga clic en 'Buscar' para buscar una comanda existente.\n"
            "Haga clic en 'Cambiar' para actualizar la información de la comanda.\n"
            "Haga clic en 'Salir' para cerrar la ventana."
        )
        messagebox.showinfo("Ayuda - Cambiar Estado Comanda", ayudaTexto)

    def salir(self, event):
            self.ventana.destroy()

    def __init__(self, usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cambiar Comanda")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0,0)

        self.usuario = usuario

        #Iconos
        self.iconoCambiar = tk.PhotoImage(file=r"Restaurante/Src/cambiar.png")
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Cambiar Estado Comanda", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        #Textos
        self.lblId = tk.Label(self.ventana, text="Id*:")
        self.lblId.place(relx=0.28, rely=0.18, anchor="center")

        self.lblCedulaCli = tk.Label(self.ventana, text="Cedula Cliente*:")
        self.lblCedulaCli.place(relx=0.39, rely=0.29, anchor="center")

        self.lblMesa = tk.Label(self.ventana, text="Mesa*:")
        self.lblMesa.place(relx=0.31, rely=0.40, anchor="center")

        self.lblPlatos = tk.Label(self.ventana, text="Platos*:")
        self.lblPlatos.place(relx=0.32, rely=0.51, anchor="center")

        self.lblPrecioTo = tk.Label(self.ventana, text="Precio Total*:")
        self.lblPrecioTo.place(relx=0.36, rely=0.63, anchor="center")

        self.lblEstado = tk.Label(self.ventana, text="Estado*:")
        self.lblEstado.place(relx=0.32, rely=0.74, anchor="center")

        #Campos de textos
        self.txtId = tk.Entry(self.ventana)
        self.txtId.place(relx=0.50, rely=0.23, anchor="center")
        Tooltip(self.lblId, "Ingrese el ID de la comanda. Solo se permiten números.")

        self.txtCedulaCli = tk.Entry(self.ventana)
        self.txtCedulaCli.place(relx=0.50, rely=0.34, anchor="center")
        Tooltip(self.lblCedulaCli, "Ingrese la cédula del cliente.")

        self.txtMesa = tk.Entry(self.ventana)
        self.txtMesa.place(relx=0.50, rely=0.45, anchor="center")
        Tooltip(self.lblMesa, "Ingrese el número de la mesa.")

        self.txtPlatos = tk.Entry(self.ventana)
        self.txtPlatos.place(relx=0.50, rely=0.56, anchor="center")
        Tooltip(self.lblPlatos, "Detalle los platos de la comanda.")

        self.txtPrecioTo = tk.Entry(self.ventana)
        self.txtPrecioTo.place(relx=0.50, rely=0.68, anchor="center")
        Tooltip(self.lblPrecioTo, "Ingrese el precio total de la comanda.")

        self.txtEstado = tk.Entry(self.ventana)
        self.txtEstado.place(relx=0.50, rely=0.79, anchor="center")
        Tooltip(self.lblEstado, "Actualice el estado de la comanda.")

        #Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.89, anchor="center")
        Tooltip(self.btnBuscar, "Haga clic para buscar una comanda existente.")

        self.btnCambiar = tk.Button(self.ventana, image=self.iconoCambiar, text="Cambiar", width=85, compound="left")
        self.btnCambiar.place(relx=0.65, rely=0.89, anchor="center")
        Tooltip(self.btnCambiar, "Haga clic para actualizar la información de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        self.ventana.mainloop()
