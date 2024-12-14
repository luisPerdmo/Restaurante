import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarPlatoComanda():

    def eliminarPlato(self, event):
        platos_str = self.txtPlatos.get().strip()
        if not platos_str:
            messagebox.showwarning("Advertencia", "No hay platos para eliminar.")
            return

        try:
            lista_platos = [int(id_plato) for id_plato in platos_str.split('-')]
        except ValueError:
            messagebox.showerror("Error", "Los platos deben ser una lista de números separados por guiones (ej. 1-2-3).")
            return

        plato_a_eliminar = self.txtPlatos.get().strip()  # Asegúrate de obtener el ID del plato a eliminar del campo correcto
        if not plato_a_eliminar.isdigit():
            messagebox.showerror("Error", "El ID del plato a eliminar debe ser numérico.")
            return

        plato_a_eliminar = int(plato_a_eliminar)
        if plato_a_eliminar not in lista_platos:
            messagebox.showerror("Error", f"El plato con ID {plato_a_eliminar} no está en la comanda.")
            return

        # Actualizar la comanda en la base de datos y obtener el nuevo precio total
        try:
            precio_total = self.Usuario.eliminarPlatoDeComanda(int(self.txtId.get()), plato_a_eliminar)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Remover el plato de la lista en la interfaz de usuario
        lista_platos.remove(plato_a_eliminar)
        platos_actualizados = '-'.join(map(str, lista_platos))
        self.txtPlatos.delete(0, tk.END)
        self.txtPlatos.insert(0, platos_actualizados)

        messagebox.showinfo("Éxito", f"Plato con ID {plato_a_eliminar} eliminado correctamente.")

    def buscarComanda(self, event):
        if not self.txtId.get():
            messagebox.showerror("Error", "Por favor ingrese el ID de la comanda.")
            return
        
        if not self.txtId.get().isdigit():
            messagebox.showerror("Error", "El campo 'ID' solo puede contener números.")
            return

        id_comanda = int(self.txtId.get())
        
        try:
            comanda = self.obtenerComanda(id_comanda)
            if comanda:
                self.txtCedulaCli.config(state="normal")
                self.txtCedulaCli.delete(0, tk.END)
                self.txtCedulaCli.insert(0, comanda[1])  
                
                self.txtMesa.config(state="normal")
                self.txtMesa.delete(0, tk.END)
                self.txtMesa.insert(0, comanda[2]) 
                
                self.txtPlatos.config(state="normal")
                self.txtPlatos.delete(0, tk.END)
                self.txtPlatos.insert(0, comanda[3])  
                
                self.estado_var.set("Pendiente")  
                
                self.cmbEstado.config(state="disabled")
                self.txtCedulaCli.config(state="disabled")
                self.txtMesa.config(state="disabled")
                self.txtPrecioTo.config(state="disabled")
                messagebox.showinfo("Información", f"Comanda con ID {id_comanda} encontrada.")
                #self.btnCambiar.config(state="normal") 
            else:
                messagebox.showinfo("Información", f"Comanda con ID {id_comanda} no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la comanda. Detalles: {e}")


    def obtenerComanda(self, id_comanda):
        return self.Usuario.buscarComanda(id_comanda)

    def mostrarAyuda(self, event):
        mensaje_ayuda = (
            "Ayuda:\n\n"
            "1. ID: Ingrese el número de ID de la comanda. Solo se permiten números.\n"
            "2. Cédula Cliente: Este campo se completará automáticamente al buscar una comanda.\n"
            "3. Mesa: Este campo se completará automáticamente al buscar una comanda.\n"
            "4. Platos: Este campo se completará automáticamente al buscar una comanda.\n"
            "5. Precio Total: Este campo se completará automáticamente al buscar una comanda.\n"
            "6. Estado: Elija el estado de la comanda entre 'en preparación' o 'servido'.\n"
            "7. Buscar: Haga clic en este botón para buscar una comanda por su ID.\n"
            "8. Cambiar: Haga clic en este botón para cambiar el estado de la comanda.\n"
            "9. Salir: Cierra la ventana de agregar plato a la comanda.\n"
            "10. Si desea agregar un nuevo plato a la comanda, complete los campos correspondientes y haga clic en 'Cambiar'."
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Eliminar Plato Comanda")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoEliminar = tk.PhotoImage(file=r"Restaurante/Src/eliminarMesa.png")
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Plato Comanda", font=("Times", 20, "bold"))
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
        self.estado_var = tk.StringVar(value="Pendiente")
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Pendiente"], state='disabled')
        self.cmbEstado.place(relx=0.50, rely=0.79, anchor="center")

        # Botones
        self.btnBuscar = tk.Button(self.ventana, image=self.iconoBuscar, text="Buscar", width=85, compound="left")
        self.btnBuscar.place(relx=0.34, rely=0.89, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarComanda)
        Tooltip(self.btnBuscar, "Haga clic para buscar una comanda existente.")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar, text="Eliminar", width=85, compound="left")
        self.btnEliminar.place(relx=0.65, rely=0.89, anchor="center")
        self.btnEliminar.bind("<Button-1>", self.eliminarPlato)
        Tooltip(self.btnEliminar, "Haga clic para Eliminar el plato de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        self.ventana.mainloop()

