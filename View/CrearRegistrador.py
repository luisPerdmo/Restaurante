import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearRegistrador():

    def limpiarCampos(self, event):
        self.txtNombres.delete(0, tk.END)
        self.txtApellido.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtCedula.delete(0, tk.END)
        self.txtPassword.delete(0, tk.END)
        self.txtNombres.config(bg="#ffffff")
        self.txtApellido.config(bg="#ffffff")
        self.txtEmail.config(bg="#ffffff")
        self.txtCedula.config(bg="#ffffff")
        self.txtPassword.config(bg="#ffffff")

    def guardarRegistrador(self, event):
        if not self.txtNombres.get() or not self.txtApellido.get() or not self.txtEmail.get() or not self.txtCedula.get() or not self.txtPassword.get():
            messagebox.showerror("Error", "Por favor ingrese todos los valores en los campos obligatorios.")
            return 
        for campo, nombreCampo in [(self.txtNombres.get(), "Nombres"), (self.txtApellido.get(), "Apellido")]:
            if not campo.replace(" ", "").isalpha():
                messagebox.showerror("Error", f"El campo '{nombreCampo}' solo puede contener letras.")
                return
        if not self.txtCedula.get().isdigit():
            messagebox.showerror("Error", "El campo 'Cedula' solo puede contener números.")
            return
        rol = "Registrador"
        if self.Usuario.existeUsuario(self.txtCedula.get()):  
            messagebox.showerror("Error", f"La cédula '{self.txtCedula.get()}' ya está registrada.")
            return
        self.Usuario.crearRegistrador(self.txtNombres.get(), self.txtApellido.get(), self.txtEmail.get(), self.txtCedula.get(), self.txtPassword.get(), rol)
        messagebox.showinfo("Confirmación", "Nuevo Registrador registrado con éxito.")

    def salir(self, event):
        self.ventana.destroy()

    def mostrarAyuda(self, event):
            mensaje = (
                "Formulario de registro de usuarios:\n\n"
                "1. Complete todos los campos obligatorios marcados con *.\n"
                "2. Pulse 'Registrar' para guardar los datos ingresados.\n"
                "3. Pulse 'Limpiar' para borrar los datos ingresados en los campos.\n"
                "4. Pulse 'Salir' para cerrar la ventana de registro.\n\n"
                "Notas adicionales:\n"
                "- Los campos de 'Nombres' y 'Apellido' solo aceptan letras.\n"
                "- El campo 'Cedula' solo acepta números.\n"
                "- El campo 'Email' debe tener un formato válido.\n"
                "- La contraseña debe ser segura y contener al menos 8 caracteres."
            )
            messagebox.showinfo("Ayuda", mensaje)

    def soloNumeros(self, event):
        numeros = event.keysym
        if numeros.isalpha(): 
            self.txtCedula.config(bg="#F8D7DA", fg="#000000")
        else:
            self.txtCedula.config(bg="#ffffff", fg="#000000")
        
    def soloLetras(self, event):
        letras = event.keysym
        if event.widget == self.txtNombres:
            if letras.isdigit() or letras == "BackSpace":
                self.txtNombres.config(bg="#F8D7DA", fg="#000000")
            else:
                self.txtNombres.config(bg="#ffffff", fg="#000000")
        elif event.widget == self.txtApellido:
            if letras.isdigit() or letras == "BackSpace":
                self.txtApellido.config(bg="#F8D7DA", fg="#000000")
            else:
                self.txtApellido.config(bg="#ffffff", fg="#000000")

    def __init__(self, Usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro de Usuarios")
        self.ventana.configure(width=320, height=390)
        self.ventana.resizable(0,0)

        self.Usuario = Usuario

        #Iconos
        self.iconoRegistrar = tk.PhotoImage(file=r"Restaurante/Src/registrar.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"Restaurante/Src/limpiar.png")
        self.iconoSalir = tk.PhotoImage(file=r"Restaurante/Src/salir.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        #Titulo
        self.lblTitulo = tk.Label(self.ventana, text="Registrarse", font=("Times", 20, "bold"))
        self.lblTitulo.place(relx=0.5, rely=0.08, anchor="center")

        #Textos
        self.lblNombres = tk.Label(self.ventana, text="Nombres*:")
        self.lblNombres.place(relx=0.34, rely=0.19, anchor="center")

        self.lblApellido = tk.Label(self.ventana, text="Apellido*:")
        self.lblApellido.place(relx=0.32, rely=0.31, anchor="center")

        self.lblEmail = tk.Label(self.ventana, text="Email*:")
        self.lblEmail.place(relx=0.30, rely=0.44, anchor="center")

        self.lblCedula = tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(relx=0.32, rely=0.57, anchor="center")

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(relx=0.35, rely=0.70, anchor="center")

        #Campos de textos
        self.txtNombres = tk.Entry(self.ventana)
        self.txtNombres.place(relx=0.50, rely=0.24, anchor="center")
        self.txtNombres.bind("<KeyPress>", self.soloLetras)
        Tooltip(self.txtNombres, "Ingrese su nombre. Solo se permiten letras.")

        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.place(relx=0.50, rely=0.37, anchor="center")
        self.txtApellido.bind("<KeyPress>", self.soloLetras)
        Tooltip(self.txtApellido, "Ingrese su apellido. Solo se permiten letras.")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.50, rely=0.50, anchor="center")
        Tooltip(self.txtEmail, "Ingrese un correo electrónico válido en formato usuario@dominio.com.")

        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.50, rely=0.63, anchor="center")
        self.txtCedula.bind("<KeyPress>", self.soloNumeros)
        Tooltip(self.txtCedula, "Ingrese su cédula. Solo se permiten números.")

        self.txtPassword = tk.Entry(self.ventana)
        self.txtPassword.place(relx=0.50, rely=0.76, anchor="center")
        Tooltip(self.txtPassword, "Ingrese una contraseña segura.")

        #Botones
        self.btnRegistart = tk.Button(self.ventana, image=self.iconoRegistrar, text="Registrar", width=85, compound="left")
        self.btnRegistart.place(relx=0.34, rely=0.87, anchor="center")
        self.btnRegistart.bind("<Button-1>", self.guardarRegistrador)
        Tooltip(self.btnRegistart, "Registrar un nuevo usuario")

        self.btnLimpiar = tk.Button(self.ventana, image=self.iconoLimpiar, text="Limpiar", width=85, compound="left")
        self.btnLimpiar.place(relx=0.65, rely=0.87, anchor="center")
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, "Limpiar los campos del formulario")

        self.btnSalir = tk.Button(self.ventana, image=self.iconoSalir, text="Salir", width=185, compound="left")
        self.btnSalir.place(relx=0.49, rely=0.93, anchor="center")
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Cerrar la ventana de registro")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.90, rely=0.07, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre el formulario")

        self.ventana.mainloop()