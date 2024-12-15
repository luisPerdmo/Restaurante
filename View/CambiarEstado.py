import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip


class CambiarEstado():

    def mostrarAyuda(self, event):
            mensaje_Ayuda = (
               "Atajos.\n\n"
               #"- presione 'F3' para cambiar el estado. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n"  
            )
            messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha(): 
            self.txtId.config(bg="#F8D7DA", fg="#000000")
        else:
            self.txtId.config(bg="#ffffff", fg="#000000")

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cambiar Estado")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoCambiar = tk.PhotoImage(file=r"Restaurante/Src/infrome.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Cambiar Estado Comanda", font=("Times", 20, "bold"))
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
        self.txtId.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.lblId, "Ingrese el ID de la comanda. Solo se permiten números.")

        self.txtCedulaCli = tk.Entry(self.ventana, state='disabled')  
        self.txtCedulaCli.place(relx=0.50, rely=0.34, anchor="center")
        Tooltip(self.lblCedulaCli, "Ingrese la cédula del cliente.")

        self.txtMesa = tk.Entry(self.ventana, state='disabled') 
        self.txtMesa.place(relx=0.50, rely=0.45, anchor="center")
        Tooltip(self.lblMesa, "Ingrese el número de la mesa.")

        self.txtPlatos = tk.Entry(self.ventana, state='disabled')  
        self.txtPlatos.place(relx=0.50, rely=0.56, anchor="center")
        Tooltip(self.lblPlatos, "Detalle los platos de la comanda.")

        self.txtPrecioTo = tk.Entry(self.ventana, state='disabled')  
        self.txtPrecioTo.place(relx=0.50, rely=0.68, anchor="center")
        Tooltip(self.lblPrecioTo, "Ingrese el precio total de la comanda.")

        # Combobox para el estado
        self.estado_var = tk.StringVar()
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Servido"], state='disabled')
        self.cmbEstado.place(relx=0.50, rely=0.79, anchor="center")
        Tooltip(self.lblEstado, "Seleccione el estado de la comanda.")

        # Botones
        self.btnCalcular = tk.Button(self.ventana, image=self.iconoCambiar, text="Calcular", width=185, compound="left")
        self.btnCalcular.place(relx=0.49, rely=0.89, anchor="center")
        #self.btnCalcular.bind("<Button-1>", self.cambiarEstado)
        #Tooltip(self.btnCalcular, "Haga clic para actualizar la información de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        # Atajo
        #self.ventana.bind("<>", self.cambiarEstado)
        self.ventana.bind("<>", self.salir)
        self.ventana.bind("<>", self.mostrarAyuda)

        self.ventana.mainloop()

