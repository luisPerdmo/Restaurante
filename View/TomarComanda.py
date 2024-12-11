import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class TomarComanda():

    def mostrarAyuda(self, event):
        mensaje_ayuda = (
            "Ayuda - Tomar Comanda:\n\n"
            "1. **Id**: Ingrese el ID único de la comanda. Este campo es obligatorio.\n"
            "2. **Cédula Cliente**: Este campo se completará automáticamente si el cliente ya está registrado. "
            "De lo contrario, debe ingresar una cédula válida para el cliente.\n"
            "3. **Mesa**: Este campo indica el número de la mesa asociada con la comanda. Se completará automáticamente.\n"
            "4. **Platos**: Contiene la lista de platos seleccionados para la comanda. Este campo será gestionado por el sistema.\n"
            "5. **Precio Total**: Calculado automáticamente en base a los platos seleccionados.\n"
            "6. **Estado**: Use el menú desplegable para seleccionar el estado actual de la comanda, ya sea 'en preparación' o 'servido'.\n"
            "7. **Guardar**: Haga clic en este botón para guardar la información ingresada y asociar la comanda al cliente.\n"
            "8. **Salir**: Cierra la ventana sin realizar cambios adicionales.\n\n"
            "Para obtener más información, contacte con el administrador del sistema."
        )
        messagebox.showinfo("Ayuda - Tomar Comanda", mensaje_ayuda)

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Tomar Comanda")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoGuardar = tk.PhotoImage(file=r"Restaurante/Src/guardar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Tomar Comanda", font=("Times", 20, "bold"))
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

        self.txtCedulaCli = tk.Entry(self.ventana, state='disabled')  
        self.txtCedulaCli.place(relx=0.50, rely=0.34, anchor="center")

        self.txtMesa = tk.Entry(self.ventana, state='disabled') 
        self.txtMesa.place(relx=0.50, rely=0.45, anchor="center")

        self.txtPlatos = tk.Entry(self.ventana, state='disabled')  
        self.txtPlatos.place(relx=0.50, rely=0.56, anchor="center")

        self.txtPrecioTo = tk.Entry(self.ventana, state='disabled')  
        self.txtPrecioTo.place(relx=0.50, rely=0.68, anchor="center")

        # Combobox para el estado
        self.estado_var = tk.StringVar()
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["en preparación", "servido"])
        self.cmbEstado.place(relx=0.50, rely=0.79, anchor="center")

        # Botones
        self.btnGuardar = tk.Button(self.ventana, image=self.iconoGuardar, text="Gardar", width=85, compound="left")
        self.btnGuardar.place(relx=0.34, rely=0.89, anchor="center")
        #self.btnGuardar.bind("<Button-1>", self.cambiarEstado)
        Tooltip(self.btnGuardar, "Haga clic para guardar la información de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=85, compound="left")
        self.btnSalir.place(relx=0.65, rely=0.89, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        self.ventana.mainloop()

