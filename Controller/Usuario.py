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
        cursor.execute("select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1] == nombre and usuario[2] == password):
                self.nombre = usuario[1]
                self.password = usuario[2]
                self.rol = usuario[3]
                if(usuario[3] == "Registrador"):
                    messagebox.showinfo("informacion", "Acceso Correcto Registrador")


    def crearRegistrador(self, nombreUsu, apellidoUsu, emailUsu, cedulaUsu, passworUsu, rolUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, cedula, password, rol) VALUES (?, ?, ?, ?, ?, ?)", (nombreUsu, apellidoUsu, emailUsu, cedulaUsu, passworUsu, rolUsu))
        conexion.commit()
        miConexion.cerrarConexion()

    def existeUsuario(self, emailUsu, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM jugadores WHERE nombre = ? WHERE cedula = ?", (emailUsu, cedulaUsu))
        conexion.commit()
        resultado = cursor.fetchone()
        miConexion.cerrarConexion()
        return resultado is not None