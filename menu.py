import os
from Producto import Producto as db
from utils import leer_texto # type: ignore

def limpiar_pantalla():
    os.system('clear')  # Use 'cls' instead of 'clear' on Windows

def listar_productos():
    """
    List all the products.
    """
    print("Listando los productos...\n")
    for producto in db.lista:
        print(producto)

def buscar_producto():
    """
    Search for a product.
    """
    print("Buscando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    producto = db.buscar(codigo)
    result = print(producto) if producto else print("Producto no encontrado.")
    return result

def añadir_producto():
    """
    Add a new product.
    """
    print("Añadiendo un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    nombre = leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
    tipo = leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()
    db.crear(codigo, nombre, tipo)

def modificar_producto():
    """
    Modify an existing product.
    """
    print("Modificando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    producto = db.buscar(codigo)
    if producto:
        nombre = leer_texto(2, 30, f"Nombre (de 2 a 30 chars)[{producto.nombre}]").capitalize()
        tipo = leer_texto(2, 30, f"Tipo (de 2 a 30 chars)[{producto.tipo}]").capitalize()
        db.modificar(producto.codigo, nombre, tipo)
        print("Producto modificado correctamente.")
    else:
        print("Producto no encontrado.")

def borrar_producto():
    """
    Delete a product.
    """
    print("Borrando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    if db.borrar(codigo):
        print("Producto borrado correctamente.")
    else:
        print("Producto no encontrado.")
        # Add an indented block here

def iniciar():
    """
    Start the product manager.
    """
    while True:
        limpiar_pantalla()
        print("========================")
        print(" BIENVENIDO AL MANAGER DE PRODUCTOS ")
        print("========================")
        print("[1] Listar productos ")
        print("[2] Buscar producto ")
        print("[3] Añadir producto ")
        print("[4] Modificar producto ")
        print("[5] Borrar producto ")
        print("[6] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        limpiar_pantalla()
        if opcion == '1':
            listar_productos()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            añadir_producto()
        elif opcion == '4':
            modificar_producto()
        elif opcion == '5':
            borrar_producto()
        elif opcion == '6':
            print("Saliendo...\n")
            break
        input("\nPresiona ENTER para continuar...")

input("\nPresiona ENTER para continuar...")
limpiar_pantalla()
