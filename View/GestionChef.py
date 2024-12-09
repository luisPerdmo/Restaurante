import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class GestionChef():

    def __init__(self, loggin, usuario):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.title("Gestion Chef")
        self.ventana.configure(width=530, height=350)
        self.ventana.resizable(0, 0)

        self.usuario = usuario


        self.ventana.mainloop()