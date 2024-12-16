import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class ConsultarMesa():
    """
    Esta clase crea una interfaz gráfica para consultar el estado de una mesa en un restaurante.
    La interfaz permite buscar una mesa por su ID, mostrar la cantidad de comensales y su estado.
    También proporciona funcionalidad para limpiar los campos, salir de la ventana y acceder a la ayuda.
    """

    def buscarMesa(self, event):
        """
        Busca una mesa por su ID introducido por el usuario. Si la mesa existe, muestra la cantidad de 
        comensales y su estado. Si no se encuentra la mesa o el ID no es válido, muestra un mensaje de error.
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
                if mesa[2] in ["Disponible", "Ocupada"]:
                    messagebox.showinfo("Información", f"Mesa {id_mesa} encontrada. Estado: {mesa[2]}")
            else:
                messagebox.showinfo("Información", f"Mesa {id_mesa} no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar la mesa. Detalles: {e}")

    def obtenerMesa(self, id_mesa):
        """
        Llama al método de usuario para buscar la mesa en la base de datos o en la fuente de datos.
        """
        return self.usuario.buscarMesa(id_mesa)

    def mostrarAyuda(self, event):
        """
        Muestra un cuadro de mensaje con los atajos de teclado disponibles en la ventana.
        """
        mensaje_Ayuda = ( 
               "Atajos.\n\n"
               "- Presione 'F4' para buscar la mesa con el ID. \n"
               "- presione 'F3' para limpiar los campos. \n"
               "- presione 'F2' para cerrar la ventana. \n"
               "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", mensaje_Ayuda)

    def limpiarCampos(self, event):
        """
        Limpia todos los campos de texto y restablece su estado a los valores iniciales.
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

    def salir(self, event):
        """
        Cierra la ventana de la aplicación.
        """
        self.ventana.destroy()

    def soloNumeros(self, event):
        """
        Permite ingresar solo números en el campo de texto del ID de mesa.
        Si se ingresa una letra, cambia el color de fondo del campo para mostrar un error visual.
        """
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")

    def __init__(self, usuario):
        """
        Inicializa la ventana y los elementos gráficos de la interfaz, incluyendo botones, campos de texto, 
        etiquetas y acciones asociadas. También configura atajos de teclado.
        """
        self.ventana = tk.Toplevel()
        self.ventana.title("Consultar Mesa")
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
        self.lblTitulo = tk.Label(self.ventana, text="Consultar Mesa", font=("Times", 20, "bold"))
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
        self.btnBuscar.place(relx=0.34, rely=0.79, anchor="center")
        self.btnBuscar.bind("<Button-1>", self.buscarMesa)
        Tooltip(self.btnBuscar, "Buscar mesa por ID")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, width=85, compound="left")
        self.btnLimpiar.place(relx=0.66, rely=0.79, anchor="center")
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
        self.ventana.bind("<F4>", self.buscarMesa)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()