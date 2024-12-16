import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tooltip import Tooltip

class OcuparMesa():
    """
    Clase para gestionar la ocupación de mesas en un restaurante.

    Permite buscar mesas por su ID, cambiar su estado a 'Ocupada',
    mostrar la cantidad de comensales y limpiar los campos de la interfaz.
    """
    
    def cambiarEstado(self, event):
        """
        Cambia el estado de una mesa al valor seleccionado en el combobox.

        Parámetros:
        - event: Evento que dispara la acción (como un clic en el botón "Ocupar").

        Validaciones:
        - Verifica que el ID de la mesa no esté vacío.
        - Asegura que el ID de la mesa sea numérico.
        - Valida que se haya seleccionado un nuevo estado para la mesa.

        Acciones:
        - Llama a la función `cambiarestadocomanda` para realizar el cambio.
        - Muestra mensajes informativos o de error según corresponda.
        """
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
        """
        Busca una mesa por su ID y muestra sus datos en los campos correspondientes.

        Parámetros:
        - event: Evento que dispara la acción (como un clic en el botón "Buscar").

        Validaciones:
        - Verifica que el ID de la mesa no esté vacío.
        - Asegura que el ID de la mesa sea numérico.

        Acciones:
        - Llama a la función `obtenerMesa` para buscar los datos de la mesa.
        - Muestra la cantidad de comensales y el estado de la mesa.
        - Habilita el botón para cambiar el estado si la mesa se encuentra.
        - Muestra mensajes informativos o de error según corresponda.
        """
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
                
                self.estado_var.set("Ocupada")
                self.btnOcupar.config(state="normal")
                self.txtCantidadComensales.config(state="disabled")
                self.cmbEstado.config(state="disabled")
                messagebox.showinfo("Información", f"Mesa con ID {id_mesa} encontrada.")
                self.cmbEstado.config(state="disabled")
            else:
                messagebox.showinfo("Información", f"Mesa con ID {id_mesa} no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la mesa. Detalles: {e}")

    def obtenerMesa(self, id_mesa):
        """
        Busca los datos de una mesa en el sistema.

        Parámetros:
        - id_mesa: ID de la mesa que se desea buscar.

        Retorna:
        - Una tupla con los datos de la mesa (si existe) o None si no se encuentra.
        """
        return self.Usuario.buscarMesa(id_mesa)
    
    def cambiarestadocomanda(self, id_mesa, nuevo_estado):
        """
        Cambia el estado de una mesa en el sistema.

        Parámetros:
        - id_mesa: ID de la mesa cuyo estado será cambiado.
        - nuevo_estado: Nuevo estado que se asignará a la mesa.

        Retorna:
        - Resultado de la operación realizada en el sistema.
        """
        return self.Usuario.cambiarMesaEstado(id_mesa, nuevo_estado)

    def limpiarCampos(self, event):
        """
        Limpia todos los campos de la interfaz gráfica.

        Acciones:
        - Reinicia los valores de los campos de texto y combobox.
        - Cambia el estado de los campos a deshabilitado.
        """
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
        """
        Muestra un mensaje con información sobre los atajos y cómo usar la ventana.

        Parámetros:
        - event: Evento que dispara la acción (como presionar "F1").
        """
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
        """
        Cierra la ventana de la aplicación.

        Parámetros:
        - event: Evento que dispara la acción (como presionar "F2").
        """
        self.ventana.destroy()

    def soloNumeros(self, event):
        """
        Cierra la ventana de la aplicación.

        Parámetros:
        - event: Evento que dispara la acción (como presionar "F2").
        """
        numeros = event.keysym
        if numeros.isalpha():
            event.widget.config(bg="#F8D7DA", fg="#000000")
        else:
            event.widget.config(bg="#ffffff", fg="#000000")
    def __init__(self, Usuario):
        """
        Constructor de la clase. Configura la ventana y sus componentes gráficos.

        Parámetros:
        - Usuario: Objeto que contiene la lógica de negocio para gestionar mesas.
        """
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

        self.txtCantidadComensales = tk.Entry(self.ventana, state="disabled")
        self.txtCantidadComensales.place(relx=0.50, rely=0.46, anchor="center")
        self.txtCantidadComensales.config(state="disabled")
        Tooltip(self.txtCantidadComensales, "La cantidad de comensales se muestra tras buscar la mesa.")

        self.estado_var = tk.StringVar()
        self.cmbEstado = ttk.Combobox(self.ventana, textvariable=self.estado_var, values=["Ocupada"], state="disabled")
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

        # Atajos
        self.ventana.bind("<F5>", self.buscarMesa)
        self.ventana.bind("<F4>", self.cambiarEstado)
        self.ventana.bind("<F3>", self.limpiarCampos)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
