from Model.ConexionBD import ConexionDB
from tkinter import messagebox

class Usuario():

    def __init__(self):
        self.__nombre = None
        self.__rol = None
        self._password = None

    # Getter y Setter 
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getRol(self):
        return self.__rol
    def setRol(self, rol):
        self.__rol = rol
    def getPassword(self):
        return self._password
    def setPassword(self, password):
        self._password = password

    def iniciarSesion(self, nombre, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()

