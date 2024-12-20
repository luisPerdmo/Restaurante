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

from View.AgregarPlato import AgregarPlato
from View.EliminarPlato import EliminarPlato
from View.CambiarEstadoComanda import CambiarEstadoComanda

class GestionChef():
    """
    Clase que representa la gestión del chef en el sistema. Esta ventana permite gestionar platos y comandas.
    Además, ofrece una barra lateral con opciones para gestionar el restaurante.
    """

    def mostrarAyuda(self, event):
        """
        Muestra un cuadro de mensaje con los atajos disponibles para el usuario.
        Los atajos son accesibles mediante teclas específicas.
        """
        ayudaTexto = (
            "Atajos.\n\n"
            "- Presione 'F4' para crear menu plato. \n"
            "- Presione 'F5' para crear menu salir. \n"
            "- presione 'F3' para crear menu comanda. \n"
            "- presione 'F2' para cerrar la ventana. \n"
            "- Presione 'F1' para obtener ayuda. \n"
        )
        messagebox.showinfo("Ayuda", ayudaTexto)

    def toggleBarra(self, event):
        """
        Función que permite expandir o contraer la barra lateral en la ventana.
        Si la barra está contraída, se expande, mostrando los botones del menú.
        Si está expandida, se contrae, ocultando los botones del menú.
        """
        if self.barraExpandida:
            self.barra.configure(width=50)
            self.barraExpandida = False
            self.btnBarra.place(relx=0.51, rely=0.05, anchor="center")
            self.btnGestionPlatos.place_forget()
            self.btnGestionComanda.place_forget()
            self.btnSalir.place_forget()
            self.lblMenu.place_forget()
        else:
            self.barra.configure(width=140)
            self.barraExpandida = True
            self.btnGestionPlatos.place(relx=0.01, rely=0.2, anchor="w")
            self.btnGestionComanda.place(relx=0.01, rely=0.3, anchor="w")
            self.btnSalir.place(relx=0.01, rely=0.4, anchor="w")
            self.btnBarra.place(relx=0.89, rely=0.05, anchor="center")
            self.lblMenu = tk.Label(self.barra, text="Menu", bg="#CCD1D1", font=("Times", 20, "bold"))
            self.lblMenu.place(relx=0.43, rely=0.05, anchor="center")

    #Plato
    def crearMenuPlato(self, event):
        """
        Crea y muestra el menú contextual para gestionar los platos.
        Incluye las opciones para agregar o eliminar platos.
        """
        if self.barraExpandida:
            self.menuPlato = tk.Menu(self.ventana)
            self.menuPlato.add_command(label="Agregar plato", command=self.agregarPlato)
            self.menuPlato.add_separator()
            self.menuPlato.add_command(label="Eliminar plato", command=self.eliminarPlato)
            self.menuPlato.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 40)
    
    def agregarPlato(self):
        """
        Abre la vista para agregar un nuevo plato.
        """
        AgregarPlato(self.usuario)

    def eliminarPlato(self):
        """
        Abre la vista para eliminar un plato existente.
        """
        EliminarPlato(self.usuario)

    #Comanda    
    def crearMenuComanda(self, event):
        """
        Crea y muestra el menú contextual para gestionar las comandas.
        Permite cambiar el estado de una comanda.
        """
        if self.barraExpandida:
            self.menuComanda = tk.Menu(self.ventana)
            self.menuComanda.add_command(label="Cambiar estado comanda", command=self.cambiarEstado)
            self.menuComanda.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 80)

    def cambiarEstado(self): 
        """
        Abre la vista para cambiar el estado de una comanda.
        """
        CambiarEstadoComanda(self.usuario)

    #SAlir
    def crearMenuSalir(self, event):
        """
        Crea y muestra el menú contextual para cerrar la aplicación.
        Ofrece una opción para salir de la ventana.
        """
        if self.barraExpandida:
            self.menuSalir = tk.Menu(self.ventana, tearoff=0)
            self.menuSalir.add_command(label="Salir", command=self.salir)
            self.menuSalir.add_separator()
            self.menuSalir.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 133)

    def salir(self, event):
        """
        Cierra la ventana principal y termina la aplicación.
        """
        self.ventana.destroy()

    def __init__(self, loggin, usuario):
        """
        Constructor de la clase, inicializa la ventana y los componentes visuales de la interfaz.
        
        :param loggin: La ventana principal donde se inició sesión
        :param usuario: El usuario actual que está gestionando la ventana
        """
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion Chef")
        self.ventana.configure(width=530, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario

        # Mensaje de bienvenida
        self.lblBienvenida = tk.Label(self.ventana, text=f"Bienvenido Chef \n{self.usuario.nombre}", font=("Times", 18, "bold"), fg="black")
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

        self.btnGestionPlatos = tk.Label(self.barra, text="Gestionar Platos", bg="#CCD1D1")
        self.btnGestionPlatos.place(relx=0.01, rely=0.1, anchor="w")
        self.btnGestionPlatos.place_forget()
        self.btnGestionPlatos.bind("<Button-1>", self.crearMenuPlato)
        Tooltip(self.btnGestionPlatos, "Haz clic para gestionar los platos: agregar o eliminar platos.")

        self.btnGestionComanda = tk.Label(self.barra, text="Gestionar Comandas", bg="#CCD1D1")
        self.btnGestionComanda.place(relx=0.01, rely=0.3, anchor="w")
        self.btnGestionComanda.place_forget()
        self.btnGestionComanda.bind("<Button-1>", self.crearMenuComanda)
        Tooltip(self.btnGestionComanda, "Haz clic para gestionar las comandas: cambiar el estado de una comanda.")

        self.btnSalir = tk.Label(self.barra, text="Salir", bg="#CCD1D1")
        self.btnSalir.place(relx=0.01, rely=0.4, anchor="w")
        self.btnSalir.place_forget()
        self.btnSalir.bind("<Button-1>", self.salir)
        Tooltip(self.btnSalir, "Presione para salir de la ventana")

        self.btnAyuda = tk.Label(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(relx=0.95, rely=0.05, anchor="center")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        Tooltip(self.btnAyuda, "Obtener ayuda sobre la ventana")

        # Atajos
        self.ventana.bind("<F4>", self.crearMenuPlato)
        self.ventana.bind("<F3>", self.crearMenuComanda)
        self.ventana.bind("<F5>", self.crearMenuSalir)
        self.ventana.bind("<F2>", self.salir)
        self.ventana.bind("<F1>", self.mostrarAyuda)


        self.ventana.mainloop()
