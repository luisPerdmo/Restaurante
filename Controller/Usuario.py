from tkinter import messagebox

class Usuario():

    def __init__(self):
        self.__nombre = None
        self.__rol = None
        self._password = None

    # Getter y Setter 
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_rol(self):
        return self.__rol
    def set_rol(self, rol):
        self.__rol = rol
    def get_password(self):
        return self._password
    def set_password(self, password):
        self._password = password

