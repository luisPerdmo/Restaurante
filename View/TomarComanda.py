_author_ = "Luis Perdomo"
_copyright_ = "Copyright 2022, CAPS"
_credits_ = ["LDM", "Luis Perdomo", "Otros"]
_license_ = "GPL"
_version_ = "0.70.10000"
_maintainer_ = "Equipo LDM"
_email_ = "luis.perdomo@correounivalle.edu.co"
_status_ = "Pruebas"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class TomarComanda():
    """
    Clase para gestionar la interfaz gráfica de la toma de comandas en un restaurante.

    Permite al usuario validar clientes y mesas, calcular el precio total de los platos,
    guardar la información de la comanda, y proporcionar ayuda sobre el uso de la ventana.
    """

    def validar_cliente_mesa(self, event):
        """
        Valida que el cliente y la mesa ingresados sean correctos y estén disponibles.
        
        Parámetros:
        - event: Evento que dispara la validación (como un clic en el botón "Buscar").

        Validaciones:
        - Verifica que la cédula del cliente no esté vacía.
        - Comprueba que el número de mesa sea numérico.
        - Valida que el cliente exista en el sistema.
        - Verifica que la mesa exista y que esté ocupada.

        Acciones:
        - Habilita el campo para ingresar los platos si todas las validaciones son exitosas.
        - Muestra mensajes de error o éxito según corresponda.
        """
        cedula = self.txtCedulaCli.get().strip()
        mesa = self.txtMesa.get().strip()
        if not cedula:
            messagebox.showerror("Error", "La cédula del cliente es obligatoria.")
            return
        if not mesa.isdigit():
            messagebox.showerror("Error", "El número de mesa debe ser numérico.")
            return
        no_mesa = int(mesa)
        cliente = self.Usuario.buscarCliente(cedula)
        if not cliente:
            messagebox.showerror("Error", "El cliente con esta cédula no existe.")
            return
        mesa_existente = self.Usuario.buscarMesa(no_mesa)
        if not mesa_existente:
            messagebox.showerror("Error", "La mesa especificada no existe.")
            return
        estado_mesa = mesa_existente[2].lower()  
        if estado_mesa != "ocupada":  
            messagebox.showerror("Error", "La mesa especificada no está ocupada.")
            return
       
        self.txtPlatos.config(state='normal')  
        self.txtCedulaCli.config(state='normal')  
        self.txtMesa.config(state='normal') 
        messagebox.showinfo("Validación exitosa", "Cliente y mesa válidos. Ahora puede ingresar los platos.")

    def calcular_precio_total(self, event):
        """
        Calcula el precio total de los platos seleccionados en la comanda.

        Parámetros:
        - event: Evento que dispara el cálculo (como un clic en el botón "Guardar").

        Validaciones:
        - Verifica que se haya ingresado una lista de platos.
        - Comprueba que los IDs de los platos sean numéricos y válidos.
        - Calcula el precio total utilizando un método del objeto Usuario.

        Acciones:
        - Muestra mensajes de error en caso de validaciones fallidas.
        - Deshabilita el campo de precio total tras el cálculo exitoso.
        """
        platos_str = self.txtPlatos.get().strip()
        if not platos_str:
            messagebox.showwarning("Advertencia", "Debe ingresar al menos un plato para calcular el precio total.")
            return
        try:
            lista_platos = [int(id_plato) for id_plato in platos_str.split('-')]
        except ValueError:
            messagebox.showerror("Error", "Los platos deben ser una lista de números separados por guiones (ej. 1-2-3).")
            return
        for id_plato in lista_platos:
            if not self.Usuario.existePlato(id_plato):
                messagebox.showerror("Error", f"El plato con ID {id_plato} no existe.")
                return
        id_comanda = self.txtId.get().strip()
        cedula_cliente = self.txtCedulaCli.get().strip()
        no_mesa = self.txtMesa.get().strip()
        precio_total = self.Usuario.tomarComanda(id_comanda, cedula_cliente, no_mesa, lista_platos)
        self.txtPrecioTo.config(state='disabled')
        messagebox.showinfo("Informarcion", "Comanda tomada con exito")

    def guardar_comanda(self):
        """
        Guarda la información de la comanda en el sistema.

        Validaciones:
        - Verifica que todos los campos requeridos estén completos.
        - Valida que los datos ingresados sean correctos (como IDs numéricos).

        Acciones:
        - Llama al método correspondiente del objeto Usuario para registrar la comanda.
        - Limpia los campos de entrada tras guardar la información.
        - Muestra mensajes de error en caso de validaciones fallidas.
        """
        id_comanda = self.txtId.get().strip()
        cedula_cliente = self.txtCedulaCli.get().strip()
        mesa = self.txtMesa.get().strip()
        platos_str = self.txtPlatos.get().strip()
        precio_total = self.txtPrecioTo.get().strip()

        # Validaciones básicas
        if not id_comanda:
            messagebox.showerror("Error", "El ID de la comanda es obligatorio.")
            return
        if not id_comanda.isdigit():
            messagebox.showerror("Error", "El ID de la comanda debe ser numérico.")
            return
        if not cedula_cliente:
            messagebox.showerror("Error", "La cédula del cliente es obligatoria.")
            return
        if not mesa:
            messagebox.showerror("Error", "El número de mesa es obligatorio.")
            return
        if not platos_str:
            messagebox.showerror("Error", "Debe ingresar al menos un plato.")
            return
        if not precio_total:
            messagebox.showerror("Error", "Debe calcular el precio total.")
            return
        id_comanda = int(id_comanda)
        no_mesa = int(mesa)
        lista_platos = [int(id_plato) for id_plato in platos_str.split('-')]
        self.Usuario.tomarComanda(id_comanda, cedula_cliente, no_mesa, lista_platos)
        self.limpiarcampos()

    def limpiarcampos(self):
        """
        Limpia todos los campos de entrada de la ventana.

        Acciones:
        - Reinicia los valores de los campos de texto.
        - Deshabilita los campos de texto que no deben ser editables por el usuario.
        """
        self.txtId.delete(0, tk.END)
        self.txtCedulaCli.delete(0, tk.END)
        self.txtMesa.delete(0, tk.END)
        self.txtPlatos.config(state='disabled')  
        self.txtPlatos.delete(0, tk.END)
        self.txtPrecioTo.config(state='normal')
        self.txtPrecioTo.delete(0, tk.END)
        self.txtPrecioTo.config(state='disabled')

    def mostrarAyuda(self, event):
        """
        Muestra un mensaje de ayuda con información sobre los atajos y cómo usar la ventana.

        Parámetros:
        - event: Evento que dispara la acción (como presionar "F1").
        """
        mensaje_ayuda = (
            "Atajos.\n\n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda - Tomar Comanda", mensaje_ayuda)

    def salir(self, event):
        """
        Cierra la ventana de la aplicación.

        Parámetros:
        - event: Evento que dispara la acción (como presionar "F2").
        """
        self.ventana.destroy()

    def __init__(self, Usuario):
        """
        Constructor de la clase. Configura la ventana y sus componentes gráficos.

        Parámetros:
        - Usuario: Objeto que contiene la lógica de negocio para gestionar clientes,
                   mesas, y platos.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Tomar Comanda")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
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

        self.txtCedulaCli = tk.Entry(self.ventana)  
        self.txtCedulaCli.place(relx=0.50, rely=0.34, anchor="center")

        self.txtMesa = tk.Entry(self.ventana) 
        self.txtMesa.place(relx=0.50, rely=0.45, anchor="center")

        self.txtPlatos = tk.Entry(self.ventana, state='disabled')  
        self.txtPlatos.place(relx=0.50, rely=0.56, anchor="center")

        self.txtPrecioTo = tk.Entry(self.ventana, state='disabled')  
        self.txtPrecioTo.place(relx=0.50, rely=0.68, anchor="center")

        # Combobox para el estado
        self.estado_var = tk.StringVar(value="Pendiente")
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Pendiente"],  state='disabled')
        self.cmbEstado.place(relx=0.50, rely=0.79, anchor="center")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.89, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.validar_cliente_mesa)
        Tooltip(self.btnBuscar, "Haga clic para buscar una comanda existente.")

        self.btnGuardar = tk.Button(self.ventana, image=self.iconoGuardar, text="Guardar", width=85, compound="left")
        self.btnGuardar.place(relx=0.65, rely=0.89, anchor="center")
        self.btnGuardar.bind("<Button-1>", self.calcular_precio_total)
        Tooltip(self.btnGuardar, "Haga clic para guardar la información de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        # Atajos
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()

