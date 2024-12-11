import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class OcuparMesa():
    
    def cambiarEstado(self, event):
        if not self.txtIdMesa.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la mesa.")
            return

        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID de Mesa' solo puede contener números.")
            return

        id_mesa = int(self.txtIdMesa.get())
        nuevo_estado = self.estado_var.get()

        if not nuevo_estado:
            messagebox.showerror("Error", "Por favor seleccione un estado para la mesa.")
            return

        self.cambiarestadocomanda(id_mesa, nuevo_estado)
        messagebox.showinfo("Información", f"Se cambió el estado de la mesa a {nuevo_estado}")

    def buscarMesa(self, event):
        if not self.txtIdMesa.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la mesa.")
            return 
        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID' solo puede contener números.")
            return
        id_mesa = int(self.txtIdMesa.get())
        try:
            mesa = self.obtenerMesa(id_mesa)
            if mesa:
                self.txtCantidadComensales.config(state="normal")
                self.txtCantidadComensales.delete(0, tk.END)
                self.txtCantidadComensales.insert(0, mesa[1])  
                
                self.cmbEstado.config(state="normal")
                self.cmbEstado.delete(0, tk.END)
                self.cmbEstado.insert(0, mesa[2])  
                
                self.estado_var.set(mesa[2])
                self.btnOcupar.config(state="normal")
                self.txtCantidadComensales.config(state="normal")
                self.cmbEstado.config(state="disabled")
                messagebox.showinfo("Información", f"Mesa con ID {id_mesa} encontrada.")
                self.cmbEstado.config(state="normal")
            else:
                messagebox.showinfo("Información", f"Mesa con ID {id_mesa} no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la mesa. Detalles: {e}")

    def obtenerMesa(self, id_mesa):
        return self.Usuario.buscarMesa(id_mesa)
    
    def cambiarestadocomanda(self, id_mesa, nuevo_estado):
        return self.Usuario.cambiarMesaEstado(id_mesa, nuevo_estado)

    def limpiarCampos(self, event):
        self.cmbEstado.config(state="normal")
        self.txtCantidadComensales.config(state="normal")
        self.txtIdMesa.delete(0, tk.END)
        self.txtCantidadComensales.delete(0, tk.END)
        self.cmbEstado.delete(0, tk.END)
        self.txtCantidadComensales.config(bg="#ffffff")
        self.cmbEstado.config(bg="#ffffff")
        self.cmbEstado.config(state="disabled")
        self.txtCantidadComensales.config(state="disabled")

    def mostrarAyuda(self, event):
        mensaje_ayuda = (
            "Ayuda:\n\n"
            "1. ID de Mesa: Ingrese el número de identificación de la mesa que desea consultar.\n"
            "2. Buscar: Al presionar este botón, se busca la mesa con el ID proporcionado.\n"
            "3. Ocupar: Si la mesa está disponible, este botón la ocupará.\n"
            "4. Limpiar: Limpia los campos para una nueva consulta.\n"
            "5. Salir: Cierra la ventana de consulta de mesa.\n"
            "6. Estado: El estado de la mesa (disponible, ocupada, etc.) se muestra tras realizar la búsqueda.\n"
            "7. Cantidad Comensales: Se muestra el número de comensales para la mesa seleccionada."
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def salir(self, event):
        self.ventana.destroy()

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")
    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Ocupar Mesa")
        self.ventana.configure(width=320, height=350)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        #iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")
        self.iconoOcupar = tk.PhotoImage(file=r"Restaurante/Src/mesa.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Ocupar Mesa", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.11, anchor="center")

        # Etiquetas
        self.lblIdMesa = tk.Label(self.ventana, text="ID de Mesa*: ")
        self.lblIdMesa.place(relx=0.36, rely=0.27, anchor="center")

        self.lblCantidadComensales = tk.Label(self.ventana, text="Cantidad Comensales: ")
        self.lblCantidadComensales.place(relx=0.45, rely=0.40, anchor="center")

        self.lblEstado = tk.Label(self.ventana, text="Estado: ")
        self.lblEstado.place(relx=0.32, rely=0.53, anchor="center")

        # Campos de texto
        self.txtIdMesa = tk.Entry(self.ventana)
        self.txtIdMesa.place(relx=0.50, rely=0.33, anchor="center")
        self.txtIdMesa.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtIdMesa, "Ingrese el ID de la mesa. Solo se permiten números.")

        self.txtCantidadComensales = tk.Entry(self.ventana)
        self.txtCantidadComensales.place(relx=0.50, rely=0.46, anchor="center")
        self.txtCantidadComensales.config(state="disabled")
        Tooltip(self.txtCantidadComensales, "La cantidad de comensales se muestra tras buscar la mesa.")

        self.estado_var = tk.StringVar()
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Ocupada"])
        self.cmbEstado.place(relx=0.50, rely=0.59, anchor="center")
        Tooltip(self.lblEstado, "Seleccione el estado de la mesa.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=self.iconoBuscar, width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.74, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnOcupar = tk.Button(self.ventana, text="Ocupar", image=self.iconoOcupar, width=85, state="disabled", compound="left")
        self.btnOcupar.place(relx=0.66, rely=0.74, anchor="center")
        self.btnOcupar.bind("<Button-1>", self.cambiarEstado)
        Tooltip(self.btnOcupar, "Eliminar mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, width=185, compound="left")
        self.btnLimpiar.place(relx=0.5, rely=0.81, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", image=self.iconoSalir, width=185, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.88, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de eliminación de mesas")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()
