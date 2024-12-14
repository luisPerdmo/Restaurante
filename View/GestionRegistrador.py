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

    def mostrarAyuda(self, event):
        messagebox.showinfo(
            "Ayuda", 
            "Bienvenido al sistema de gestión de registradores.\n\n"
            "1. Use el menú lateral para gestionar chefs, meseros y mesas.\n"
            "2. Puede crear y eliminar registros según sea necesario.\n"
            "3. Expanda o contraiga el menú con el botón de la barra.\n"
        )

    def toggleBarra(self, event):
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
        if self.barraExpandida:
            self.menuChef = tk.Menu(self.ventana)
            self.menuChef.add_command(label="Registrar Chef", command=self.agregarChef)
            self.menuChef.add_separator()
            self.menuChef.add_command(label="Eliminar Chef", command=self.eliminarChef)
            self.menuChef.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 40)

    def agregarChef(self):  
        CrearChef(self.usuario)

    def eliminarChef(self):  
        EliminarChef(self.usuario)

    # Función para mesas
    def crearMenuMesa(self, event):
        if self.barraExpandida:
            self.menuMesa = tk.Menu(self.ventana)
            self.menuMesa.add_command(label="Registrar Mesa", command=self.agregarMesa)
            self.menuMesa.add_separator()
            self.menuMesa.add_command(label="Eliminar Mesa", command=self.eliminarMesa)
            self.menuMesa.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 110)

    def agregarMesa(self):
        CrearMesa(self.usuario)  

    def eliminarMesa(self):
        EliminarMesa(self.usuario)

    #Mesero
    def crearMenuMesero(self, event):
        if self.barraExpandida:
            self.menuMesero = tk.Menu(self.ventana)
            self.menuMesero.add_command(label="Registrar Mesero", command=self.agregarMesero)
            self.menuMesero.add_separator()
            self.menuMesero.add_command(label="Eliminar Mesero", command=self.eliminarMesero)
            self.menuMesero.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 80)

    def agregarMesero(self): 
        CrearMesero(self.usuario)

    def eliminarMesero(self): 
        EliminarMesero(self.usuario)

    #Comanda
    def crearMenuComada(self, event):
        if self.barraExpandida:
            self.menuComada = tk.Menu(self.ventana, tearoff=0)
            self.menuComada.add_command(label="Crear informe diario", command=self.informeDiario)
            self.menuComada.add_separator()
            self.menuComada.add_command(label="Calcular precio total", command=self.precioTotal)
            self.menuComada.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 150)
       
    def informeDiario(self):
        InformeDiario(self.usuario)

    def precioTotal(self):
        Calculartotal(self.usuario)

    #Salir
    def crearMenuSalir(self, event):
        if self.barraExpandida:
            self.menuSalir = tk.Menu(self.ventana, tearoff=0)
            self.menuSalir.add_command(label="Salir", command=self.salir)
            self.menuSalir.add_separator()
            self.menuSalir.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 198)
    
    def salir(self):
        self.ventana.destroy()

    def __init__(self, loggin, usuario):
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
        self.btnSalir.bind("<Button-1>", self.crearMenuSalir)
        Tooltip(self.btnSalir, "Presione para salir de la ventana")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.95, rely=0.05, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre la ventana")

        self.ventana.mainloop()
