from Model.ConexionBD import ConexionDB 
from tkinter import messagebox
import mariadb
from View.GestionRegistrador import GestionRegistrador
from View.GestionChef import GestionChef
from View.GestionMesero import GestionMesero

class Usuario():

    def __init__(self):
        self.__nombre = None
        self.__password = None
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

    def iniciarSesion(self, nombre, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[1] == nombre and usuario[7] == password and usuario[6] == "Registrador"):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                messagebox.showinfo("informacion", "Acceso Correcto Registrador")
                menuRegistrador = GestionRegistrador(loggin, self)
                return   
            elif(usuario[1] == nombre and usuario[5] == password and usuario[6] == "Chef"):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                messagebox.showinfo("informacion", "Acceso correcto Chef")
                menuChef = GestionChef(loggin, self)
                return
            elif(usuario[1] == nombre and usuario[5] == password and usuario[6] == "Mesero"):
                self.nombre = usuario[1]
                self.password = usuario[7]
                self.rol = usuario[6]
                messagebox.showinfo("informacion", "Acceso correcto Mesero")
                menuMesero = GestionMesero(loggin, self)
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
        cursor.execute("DELETE FROM mesa WHERE id_mesa = ? AND estado = 'Disponible'", (id_mesa,))
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
    
    def cambiarMesaEstado(self, id_mesa, nuevo_estado):
        try:
            miConexion = ConexionDB()
            miConexion.crearConexion()
            conexion = miConexion.getConection()
            cursor = conexion.cursor()
            cursor.execute("UPDATE mesa SET estado = ? WHERE id_mesa = ?", (nuevo_estado, id_mesa))
            conexion.commit() 
        except Exception as e:
            print(f"Error al intentar cambiar el estado: {e}")  
            miConexion.cerrarConexion()
    
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
    
    #Plato
    def crearPlato(self, id_plato, nombrePla, precioPla, cantidadPla, descripcionPla):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO plato (id_plato, nombre, precio, cantidad_disponible, descripcion) VALUES (?, ?, ?, ?, ?)", (id_plato, nombrePla, precioPla, cantidadPla, descripcionPla))
        conexion.commit()
        miConexion.cerrarConexion()

    def existePlato(self, id_plato):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM plato WHERE id_plato = ?", (id_plato,))
        resultado = cursor.fetchone()
        miConexion.cerrarConexion()
        return resultado is not None
    
    def eliminarPlato(self, id_plato):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM plato WHERE id_plato = ?", (id_plato,))
        conexion.commit()
        miConexion.cerrarConexion()

    def buscarPlato(self, id_plato):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from plato WHERE id_plato = ?", (id_plato,))
        mesero = cursor.fetchone()  
        miConexion.cerrarConexion()
        return mesero
    
    #Comanda
    def buscarComanda(self, id_comanda):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from comanda WHERE id_comanda = ?", (id_comanda,))
        comanda = cursor.fetchone()  
        miConexion.cerrarConexion()
        return comanda 
    
    def cambiarComanda(self, id_comanda, nuevo_estado):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Update comanda SET estado = ? WHERE id_comanda = ?", (nuevo_estado, id_comanda))
        miConexion.cerrarConexion()

    def tomarComanda(self, id_comanda, cedula_cliente, no_mesa, lista_platos):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        total_precio = 0

        try:
            for plato_id in lista_platos:
                cursor.execute("SELECT precio FROM Plato WHERE id_plato = ?", (plato_id,))
                precio_plato = cursor.fetchone()
                if precio_plato:
                    total_precio += precio_plato[0]

            platos_str = '-'.join(map(str, lista_platos))
            estado = 'Pendiente'

            cursor.execute(
                "INSERT INTO Comanda (id_comanda, cedula_cliente, no_mesa, platos, precio_total, estado) VALUES (?, ?, ?, ?, ?, ?)",
                (id_comanda, cedula_cliente, no_mesa, platos_str, total_precio, estado)
            )
            conexion.commit()
            messagebox.showinfo("Éxito", f"Comanda con ID {id_comanda} tomada correctamente.")
        
        except mariadb.IntegrityError:
            messagebox.showerror("Error", f"El ID de comanda {id_comanda} ya existe. Por favor, ingrese otra ID para poder tomar la comanda.")
            return  

        finally:
            miConexion.cerrarConexion()

        return total_precio
    
    def eliminarPlatoDeComanda(self, id_comanda, plato_a_eliminar):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT estado, platos FROM Comanda WHERE id_comanda = ?", (id_comanda,))
        comanda = cursor.fetchone()
        if not comanda:
            miConexion.cerrarConexion()
            raise ValueError(f"No se encontró la comanda con ID {id_comanda}")
        estado, platos = comanda
        if estado != "Pendiente":
            miConexion.cerrarConexion()
            raise ValueError("Solo se pueden eliminar platos de comandas con estado 'Pendiente'")
        lista_platos = [int(id_plato) for id_plato in platos.split('-')]
        if plato_a_eliminar not in lista_platos:
            miConexion.cerrarConexion()
            raise ValueError(f"El plato con ID {plato_a_eliminar} no está en la comanda")
        lista_platos.remove(plato_a_eliminar)
        total_precio = 0
        for plato_id in lista_platos:
            cursor.execute("SELECT precio FROM Plato WHERE id_plato = ?", (plato_id,))
            precio_plato = cursor.fetchone()
            if precio_plato:
                total_precio += precio_plato[0]
        platos_str = '-'.join(map(str, lista_platos))
        cursor.execute("UPDATE Comanda SET platos = ?, precio_total = ? WHERE id_comanda = ?",
                       (platos_str, total_precio, id_comanda))
        conexion.commit()
        miConexion.cerrarConexion()
        return total_precio

    def agregarPlatoAComanda(self, id_comanda, plato_a_agregar):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT estado, platos FROM Comanda WHERE id_comanda = ?", (id_comanda,))
        comanda = cursor.fetchone()
        if not comanda:
            miConexion.cerrarConexion()
            raise ValueError(f"No se encontró la comanda con ID {id_comanda}")
        estado, platos = comanda
        if estado != "Pendiente":
            miConexion.cerrarConexion()
            raise ValueError("Solo se pueden agregar platos a comandas con estado 'Pendiente'")
        lista_platos = [int(id_plato) for id_plato in platos.split('-')]
        lista_platos.append(plato_a_agregar)
        total_precio = 0
        for plato_id in lista_platos:
            cursor.execute("SELECT precio FROM Plato WHERE id_plato = ?", (plato_id,))
            precio_plato = cursor.fetchone()
            if precio_plato:
                total_precio += precio_plato[0]
        platos_str = '-'.join(map(str, lista_platos))
        cursor.execute("UPDATE Comanda SET platos = ?, precio_total = ? WHERE id_comanda = ?",
                       (platos_str, total_precio, id_comanda))
        conexion.commit()
        miConexion.cerrarConexion()
        return total_precio
    
    def calcularTotal(self, id_comanda):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT cedula_cliente, no_mesa, platos, precio_total, estado FROM Comanda WHERE id_comanda = ?", (id_comanda,))
        comanda = cursor.fetchone()
        
        miConexion.cerrarConexion()
        
        if not comanda:
            raise Exception("No se encontró una comanda con el ID proporcionado.")
        
        return comanda

    #Cliente
    def crearCliente(self, cedulaCli, nombreCli, apellidoCli, telefonoCli, emailCli):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cliente (cedula, nombre, apellido, telefono, email) VALUES (?, ?, ?, ?, ?)", (cedulaCli, nombreCli, apellidoCli, telefonoCli, emailCli))
        conexion.commit()
        miConexion.cerrarConexion()

    def buscarCliente(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from cliente WHERE cedula = ?", (cedulaUsu,))
        cliente = cursor.fetchone()  
        miConexion.cerrarConexion()
        return cliente
    
    def eliminarCliente(self, cedulaUsu):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE cedula = ?", (cedulaUsu,))
        conexion.commit()
        miConexion.cerrarConexion()

    def generarInformeDiario(self):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_comanda, precio_total FROM Comanda WHERE estado = 'Servido'")
        comandas = cursor.fetchall()

        if not comandas:
            miConexion.cerrarConexion()
            raise ValueError("No hay comandas con estado 'Servido'")
        cantidad_comandas = len(comandas)
        ganancia_total = sum(comanda[1] for comanda in comandas)
        promedio_dia = ganancia_total / cantidad_comandas if cantidad_comandas > 0 else 0

        miConexion.cerrarConexion()
        return {
            "id_informe": 1,  
            "cantidad_comandas": cantidad_comandas,
            "ganancia_total": ganancia_total,
            "promedio_dia": promedio_dia
        }