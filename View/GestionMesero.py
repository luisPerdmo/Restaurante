import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

from View.CrearCliente import CrearCliente
from View.EliminarCliente import EliminarCliente
from View.ConsultarMesa import ConsultarMesa
from View.OcuparMesa import OcuparMesa

class GestionMesero():

    def toggleBarra(self, event):
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
        if self.barraExpandida:
            self.menuCliente = tk.Menu(self.ventana)
            self.menuCliente.add_command(label="Registrar Cliente", command=self.agregarCliente)
            self.menuCliente.add_separator()
            self.menuCliente.add_command(label="Eliminar Cliente", command=self.eliminarCliente)
            self.menuCliente.post(self.barra.winfo_rootx() + 85, self.barra.winfo_rooty() + 40)

    def agregarCliente(self):  
        CrearCliente(self.usuario)

    def eliminarCliente(self):  
        EliminarCliente(self.usuario)

    # Funciones cliente
    def crearMenuMesa(self, event):
        if self.barraExpandida:
            self.menuMesa = tk.Menu(self.ventana)
            self.menuMesa.add_command(label="Registrar Cliente", command=self.consultarMesa)
            self.menuMesa.add_separator()
            self.menuMesa.add_command(label="Eliminar Cliente", command=self.ocuparMesa)
            self.menuMesa.post(self.barra.winfo_rootx() + 85, self.barra.winfo_rooty() + 110)

    def consultarMesa(self):  
        ConsultarMesa(self.usuario)

    def ocuparMesa(self):  
        OcuparMesa(self.usuario)

    
    #Salir
    def crearMenuSalir(self, event):
        if self.barraExpandida:
            self.menuSalir = tk.Menu(self.ventana, tearoff=0)
            self.menuSalir.add_command(label="Salir", command=self.salir)
            self.menuSalir.add_separator()
            self.menuSalir.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 163)
    
    def salir(self):
        self.ventana.destroy()

    def __init__(self, loggin, usuario):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion de Mesero")
        self.ventana.configure(width=530, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        # Iconos
        self.iconoBarra = tk.PhotoImage(file=r"Restaurante/Src/barra.png")

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

        self.btnGestionComandas = tk.Label(self.barra, text="Gestionar Mesa", bg="#B0B0B0")
        self.btnGestionComandas.place(relx=0.01, rely=0.4, anchor="w")
        self.btnGestionComandas.place_forget()
        #self.btnGestionComandas.bind("<Button-1>", self.crearMenuMesa)

        self.btnSalir = tk.Label(self.barra, text="Salir", bg="#B0B0B0")
        self.btnSalir.place(relx=0.01, rely=0.5, anchor="w")
        self.btnSalir.place_forget()
        self.btnSalir.bind("<Button-1>", self.crearMenuSalir)



        self.ventana.mainloop()