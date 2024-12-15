import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearMesa():

    def mostrarAyuda(self, event):
        mensaje_Ayuda = (
               "Atajos.\n\n"
               "- Presione 'F4' para registrar un nuevo usuario. \n"
               "- presione 'F3' para limpiar los campos. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n" 
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

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
            if self.usuario.existeMesa(self.txtIdMesa.get()):
                messagebox.showerror("Error", f"La ID '{self.txtIdMesa.get()}' ya está registrada.")
                return
            self.usuario.crearMesa(self.txtIdMesa.get(), self.txtCantidadComensales.get(), estado)
            messagebox.showinfo("Confirmación", "Mesa registrada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la mesa. Detalles: {e}")

    def salir(self, event):
        self.ventana.destroy()

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Crear Mesa")
        self.ventana.configure(width=320, height=270)
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()

        self.usuario = usuario

        #iconos
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoMesa = tk.PhotoImage(file=r"Restaurante/Src/mesa.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Crear Mesa", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.14, anchor="center")

        # Textos
        self.lblIdMesa = tk.Label(self.ventana, text="ID de Mesa*: ")
        self.lblIdMesa.place(relx=0.36, rely=0.3, anchor="center")

        self.lblCantidadComensales = tk.Label(self.ventana, text="Cantidad Comensales*: ")
        self.lblCantidadComensales.place(relx=0.46, rely=0.47, anchor="center")

        # Campos de texto
        self.txtIdMesa = tk.Entry(self.ventana)
        self.txtIdMesa.place(relx=0.50, rely=0.38, anchor="center")
        self.txtIdMesa.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtIdMesa, "Ingrese el ID de la mesa. Solo se permiten números.")

        self.txtCantidadComensales = tk.Entry(self.ventana)
        self.txtCantidadComensales.place(relx=0.50, rely=0.55, anchor="center")
        self.txtCantidadComensales.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCantidadComensales, "Ingrese la cantidad de comensales. Solo se permiten números.")

        # Botones
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", image=self.iconoMesa, width=85, compound="left")
        self.btnRegistrar.place(relx=0.34, rely=0.7, anchor="center")
        self.btnRegistrar.bind("<Button-1>", self.guardarMesa)
        Tooltip(self.btnRegistrar, "Registrar una nueva mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, width=85,  compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.7, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", image=self.iconoSalir, width=185, compound="left")
        self.btnSalir.place(relx=0.50, rely=0.80, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de creación de mesas")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        # Atajo
        self.ventana.bind("<F4>", self.guardarMesa)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
