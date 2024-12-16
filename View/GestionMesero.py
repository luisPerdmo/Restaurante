__author__ = "Luis Perdomo"
__copyright__ = "Copyright 2022, CAPS"
__credits__ = ["LDM", "Luis Perdomo", "Otros"]
__license__ = "GPL"
__version__ = "0.70.10000"
__maintainer__ = "Equipo LDM"
__email__ = "luis.perdomo@correounivalle.edu.co"
__status__ = "Pruebas"

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

from View.CrearCliente import CrearCliente
from View.EliminarCliente import EliminarCliente
from View.ConsultarMesa import ConsultarMesa
from View.OcuparMesa import OcuparMesa
from View.LiberarMesa import LiberarMesa
from View.AgregrarPlatoComanda import AgregarPlatoComanda
from View.TomarComanda import TomarComanda
from View.EliminarPlatoComando import EliminarPlatoComanda
from View.EnviarComanda import EnviarComanda

class GestionMesero():
    """Clase para gestionar la interfaz y la lógica del mesero"""
        
    def mostrarAyuda(self, event):
        mensaje_ayuda = ( 
            "Atajos.\n\n"
            "- presione 'F6' para crear el menu cliente.\n"
            "- presione 'F5' para crear el menu mesa.\n"
            "- presione 'F4' para crear el menu salir.\n"
            "- presione 'F3' para crear el menu comanda.\n"
            "- presione 'F2' para salir. \n"
            "- presione 'F1' para obtener ayuda.\n"
        )
        messagebox.showinfo("Ayuda", mensaje_ayuda)

    def toggleBarra(self, event):
        """Función para expandir o contraer la barra lateral"""
        if self.barraExpandida:
            self.barra.configure(width=50)
            self.barraExpandida = False
            self.btnBarra.place(relx=0.51, rely=0.05, anchor="center")
            self.btnGestionCliente.place_forget()
            self.btnGestionMesas.place_forget()
            self.btnGestionComandas.place_forget()  
            self.btnSalir.place_forget()
            self.lblMenu.place_forget()
        else:
            self.barra.configure(width=140)
            self.barraExpandida = True
            self.btnGestionCliente.place(relx=0.01, rely=0.2, anchor="w")
            self.btnGestionMesas.place(relx=0.01, rely=0.3, anchor="w")
            self.btnGestionComandas.place(relx=0.01, rely=0.4, anchor="w")
            self.btnSalir.place(relx=0.01, rely=0.5, anchor="w")
            self.btnBarra.place(relx=0.89, rely=0.05, anchor="center")
            self.lblMenu = tk.Label(self.barra, text="Menu", bg="#B0B0B0", font=("Times", 20, "bold"))
            self.lblMenu.place(relx=0.43, rely=0.05, anchor="center")

    # Funciones cliente
    def crearMenuCliente(self, event):
        """Crea el menú para gestionar clientes"""
        if self.barraExpandida:
            self.menuCliente = tk.Menu(self.ventana)
            self.menuCliente.add_command(label="Registrar Cliente", command=self.agregarCliente)
            self.menuCliente.add_separator()
            self.menuCliente.add_command(label="Eliminar Cliente", command=self.eliminarCliente)
            self.menuCliente.post(self.barra.winfo_rootx() + 85, self.barra.winfo_rooty() + 40)

    def agregarCliente(self):  
        """Crea una nueva ventana para agregar un cliente"""
        CrearCliente(self.usuario)

    def eliminarCliente(self):  
        """Crea una nueva ventana para eliminar un cliente"""
        EliminarCliente(self.usuario)

    # Funciones Mesa
    def crearMenuMesa(self, event):
        """Crea el menú para gestionar mesas"""
        if self.barraExpandida:
            self.menuMesa = tk.Menu(self.ventana)
            self.menuMesa.add_command(label="Consultar Mesa", command=self.consultarMesa)
            self.menuMesa.add_separator()
            self.menuMesa.add_command(label="Ocupar Mesa", command=self.ocuparMesa)
            self.menuMesa.add_separator()
            self.menuMesa.add_command(label="Liberar Mesa", command=self.liberarMesa)
            self.menuMesa.post(self.barra.winfo_rootx() + 85, self.barra.winfo_rooty() + 80)

    def consultarMesa(self):  
        """Consulta el estado de una mesa"""
        ConsultarMesa(self.usuario)

    def ocuparMesa(self):
        """Ocupar una mesa"""  
        OcuparMesa(self.usuario)

    def liberarMesa(self):  
        """Liberar una mesa"""
        LiberarMesa(self.usuario)

     # Funciones comanda
    def crearMenuComanda(self, event):
        """Crea el menú para gestionar las comandas"""
        if self.barraExpandida:
            self.menuComanda = tk.Menu(self.ventana)
            self.menuComanda.add_command(label="Tomar Comanda", command=self.tomarComanda)
            self.menuComanda.add_separator()
            self.menuComanda.add_command(label="Agregar plato Comanda", command=self.agregarComanda)
            self.menuComanda.add_separator()
            self.menuComanda.add_command(label="Eliminar plato Comanda", command=self.eliminarPlatoCo)
            self.menuComanda.add_separator()
            self.menuComanda.add_command(label="Enviar Comanda", command=self.enviarComanda)
            self.menuComanda.post(self.barra.winfo_rootx() + 85, self.barra.winfo_rooty() + 110)

    def tomarComanda(self):  
        """Tomar una nueva comanda"""
        TomarComanda(self.usuario)

    def agregarComanda(self):  
        """Agregar un plato a la comanda"""
        AgregarPlatoComanda(self.usuario)

    def eliminarPlatoCo(self):
        """Eliminar un plato de la comanda"""
        EliminarPlatoComanda(self.usuario)

    def enviarComanda(self):
        """Enviar la comanda al sistema"""
        EnviarComanda(self.usuario)

    #Salir
    def crearMenuSalir(self, event):
        """Crea el menú de salida"""
        if self.barraExpandida:
            self.menuSalir = tk.Menu(self.ventana, tearoff=0)
            self.menuSalir.add_command(label="Salir", command=self.salir)
            self.menuSalir.add_separator()
            self.menuSalir.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 163)
    
    def salir(self, event):
        """Cerrar la ventana"""
        self.ventana.destroy()

    def __init__(self, loggin, usuario):
        """Inicializa la ventana y componentes de la interfaz"""
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion de Mesero")
        self.ventana.configure(width=530, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        # Iconos
        self.iconoBarra = tk.PhotoImage(file=r"Restaurante/Src/barra.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Restaurante\Src\ayuda.png")

        # Mensaje de bienvenida
        self.lblBienvenida = tk.Label(self.ventana, text=f"Bienvenido Mesero \n{self.usuario.nombre}", font=("Times", 18, "bold"), fg="black")
        self.lblBienvenida.place(relx=0.5, rely=0.4, anchor="center")

        # Variable para saber si la barra está expandida
        self.barraExpandida = False

        # Barra lateral
        self.barra = tk.Frame(self.ventana, width=50, height=348, bg="#B0B0B0")
        self.barra.place(relx=0.00, rely=0.5, anchor="w")

        # Botones
        self.btnBarra = tk.Label(self.barra, image=self.iconoBarra)
        self.btnBarra.place(relx=0.51, rely=0.05, anchor="center")
        self.btnBarra.bind("<Button-1>", self.toggleBarra)
        Tooltip(self.btnBarra, "Expandir o contraer el menú")
        
        self.btnGestionCliente = tk.Label(self.barra, text="Gestionar Cliente", bg="#B0B0B0")
        self.btnGestionCliente.place(relx=0.01, rely=0.1, anchor="w")
        self.btnGestionCliente.place_forget()
        self.btnGestionCliente.bind("<Button-1>", self.crearMenuCliente)

        self.btnGestionMesas = tk.Label(self.barra, text="Gestionar Mesas", bg="#B0B0B0")
        self.btnGestionMesas.place(relx=0.01, rely=0.3, anchor="w")
        self.btnGestionMesas.place_forget()
        self.btnGestionMesas.bind("<Button-1>", self.crearMenuMesa)

        self.btnGestionComandas = tk.Label(self.barra, text="Gestionar Comanda", bg="#B0B0B0")
        self.btnGestionComandas.place(relx=0.01, rely=0.4, anchor="w")
        self.btnGestionComandas.place_forget()
        self.btnGestionComandas.bind("<Button-1>", self.crearMenuComanda)

        self.btnSalir = tk.Label(self.barra, text="Salir", bg="#B0B0B0")
        self.btnSalir.place(relx=0.01, rely=0.5, anchor="w")
        self.btnSalir.place_forget()
        self.btnSalir.bind("<Button-1>", self.salir)

        self.btnAyuda = tk.Label(self.ventana, text="Ayuda", image=self.iconoAyuda, width=20)
        self.btnAyuda.place(relx=0.95, rely=0.05,anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)


         # Atajos
        self.ventana.bind("<F6>", self.crearMenuCliente)
        self.ventana.bind("<F5>", self.crearMenuMesa)
        self.ventana.bind("<F4>", self.crearMenuSalir)
        self.ventana.bind("<F3>", self.crearMenuComanda)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)


        self.ventana.mainloop()