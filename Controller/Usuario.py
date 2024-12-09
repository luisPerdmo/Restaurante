from Model.ConexionBD import ConexionDB
from tkinter import messagebox
from View.GestionRegistrador import GestionRegistrador
from View.GestionChef import GestionChef

class Usuario():

    def __init__(self):
        self.__nombre = None
        self.__password = None
        self.__cedula = None
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
        return self.__password
    def setPassword(self, password):
        self.__password = password
    def getCedula(self):
        return self.__cedula
    def setCedula(self, cedula):
        self.__cedula = cedula

    def iniciarSesion(self, nombre, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1] == nombre and usuario[7] == password):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                if(usuario[6] == "Registrador"):
                    messagebox.showinfo("informacion", "Acceso Correcto Registrador")
                    menuRegistrador = GestionRegistrador(loggin, self)
                    return   
            elif(usuario[1] == nombre and usuario[5] == password):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                if(usuario[6] == "Chef"):
                    messagebox.showinfo("informacion", "Acceso correcto Chef")
                    menuChef = GestionChef(loggin, self)
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

    #chef
    def crearChef(self, nombreUsu, apellidoUsu, emailUsu, telefonoUsu, cedulaUsu, rolUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, telefono, cedula, rol) VALUES (?, ?, ?, ?, ?, ?)", (nombreUsu, apellidoUsu, emailUsu, telefonoUsu, cedulaUsu, rolUsu))
        conexion.commit()
        miConexion.cerrarConexion()

    def eliminarChef(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuario WHERE cedula = ?", (cedulaUsu,))
        conexion.commit()
        miConexion.cerrarConexion()

    def buscarChef(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario WHERE cedula = ?", (cedulaUsu,))
        chef = cursor.fetchone()  
        miConexion.cerrarConexion()
        return chef  

    def existeUsuario(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE cedula = ?", (cedulaUsu,))
        resultado = cursor.fetchone()
        miConexion.cerrarConexion()
        return resultado is not None
    
    #Mesa
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
    
    #Mesero
    def crearMesero(self, nombreUsu, apellidoUsu, emailUsu, telefonoUsu, cedulaUsu, rolUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, telefono, cedula, rol) VALUES (?, ?, ?, ?, ?, ?)", (nombreUsu, apellidoUsu, emailUsu, telefonoUsu, cedulaUsu, rolUsu))
        conexion.commit()
        miConexion.cerrarConexion()

    def eliminarMesero(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuario WHERE cedula = ?", (cedulaUsu,))
        conexion.commit()
        miConexion.cerrarConexion()

    def buscarMesero(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario WHERE cedula = ?", (cedulaUsu,))
        mesero = cursor.fetchone()  
        miConexion.cerrarConexion()
        return mesero
    