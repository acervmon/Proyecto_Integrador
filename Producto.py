# de LA CLASE producto AÑADE QUE SE PUEDA MODIFICAR, AGREGAR, ELIMINAR Y TRANSFORMAR ADEMAS QUE TENGA  el gestor de clientes que se va a transformar en un gestor de productos 
# de LA CLASE actor principal AÑADE tenemos gesto de actores que es igual a los gestores anteriores
# despues hacer un main menu para agregar,modificar, actualizar, gestionar tanto el producto como un actor. CADA GESTOR DE CLIETNE TIENE UN MAIN DONDE GESTOR DE CLEINTE GESTIONA SOLO PRODUCTO Y OTRO GESTOR GESTUINA LAS ACTORES Y SOBRE ELLO PEDIR LA OPCION DE GESTIONAR PRODUCTO O ACTORES
# EL ACTOR PRINCIPAL SERA UN INTERFAZE UNA CLASE A B C " CLASE ABSTRACTA"
# APARTE DE LOS QUE TIENEN EL GESTOR DE CLIENTE TENDRA METODOS PROPIOS
#MATERIAS PRIMAS "QUE TIPO Y CUANTOS MATERIAS PRIMAS QUE HAYAMOS DEFINIDO UN PRODUCTO" LE TENEMOS QUE DECIR UN ID, UNA MATERIA PRIMA, UN NOMBRE
#DE MATERIA PRIMA VAMOS A LLAMAR A PRODUCTO "GENERAR UNA LISTA DE PRODUCTOS " LLAMAR AL METODO "LISTA PRODUCTO"
#CAMBIO DE CUSTODIA DEL ACTOR 1 AL ACTOR 2
# ESTOS SON LOS METODOS QUE TIENEN TODOS
# DEFINIR QUE TIPO DE ACTOR
#PROVEEDOR SOLO RECOGE DATOS TENDRA UN METODO DE "DAME MATERIAS" Y SERA EL UNICO QUE VA A PODER GESTIONAR UN PRODUCTO, VA A RECIBIR LAS MATERIAS PARA ENVIARSELOS AL FABRICANTE
#FABRICANTE VE LO DE LOS PRODUCTO QUE VA LIGADO CON ELLOS, TENDRA UN METODO DE "FABRICAR Y TRANSFORMAR MATERIAS EN PRODUCTO" ESTE FABRICANTE SE LO DARA AL DSISTRIBUIDOR
# EL DISTRIBUIDOR LO DARA AL MINORISTA Y AL CONSUMIDOR , LOS DISTRIBUIDORES  TENDRA UN METODO DE "DISTRIBUYE PRODUCTOS"
#EL MINORISTA TENDRA EL METODO DE "COMPRA PRODUCTO" Y TENDRA VARAIBLES COMO PRECIO, CANITDAD Y TAL
# CONSUMIDOR TENDRA EL EMTODO DE CONSUME

