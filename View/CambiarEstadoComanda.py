import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EnviarComanda():

    def salirApp(self, event):
        respuesta = messagebox.askquestion("Confirmación", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cambiar Estado")
        self.ventana.config(width=400, height=420)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Cambiar Estado Comanda", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        self.lblId = tk.Label(self.ventana, text="Id*:", width=18, anchor="e")
        self.lblId.place(relx=0.4, rely=0.2, anchor="e")
        self.txtId = tk.Entry(self.ventana, width=20)
        self.txtId.place(relx=0.4, rely=0.2, anchor="w")

        self.lblCedulaCliente = tk.Label(self.ventana, text="Cédula Cliente*:", width=18, anchor="e")
        self.lblCedulaCliente.place(relx=0.4, rely=0.3, anchor="e")
        self.txtCedula = tk.Entry(self.ventana, width=20, state="readonly")
        self.txtCedula.place(relx=0.4, rely=0.3, anchor="w")

        self.lblMesa = tk.Label(self.ventana, text="No. Mesa*:", width=18, anchor="e")
        self.lblMesa.place(relx=0.4, rely=0.4, anchor="e")
        self.txtMesa = tk.Entry(self.ventana, width=20, state="readonly")
        self.txtMesa.place(relx=0.4, rely=0.4, anchor="w")

        self.lblPlato = tk.Label(self.ventana, text="Plato*:", width=18, anchor="e")
        self.lblPlato.place(relx=0.4, rely=0.5, anchor="e")
        self.txtPlato = tk.Entry(self.ventana, width=20, state="readonly")
        self.txtPlato.place(relx=0.4, rely=0.5, anchor="w")

        self.lblPrecioTotal = tk.Label(self.ventana, text="Precio Total:", width=18, anchor="e")
        self.lblPrecioTotal.place(relx=0.4, rely=0.6, anchor="e")
        self.txtPrecioTotal = tk.Entry(self.ventana, width=20, state="readonly")
        self.txtPrecioTotal.place(relx=0.4, rely=0.6, anchor="w")

        self.lblEstado = tk.Label(self.ventana, text="Estado*:", width=18, anchor="e")
        self.lblEstado.place(relx=0.4, rely=0.7, anchor="e")
        self.txtEstado = ttk.Combobox(self.ventana, values=["Servido"], width=17, state="readonly")
        self.txtEstado.place(relx=0.4, rely=0.7, anchor="w")

        # Botones
        self.btnGuardar = tk.Button(self.ventana, text="Calcular Total", width=15)
        self.btnGuardar.place(relx=0.35, rely=0.85, anchor="center")

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=15)
        self.btnSalir.place(relx=0.65, rely=0.85, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salirApp)

        self.ventana.mainloop()
