from Model.ConexionBD import ConexionDB
from tkinter import messagebox
from View.GestionRegistrador import GestionRegistrador

class Usuario():

    def __init__(self):
        self.__nombre = None
        self._password = None
        self.__rol = None

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
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            print(f"Usuario en DB: {usuario[1]}, Contraseña en DB: {usuario[7]}, {usuario[6]}")
            if(usuario[1] == nombre and usuario[7] == password):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                if(usuario[6] == "Registrador"):
                    messagebox.showinfo("informacion", "Acceso Correcto Registrador")
                    menuRegistrador = GestionRegistrador(loggin, self)
                    return        
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o Password no existe, verifique e intente nuevamente!")

    def crearRegistrador(self, nombreUsu, apellidoUsu, emailUsu, cedulaUsu, passworUsu, rolUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, cedula, password, rol) VALUES (?, ?, ?, ?, ?, ?)", (nombreUsu, apellidoUsu, emailUsu, cedulaUsu, passworUsu, rolUsu))
        conexion.commit()
        miConexion.cerrarConexion()

    def existeUsuario(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE cedula = ?", (cedulaUsu,))
        resultado = cursor.fetchone()
        miConexion.cerrarConexion()
        return resultado is not None
    
    def crearMesa(self, idMe, cantidadCo, estadoMe):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO mesa (id_mesa, cantidad_comensales, estado) VALUES (?, ?, ?)", (idMe, cantidadCo, estadoMe))
        conexion.commit()
        miConexion.cerrarConexion()

    def existeMesa(self, idMesa):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM mesa WHERE id_mesa = ?", (idMesa,))
        resultado = cursor.fetchone()
        miConexion.cerrarConexion()
        return resultado is not None

    def eliminarMesa(self, id_mesa):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM mesa WHERE id_mesa = ?", (id_mesa,))
        conexion.commit()
        miConexion.cerrarConexion()

    def buscarMesa(self, id_mesa):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from mesa WHERE id_mesa = ?", (id_mesa,))
        mesas = cursor.fetchone()  
        miConexion.cerrarConexion()
        return mesas  