from abc import ABC, abstractmethod
class Producto:
    def __init__(self, id, nombre, tipo, cantidad, precio, materias_primas=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
        self.materias_primas = materias_primas or []

    def modificar(self, nombre, tipo, cantidad, precio, materias_primas=None):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
        if materias_primas:
            self.materias_primas = materias_primas
            class GestorProductos:
                def __init__(self):
                    self.productos = []

                def agregar_producto(self, producto):
                    self.productos.append(producto)

                def modificar_producto(self, id, nombre, tipo, cantidad, precio, materias_primas=None):
                    for producto in self.productos:
                        if producto.id == id:
                            producto.modificar(nombre, tipo, cantidad, precio, materias_primas)
                            break

                def eliminar_producto(self, id):
                    for producto in self.productos:
                        if producto.id == id:
                            self.productos.remove(producto)
                            break

                def ver_lista_productos(self):
                    for producto in self.productos:
                        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
class ActorPrincipal(ABC, Producto):
    lista = []

    def __init__(self, id, nombre, tipo, materias_primas=None):
        super().__init__(id, nombre, tipo, 0, 0, materias_primas)
        self.punto_recepcion_materias_primas = None
        self.punto_transformacion_materiales = None
        self.punto_cambio_custodia = None
        self.punto_venta = None
        self.punto_consumo = None
        ActorPrincipal.lista.append(self)

    @abstractmethod
    def gestionar(self):
        pass

    @staticmethod
    def buscar(dni):
        for actor in ActorPrincipal.lista:
            if actor.id == dni:
                return actor

    @staticmethod
    def crear(id, nombre, tipo, materias_primas=None):
        actor = ActorPrincipal(id, nombre, tipo, materias_primas)
        return actor

class Proveedor(ActorPrincipal):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre, tipo)

    def gestionar(self):
        while True:
            print("1. Agregar materia prima")
            print("2. Modificar materia prima")
            print("3. Eliminar materia prima")
            print("4. Volver al menú principal")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.agregar_materia_prima()
            elif opcion == 2:
                self.modificar_materia_prima()
            elif opcion == 3:
                self.eliminar_materia_prima()
            elif opcion == 4:
                break
            else:
                print("Opción inválida")

    def agregar_materia_prima(self):
        id = int(input("Ingrese el ID de la materia prima: "))
        nombre = input("Ingrese el nombre de la materia prima: ")
        materia_prima = {"id": id, "nombre": nombre}
        self.materias_primas.append(materia_prima)

    def modificar_materia_prima(self):
        id = int(input("Ingrese el ID de la materia prima a modificar: "))
        for materia_prima in self.materias_primas:
            if materia_prima["id"] == id:
                materia_prima["nombre"] = input("Ingrese el nuevo nombre de la materia prima: ")
                break

    def eliminar_materia_prima(self):
        id = int(input("Ingrese el ID de la materia prima a eliminar: "))
        for materia_prima in self.materias_primas:
            if materia_prima["id"] == id:
                self.materias_primas.remove(materia_prima)
                break

class Fabricante(ActorPrincipal):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre, tipo)

    def fabricar_y_transformar_materias_en_producto(self, materias_primas):
        producto = Producto(len(self.lista) + 1, "Producto Nuevo", "Tipo Nuevo", 1, 100, materias_primas)
        self.lista.append(producto)

    def dame_materias(self):
        materias_primas = []
        while True:
            print("1. Agregar materia prima")
            print("2. Terminar")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                id = int(input("Ingrese el ID de la materia prima: "))
                nombre = input("Ingrese el nombre de la materia prima: ")
                materia_prima = {"id": id, "nombre": nombre}
                materias_primas.append(materia_prima)
            elif opcion == 2:
                break
            else:
                print("Opción inválida")
        return materias_primas
        def ver_lista_productos(self):
            for producto in self.productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
                print("Opción inválida")

def ver_lista_productos(self):
    for producto in self.lista:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

class Distribuidor(ActorPrincipal):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre, tipo)
        self.productos = []

    def distribuir_productos(self, productos):
        self.productos = productos

    def gestionar(self):
        while True:
            print("1. Ver lista de productos")
            print("2. Volver al menú principal")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.ver_lista_productos()
            elif opcion == 2:
                break
            else:
                print("Opción inválida")

    def ver_lista_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

class Minorista(ActorPrincipal):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre, tipo)
        self.productos = []

    def comprar_productos(self, productos):
        self.productos = productos

    def dame_productos(self):
        productos = []
        while True:
            print("1. Agregar producto")
            print("2. Terminar")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                tipo = input("Ingrese el tipo del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id, nombre, tipo, cantidad, precio)
                productos.append(producto)
            elif opcion == 2:
                break
            else:
                print("Opción inválida")
        return productos

    def gestionar(self):
        while True:
            print("1. Ver lista de productos")
            print("2. Comprar productos")
            print("3. Volver al menú principal")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.ver_lista_productos()
            elif opcion == 2:
                self.comprar_productos(self.dame_productos())  # Fixed the issue by calling the dame_productos method on self
            elif opcion == 3:
                break
            else:
                print("Opción inválida")

    def ver_lista_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

class Consumidor(ActorPrincipal):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre, tipo)
        self.productos = []

    def consumir_producto(self, producto):
        if producto in self.productos:
            print(f"Consumiendo producto: {producto.nombre}")
            self.productos.remove(producto)
        else:
            print("El producto no está en la lista de productos del consumidor")
