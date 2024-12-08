import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarMesa:

    def limpiarCampos(self, event):
        self.txtIdMesa.delete(0, tk.END)
        self.txtCantidadComensales.delete(0, tk.END)
        self.txtCantidadComensales.config(bg="#ffffff")
        self.txtEstado.config(bg="#ffffff")
        self.txtEstado.config(state="disabled")

    def buscarMesa(self, event):
        if not self.txtIdMesa.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la mesa.")
            return

        if not self.txtIdMesa.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID de Mesa' solo puede contener números.")
            return

        id_mesa = int(self.txtIdMesa.get())
        try:
            mesa = self.obtenerMesa(id_mesa)
            if mesa:  # Verifica si la mesa existe y se encontró en la base de datos
                self.txtCantidadComensales.config(state="normal")
                self.txtEstado.config(state="normal")
                self.txtCantidadComensales.delete(0, tk.END)
                self.txtCantidadComensales.insert(0, mesa[1])  # Asumiendo que la cantidad de comensales está en la posición 1
                self.txtEstado.delete(0, tk.END)
                self.txtEstado.insert(0, mesa[2])  # Asumiendo que el estado está en la posición 2
                self.txtCantidadComensales.config(state="disabled")
                self.txtEstado.config(state="disabled")
                messagebox.showinfo("Información", f"Mesa {id_mesa} encontrada. Estado: {mesa[2]}")
                
                # Habilitar el botón de eliminar solo si la mesa está disponible
                if mesa[2] == "Disponible":  # Cambia esto según tu lógica de estado
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
        return self.usuario.buscarMesa(id_mesa)


    def eliminarMesa(self, event):
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
                # Accede a la tupla por índices numéricos
                if mesa[2] == "Ocupado":  # Asegúrate de usar el índice correcto
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
        self.ventana.destroy()

    def mostrarAyuda(self, event):
        mensaje = (
            "Formulario para eliminar mesas:\n\n"
            "1. Ingrese el ID de la mesa que desea buscar y eliminar.\n"
            "2. Pulse 'Buscar' para ver los detalles de la mesa.\n"
            "3. Si la mesa está en estado 'Ocupado', no se podrá eliminar.\n"
            "4. Pulse 'Eliminar' para eliminar la mesa si está disponible.\n"
            "5. Pulse 'Limpiar' para borrar los datos ingresados.\n"
            "6. Pulse 'Salir' para cerrar la ventana.\n\n"
            "Notas adicionales:\n"
            "- El campo 'ID de Mesa' solo acepta números."
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
        self.ventana.title("Eliminar Mesa")
        self.ventana.configure(width=320, height=300)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Mesa", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor="center")

        # Etiquetas
        self.lblIdMesa = tk.Label(self.ventana, text="ID de Mesa*: ")
        self.lblIdMesa.place(relx=0.3, rely=0.3, anchor="center")

        self.lblCantidadComensales = tk.Label(self.ventana, text="Cantidad Comensales: ")
        self.lblCantidadComensales.place(relx=0.35, rely=0.5, anchor="center")

        self.lblEstado = tk.Label(self.ventana, text="Estado: ")
        self.lblEstado.place(relx=0.35, rely=0.7, anchor="center")

        # Campos de texto
        self.txtIdMesa = tk.Entry(self.ventana)
        self.txtIdMesa.place(relx=0.6, rely=0.3, anchor="center")
        self.txtIdMesa.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtIdMesa, "Ingrese el ID de la mesa. Solo se permiten números.")

        self.txtCantidadComensales = tk.Entry(self.ventana)
        self.txtCantidadComensales.place(relx=0.6, rely=0.5, anchor="center")
        self.txtCantidadComensales.config(state="disabled")
        Tooltip(self.txtCantidadComensales, "La cantidad de comensales se muestra tras buscar la mesa.")

        self.txtEstado = tk.Entry(self.ventana)
        self.txtEstado.place(relx=0.6, rely=0.7, anchor="center")
        self.txtEstado.config(state="disabled")
        Tooltip(self.txtEstado, "El estado de la mesa se muestra tras buscarla.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", width=10)
        self.btnBuscar.place(relx=0.3, rely=0.85, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", width=10, state="disabled")
        self.btnEliminar.place(relx=0.7, rely=0.85, anchor="center")
        self.btnEliminar.bind("<Button-1>", self.eliminarMesa)
        Tooltip(self.btnEliminar, "Eliminar mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", width=10)
        self.btnLimpiar.place(relx=0.5, rely=0.95, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", width=15)
        self.btnSalir.place(relx=0.5, rely=1.0, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de eliminación de mesas")

        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante\Src\ayuda.png")
        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.9, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()
