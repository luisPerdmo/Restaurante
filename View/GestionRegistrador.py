import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip
from View.CrearChef import CrearChef
from View.EliminarChef import EliminarChef
from View.CrearMesa import CrearMesa  
from View.EliminarMesa import EliminarMesa
from View.CrearMesero import CrearMesero
from View.EliminarMesero import EliminarMesero
from View.InformeDiario import InformeDiario
from View.Calculartotal import Calculartotal

class GestionRegistrador():
    """
    Clase que gestiona la ventana del Registrador en el sistema.
    Permite la creación y eliminación de chefs, mesas, meseros, y generar informes de comanda.
    """

    def mostrarAyuda(self, event):
        """
        Muestra un cuadro de mensaje con los atajos de teclado disponibles.
        """
        mensaje_ayuda = (
            "Atajos.\n\n"
            "- presione 'F7' para crear el menu Chef.\n"
            "- presione 'F6' para crear el menu mesa.\n"
            "- presione 'F5' para crear el menu mesero.\n"
            "- presione 'F4' para crear el menu salir.\n"
            "- presione 'F3' para crear el menu comanda.\n"
            "- presione 'F2' para salir. \n"
            "- presione 'F1' para obtener ayuda.\n"
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def toggleBarra(self, event):
        """
        Expande o contrae la barra lateral dependiendo de su estado actual.
        """
        if self.barraExpandida:
            self.barra.configure(width=50)
            self.barraExpandida = False
            self.btnBarra.place(relx=0.51, rely=0.05, anchor="center")
            self.btnGestionChef.place_forget()
            self.btnGestionMesero.place_forget()
            self.btnGestionMesa.place_forget()  
            self.btnGestionComanda.place_forget()
            self.btnSalir.place_forget()
            self.lblMenu.place_forget()
        else:
            self.barra.configure(width=140)
            self.barraExpandida = True
            self.btnGestionChef.place(relx=0.01, rely=0.2, anchor="w")
            self.btnGestionMesero.place(relx=0.01, rely=0.3, anchor="w")
            self.btnGestionMesa.place(relx=0.01, rely=0.4, anchor="w")
            self.btnGestionComanda.place(relx=0.01, rely=0.5, anchor="w")
            self.btnSalir.place(relx=0.01, rely=0.6, anchor="w")
            self.btnBarra.place(relx=0.89, rely=0.05, anchor="center")
            self.lblMenu = tk.Label(self.barra, text="Menu", bg="#CCD1D1", font=("Times", 20, "bold"))
            self.lblMenu.place(relx=0.43, rely=0.05, anchor="center")
    
    # Funciones chef
    def crearMenuChef(self, event):
        """
        Crea y muestra el menú para gestionar chefs (registrar o eliminar).
        """
        if self.barraExpandida:
            self.menuChef = tk.Menu(self.ventana)
            self.menuChef.add_command(label="Registrar Chef", command=self.agregarChef)
            self.menuChef.add_separator()
            self.menuChef.add_command(label="Eliminar Chef", command=self.eliminarChef)
            self.menuChef.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 40)

    def agregarChef(self): 
        """
        Abre la ventana para registrar un nuevo chef.
        """ 
        CrearChef(self.usuario)

    def eliminarChef(self): 
        """
        Abre la ventana para eliminar un chef existente.
        """ 
        EliminarChef(self.usuario)

    # Función para mesas
    def crearMenuMesa(self, event):
        """
        Crea y muestra el menú para gestionar mesas (registrar o eliminar).
        """
        if self.barraExpandida:
            self.menuMesa = tk.Menu(self.ventana)
            self.menuMesa.add_command(label="Registrar Mesa", command=self.agregarMesa)
            self.menuMesa.add_separator()
            self.menuMesa.add_command(label="Eliminar Mesa", command=self.eliminarMesa)
            self.menuMesa.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 110)

    def agregarMesa(self):
        """
        Abre la ventana para registrar una nueva mesa.
        """
        CrearMesa(self.usuario)  

    def eliminarMesa(self):
        """
        Abre la ventana para eliminar una mesa existente.
        """
        EliminarMesa(self.usuario)

    #Mesero
    def crearMenuMesero(self, event):
        """
        Crea y muestra el menú para gestionar meseros (registrar o eliminar).
        """
        if self.barraExpandida:
            self.menuMesero = tk.Menu(self.ventana)
            self.menuMesero.add_command(label="Registrar Mesero", command=self.agregarMesero)
            self.menuMesero.add_separator()
            self.menuMesero.add_command(label="Eliminar Mesero", command=self.eliminarMesero)
            self.menuMesero.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 80)

    def agregarMesero(self): 
        """
        Abre la ventana para registrar un nuevo mesero.
        """
        CrearMesero(self.usuario)
        

    def eliminarMesero(self): 
        """
        Abre la ventana para eliminar un mesero existente.
        """
        EliminarMesero(self.usuario)

    #Comanda
    def crearMenuComada(self, event):
        """
        Crea y muestra el menú para gestionar comandas (generar informes y calcular precio total).
        """
        if self.barraExpandida:
            self.menuComada = tk.Menu(self.ventana, tearoff=0)
            self.menuComada.add_command(label="Crear informe diario", command=self.informeDiario)
            self.menuComada.add_separator()
            self.menuComada.add_command(label="Calcular precio total", command=self.precioTotal)
            self.menuComada.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 150)
       
    def informeDiario(self):
        """
        Abre la ventana para generar el informe diario de las comandas.
        """
        InformeDiario(self.usuario)

    def precioTotal(self):
        """
        Abre la ventana para calcular el precio total de las comandas.
        """
        Calculartotal(self.usuario)

    #Salir
    def crearMenuSalir(self, event):
        """
        Crea y muestra el menú para salir de la ventana.
        """
        if self.barraExpandida:
            self.menuSalir = tk.Menu(self.ventana, tearoff=0)
            self.menuSalir.add_command(label="Salir", command=self.salir)
            self.menuSalir.add_separator()
            self.menuSalir.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 198)
    
    def salir(self, event):
        """
        Cierra la ventana actual.
        """
        self.ventana.destroy()

    def __init__(self, loggin, usuario):
        """
        Inicializa la ventana del Registrador y establece la configuración inicial.
        """
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion de Registrador")
        self.ventana.configure(width=530, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        # Mensaje de bienvenida
        self.lblBienvenida = tk.Label(self.ventana, text=f"Bienvenido Registrador \n{self.usuario.nombre}", font=("Times", 18, "bold"), fg="black")
        self.lblBienvenida.place(relx=0.5, rely=0.4, anchor="center")

        # Variable para saber si la barra está expandida
        self.barraExpandida = False

        # Iconos
        self.iconoBarra = tk.PhotoImage(file=r"Restaurante/Src/barra.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante/Src/ayuda.png")

        # Barra lateral
        self.barra = tk.Frame(self.ventana, width=50, height=348, bg="#CCD1D1")
        self.barra.place(relx=0.00, rely=0.5, anchor="w")

        # Botones
        self.btnBarra = tk.Label(self.barra, image=self.iconoBarra)
        self.btnBarra.place(relx=0.51, rely=0.05, anchor="center")
        self.btnBarra.bind("<Button-1>", self.toggleBarra)
        Tooltip(self.btnBarra, "Expandir o contraer el menú")

        self.btnGestionChef = tk.Label(self.barra, text="Gestionar Chef", bg="#CCD1D1")
        self.btnGestionChef.place(relx=0.01, rely=0.1, anchor="w")
        self.btnGestionChef.place_forget()
        self.btnGestionChef.bind("<Button-1>", self.crearMenuChef)
        Tooltip(self.btnGestionChef, "Registrar o eliminar un chef")

        self.btnGestionMesero = tk.Label(self.barra, text="Gestionar Mesero", bg="#CCD1D1")
        self.btnGestionMesero.place(relx=0.01, rely=0.3, anchor="w")
        self.btnGestionMesero.place_forget()
        self.btnGestionMesero.bind("<Button-1>", self.crearMenuMesero)
        Tooltip(self.btnGestionMesero, "Registrar o eliminar un mesero")

        self.btnGestionMesa = tk.Label(self.barra, text="Gestionar Mesa", bg="#CCD1D1")
        self.btnGestionMesa.place(relx=0.01, rely=0.4, anchor="w")
        self.btnGestionMesa.place_forget()
        self.btnGestionMesa.bind("<Button-1>", self.crearMenuMesa)
        Tooltip(self.btnGestionMesa, "Registrar o eliminar una mesa")

        self.btnGestionComanda = tk.Label(self.barra, text="Gestionar Comandas", bg="#CCD1D1")
        self.btnGestionComanda.place(relx=0.01, rely=0.5, anchor="w")
        self.btnGestionComanda.place_forget()
        self.btnGestionComanda.bind("<Button-1>", self.crearMenuComada)
        Tooltip(self.btnGestionComanda, "Gestionar comandas y generar informes")

        self.btnSalir = tk.Label(self.barra, text="Salir", bg="#CCD1D1")
        self.btnSalir.place(relx=0.01, rely=0.6, anchor="w")
        self.btnSalir.place_forget()
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Presione para salir de la ventana")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.95, rely=0.05, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre la ventana")

        # Atajos
        self.ventana.bind("<F7>", self.crearMenuChef)
        self.ventana.bind("<F6>", self.crearMenuMesa)
        self.ventana.bind("<F5>", self.crearMenuMesero)
        self.ventana.bind("<F4>", self.crearMenuSalir)
        self.ventana.bind("<F3>", self.crearMenuComada)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)

        self.ventana.mainloop()
