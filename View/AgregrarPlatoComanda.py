import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class AgregarPlatoComanda():

    def agregarPlato(self, event):
        platos_str = self.txtPlatos.get().strip()
        if not platos_str:
            messagebox.showwarning("Advertencia", "No hay platos para agregar.")
            return
        try:
            lista_platos = [int(id_plato) for id_plato in platos_str.split('-')]
        except ValueError:
            messagebox.showerror("Error", "Los platos deben ser una lista de números separados por guiones (ej. 1-2-3).")
            return
        plato_a_agregar_str = self.txtPlatos.get().strip() 
        if not plato_a_agregar_str.isdigit():
            messagebox.showerror("Error", "El ID del plato a agregar debe ser numérico.")
            return

        plato_a_agregar = int(plato_a_agregar_str)
        if not self.Usuario.existePlato(plato_a_agregar):
            messagebox.showerror("Error", f"El plato con ID {plato_a_agregar} no existe.")
            return
        try:
            precio_total = self.Usuario.agregarPlatoAComanda(int(self.txtId.get()), plato_a_agregar)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        lista_platos.append(plato_a_agregar)
        platos_actualizados = '-'.join(map(str, lista_platos))
        self.txtPlatos.config(state='normal')
        self.txtPrecioTo.config(state='disabled')
        messagebox.showinfo("Éxito", f"Plato con ID {plato_a_agregar} agregado correctamente.")


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
               "Ayuda", 
               "Atajos.\n\n"
               "- Presione 'F4' para buscar la comanda existente. \n"
               "- presione 'F3' para agregar informacion a la comanda. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def salir(self, event):
        self.ventana.destroy()

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Agregar Plato Comanda")
        self.ventana.configure(width=320, height=410)
        self.ventana.resizable(0, 0)

        self.Usuario = Usuario

        # Iconos
        self.iconoGuardar = tk.PhotoImage(file=r"Restaurante/Src/plato.png")
        self.iconoBuscar = tk.PhotoImage(file=r"Restaurante/Src/buscar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Agrgear Plato Comanda", font=("Times", 20, "bold"))
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

        self.btnGuardar = tk.Button(self.ventana, image=self.iconoGuardar, text="Guardar", width=85, compound="left")
        self.btnGuardar.place(relx=0.65, rely=0.89, anchor="center")
        self.btnGuardar.bind("<Button-1>", self.agregarPlato)
        Tooltip(self.btnGuardar, "Haga clic para Agregar la información de la comanda.")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.95, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Haga clic para salir de la ventana.")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.93, rely=0.16, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Haga clic para obtener ayuda sobre cómo usar esta ventana.")

        # Atajo
        self.ventana.bind("<F4>", self.buscarComanda)
        self.ventana.bind("<F3>", self.agregarPlato)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()

