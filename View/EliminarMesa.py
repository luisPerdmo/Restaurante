__author__ = "Luis Perdomo"
__copyright__ = "Copyright 2022, CAPS"
__credits__ = ["LDM", "Luis Perdomo", "Otros"]
__license__ = "GPL"
__version__ = "0.70.10000"
__maintainer__ = "Equipo LDM"
__email__ = "luis.perdomo@correounivalle.edu.co"
__status__ = "Pruebas"

import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarMesa:

    def mostrarAyuda(self, event):
        """
        Muestra un mensaje de ayuda con los atajos disponibles.
        """
        mensaje_Ayuda = (
            "Atajos.\n\n"
            "- Presione 'F5' para buscar la mesa por el ID . \n"
            "- Presione 'F4' para eliminar mesa. \n"
            "- presione 'F3' para limpiar los campos. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def limpiarCampos(self, event):
        """
        Limpia los campos del formulario, incluyendo el estado y la cantidad de comensales.
        """
        self.txtEstado.config(state="normal")
        self.txtCantidadComensales.config(state="normal")
        self.txtIdMesa.delete(0, tk.END)
        self.txtCantidadComensales.delete(0, tk.END)
        self.txtEstado.delete(0, tk.END)
        self.txtCantidadComensales.config(bg="#ffffff")
        self.txtEstado.config(bg="#ffffff")
        self.txtEstado.config(state="disabled")
        self.txtCantidadComensales.config(state="disabled")

    def buscarMesa(self, event):
        """
        Busca una mesa por su ID. Si la encuentra, muestra los detalles de la mesa (cantidad de comensales y estado).
        """
        if not self.txtIdMesa.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la mesa.")
            return
        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID de Mesa' solo puede contener números.")
            return
        id_mesa = int(self.txtIdMesa.get())
        try:
            mesa = self.obtenerMesa(id_mesa)
            if mesa: 
                self.txtCantidadComensales.config(state="normal")
                self.txtEstado.config(state="normal")
                self.txtCantidadComensales.delete(0, tk.END)
                self.txtCantidadComensales.insert(0, mesa[1]) 
                self.txtEstado.delete(0, tk.END)
                self.txtEstado.insert(0, mesa[2])  
                self.txtCantidadComensales.config(state="disabled")
                self.txtEstado.config(state="disabled")
                messagebox.showinfo("Información", f"Mesa {id_mesa} encontrada. Estado: {mesa[2]}")
                if mesa[2] == "Disponible":  
                    self.btnEliminar.config(state="normal")
                else:
                    self.btnEliminar.config(state="disabled") 
            else:
                messagebox.showinfo("Información", f"Mesa {id_mesa} no encontrada.")
                self.btnEliminar.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar la mesa. Detalles: {e}")
            self.btnEliminar.config(state="disabled")

    def obtenerMesa(self, id_mesa):
        """
        Obtiene los detalles de la mesa a través de la clase `usuario`.
        """
        return self.usuario.buscarMesa(id_mesa)

    def eliminarMesa(self, event):
        """
        Elimina una mesa si está disponible. Si la mesa está ocupada, no puede ser eliminada.
        """
        if not self.txtIdMesa.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la mesa.")
            return
        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID de Mesa' solo puede contener números.")
            return
        id_mesa = int(self.txtIdMesa.get())
        try:
            mesa = self.obtenerMesa(id_mesa)
            if mesa:
                if mesa[2] == "Ocupada": 
                    messagebox.showwarning("Advertencia", "No se puede eliminar la mesa porque está ocupada.")
                else:
                    self.usuario.eliminarMesa(id_mesa)
                    messagebox.showinfo("Confirmación", f"Mesa {id_mesa} eliminada con éxito.")
                    self.limpiarCampos(event)
            else:
                messagebox.showinfo("Información", f"Mesa {id_mesa} no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la mesa. Detalles: {e}")

    def salir(self, event):
        """
        Cierra la ventana de eliminación de mesa.
        """
        self.ventana.destroy()

    def soloNumeros(self, event):
        """
        Permite solo la entrada de números en los campos de ID de mesa.
        """
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        """
        Inicializa la ventana de la clase `EliminarMesa`, configura los widgets y acciones.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Eliminar Mesa")
        self.ventana.configure(width=320, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        #iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Restaurante/Src/eliminarMesa.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Mesa", font=("Times", 20, "bold"))
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

        self.txtEstado = tk.Entry(self.ventana)
        self.txtEstado.place(relx=0.50, rely=0.59, anchor="center")
        self.txtEstado.config(state="disabled")
        Tooltip(self.txtEstado, "El estado de la mesa se muestra tras buscarla.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=self.iconoBuscar, width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.74, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", image=self.iconoEliminar, width=85, state="disabled", compound="left")
        self.btnEliminar.place(relx=0.66, rely=0.74, anchor="center")
        self.btnEliminar.bind("<Button-1>", self.eliminarMesa)
        Tooltip(self.btnEliminar, "Eliminar mesa")

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

        # Atajo
        self.ventana.bind("<F5>", self.buscarMesa)
        self.ventana.bind("<F4>", self.eliminarMesa)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
