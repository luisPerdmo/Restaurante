import tkinter as tk
from tkinter import *
from tkinter import messagebox
from View.RegistrarChef import RegistrarChef

class GestionRegistrador():

    def toggleBarra(self, event):
        if self.barraExpandida:
            self.barra.configure(width=70)
            self.barraExpandida = False
            self.btnBarra.place(relx=0.78, rely=0.05, anchor="center")
            self.btnGestionChef.place_forget()
            self.btnGestionMesero.place_forget()
        else:
            self.barra.configure(width=120)
            self.barraExpandida = True
            self.btnGestionChef.place(relx=0.01, rely=0.2, anchor="w")
            self.btnGestionMesero.place(relx=0.01, rely=0.3, anchor="w")
            self.btnBarra.place(relx=0.85, rely=0.05, anchor="center")
    
    #funciones chef
    def crearMenuChef(self, event):
        if self.barraExpandida:
            self.menuChef = tk.Menu(self.ventana)
            self.menuChef.add_command(label="Registrar Chef", command=self.agregarChef)
            self.menuChef.add_separator()
            self.menuChef.post(self.barra.winfo_rootx() + 80, self.barra.winfo_rooty() + 40)

    def agregarChef(self):
        RegistrarChef(self.ventana)

    
    def __init__(self, loggin, usuario):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion de Registador")
        self.ventana.configure(width=600, height=350)
        self.ventana.resizable(0,0)

        self.usuario = usuario

        # Variable para saber si la barra está expandida
        self.barraExpandida = False

        #Iconos 
        self.iconoBarra = tk.PhotoImage(file=r"Restaurante/Src/barra.png")

        #Barra lateral
        self.barra = tk.Frame(self.ventana, width=70, height=348, bg="#CCD1D1")
        self.barra.place(relx=0.00, rely=0.5, anchor="w")

        # Botones
        self.btnBarra = tk.Label(self.barra, image=self.iconoBarra)
        self.btnBarra.place(relx=0.78, rely=0.05, anchor="center")
        self.btnBarra.bind("<Button-1>", self.toggleBarra)

        self.btnGestionChef = tk.Label(self.barra, text="Gestionar Chef")
        self.btnGestionChef.place(relx=0.01, rely=0.1, anchor="w")
        self.btnGestionChef.place_forget()
        self.btnGestionChef.bind("<Button-1>", self.crearMenuChef)

        self.btnGestionMesero = tk.Label(self.barra, text="Gestionar Mesero")
        self.btnGestionMesero.place(relx=0.01, rely=0.3, anchor="w")
        self.btnGestionMesero.place_forget()
        self.btnGestionMesero.bind("<Button-1>", self.crearMenuChef)
       


        self.ventana.mainloop()