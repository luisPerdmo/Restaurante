import tkinter as tk
from tkinter import *
from tkinter import messagebox

class RegistrarChef():
        

    def __init__(self, usuario):
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestion de Registador")
        self.ventana.configure(width=300, height=350)
        self.ventana.resizable(0,0)

        self.usuario = usuario