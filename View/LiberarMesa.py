import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class LiberarMesa():
    
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
                self.cmbEstado.insert(0, "Disponible")  
                
                self.estado_var.set(mesa[2]) 
                self.btnLiberar.config(state="normal")
                self.txtCantidadComensales.config(state="disabled")
                self.cmbEstado.config(state="normal")
                messagebox.showinfo("Información", f"Mesa con ID {id_mesa} encontrada.")
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
            "Atajos.\n\n"
            "- Presione 'F5' para buscar la mesa con el ID. \n"
            "- Presione 'F4' para cambiar el estado de la mesa. \n"
            "- Presione 'F3' para para limpiar los campos. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
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
        self.ventana.title("Liberar Mesa")
        self.ventana.configure(width=320, height=350)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        #iconos
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")
        self.iconoLiberar = tk.PhotoImage(file=r"Restaurante/Src/mesa.png")

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Liberar Mesa", font=("Times", 20, "bold"))
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
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Disponible"])
        self.cmbEstado.place(relx=0.50, rely=0.59, anchor="center")
        Tooltip(self.lblEstado, "Estado de la mesa: solo 'Disponible' para liberar.")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=self.iconoBuscar, width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.74, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnLiberar = tk.Button(self.ventana, text="Liberar", image=self.iconoLiberar, width=85, state="disabled", compound="left")
        self.btnLiberar.place(relx=0.66, rely=0.74, anchor="center")
        self.btnLiberar.bind("<Button-1>", self.cambiarEstado)
        Tooltip(self.btnLiberar, "liberar Mesa")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, width=185, compound="left")
        self.btnLimpiar.place(relx=0.5, rely=0.81, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, text="Salir", image=self.iconoSalir, width=185, compound="left")
        self.btnSalir.place(relx=0.5, rely=0.88, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de liberación de mesas")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        # Atajo
        self.ventana.bind("<F5>", self.buscarMesa)
        self.ventana.bind("<F4>", self.cambiarEstado)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()