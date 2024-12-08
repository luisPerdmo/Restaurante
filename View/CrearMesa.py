import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearMesa:

    def limpiarCampos(self, event):
        self.txtIdMesa.delete(0, tk.END)
        self.txtCantidadComensales.delete(0, tk.END)
        self.txtIdMesa.config(bg="#ffffff")
        self.txtCantidadComensales.config(bg="#ffffff")

    def guardarMesa(self, event):
        if not self.txtIdMesa.get() or not self.txtCantidadComensales.get():
            messagebox.showerror("Error", "Por favor ingrese todos los valores en los campos obligatorios.")
            return
        
        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID de Mesa' solo puede contener números.")
            return
        
        if not self.txtCantidadComensales.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cantidad de Comensales' solo puede contener números.")
            return
        
        estado = "Disponible"

        try:
            # Verificar si la mesa ya existe antes de crearla
            if self.usuario.existeMesa(self.txtIdMesa.get()):
                messagebox.showerror("Error", f"La ID '{self.txtIdMesa.get()}' ya está registrada.")
                return

            # Llamar a la función de creación de la mesa en la base de datos
            self.usuario.crearMesa(self.txtIdMesa.get(), self.txtCantidadComensales.get(), estado)
            messagebox.showinfo("Confirmación", "Mesa registrada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la mesa. Detalles: {e}")

    def salir(self, event):
        self.ventana.destroy()

    def mostrarAyuda(self, event):
        mensaje = (
            "Formulario para crear mesas:\n\n"
            "1. Complete todos los campos obligatorios marcados con *.\n"
            "2. Pulse 'Registrar' para guardar los datos ingresados.\n"
            "3. Pulse 'Limpiar' para borrar los datos ingresados en los campos.\n"
            "4. Pulse 'Salir' para cerrar la ventana de creación de mesas.\n\n"
            "Notas adicionales:\n"
            "- El campo 'ID de Mesa' solo acepta números.\n"
            "- El campo 'Cantidad de Comensales' solo acepta números."
        )
        messagebox.showinfo("Ayuda", mensaje)

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Crear Mesa")
        self.ventana.configure(width=320, height=300)
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()

        self.usuario = usuario

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Crear Mesa", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor="center")

        # Textos
        self.lblIdMesa = tk.Label(self.ventana, text="ID de Mesa*: ")
        self.lblIdMesa.place(relx=0.3, rely=0.3, anchor="center")

        self.lblCantidadComensales = tk.Label(self.ventana, text="Cantidad Comensales*: ")
        self.lblCantidadComensales.place(relx=0.35, rely=0.5, anchor="center")

        # Campos de texto
        self.txtIdMesa = tk.Entry(self.ventana)
        self.txtIdMesa.place(relx=0.6, rely=0.3, anchor="center")
        self.txtIdMesa.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtIdMesa, "Ingrese el ID de la mesa. Solo se permiten números.")

        self.txtCantidadComensales = tk.Entry(self.ventana)
        self.txtCantidadComensales.place(relx=0.6, rely=0.5, anchor="center")
        self.txtCantidadComensales.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCantidadComensales, "Ingrese la cantidad de comensales. Solo se permiten números.")

        # Botones
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", width=10)
        self.btnRegistrar.place(relx=0.3, rely=0.7, anchor="center")
        self.btnRegistrar.bind("<Button-1>", self.guardarMesa)
        Tooltip(self.btnRegistrar, "Registrar una nueva mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", width=10)
        self.btnLimpiar.place(relx=0.7, rely=0.7, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=15)
        self.btnSalir.place(relx=0.5, rely=0.85, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de creación de mesas")
        
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante\Src\ayuda.png")
        self.btnAyuda = tk.Label(self.ventana,image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.9, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()
