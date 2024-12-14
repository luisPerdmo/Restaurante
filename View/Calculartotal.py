import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip


class Calculartotal():

    def limpiarCampos(self, event):
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
        
        self.estado_var.set("")

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Calcular Total")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoCalcular = tk.PhotoImage(file=r"Restaurante\Src\buscar.png")
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

        # Combobox para el estado
        self.estado_var = tk.StringVar(value="Servido")
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Servido"],  state='disabled')
        self.cmbEstado.place(relx=0.50, rely=0.79, anchor="center")

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

        self.ventana.mainloop()