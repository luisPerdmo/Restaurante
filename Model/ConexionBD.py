import mariadb as sql
from tkinter import messagebox

class ConexionDB():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__port = 3306
        self.__database = "restaurante"
        self.__conection = None

    def crearConexion(self):
        try:
            self.__conection = sql.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                port = self.__port,
                database = self.__database          
            )
        except sql.OperationalError as e:
            messagebox.showwarning("Advertencia", "Error de conexion al servidor de base de datos\nVerifique su conexion e internet o contacte al administrador del sistema...")

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

     # Getters
    def getHost(self):
        return self.__host
    def getUser(self):
        return self.__user
    def getPassword(self):
        return self.__password
    def getPort(self):
        return self.__port
    def getDatabase(self):
        return self.__database
    def getConection(self):
        return self.__conection
    # Setters
    def setHost(self, host):
        self.__host = host
    def setUser(self, user):
        self.__user = user
    def setPassword(self, password):
        self.__password = password
    def setPort(self, port):
        self.__port = port
    def setDatabase(self, database):
        self.__database = database
    def setConection(self, conection):
        self.__conection = conection