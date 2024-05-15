import os
from Producto import Producto

def limpiar_pantalla():
    """
    Clear the console screen.
    """
    os.system('clear')  # Use 'cls' instead of 'clear' on Windows

def obtener_productos():
    """
    Get a list of products.
    """
    # Add code here to retrieve the list of products
    pass

def listar_productos():
    """
    List all the products.
    """
    print("Listando los productos...\n")
    for producto in obtener_productos():
        print(producto)

def buscar_producto():
    """
    Search for a product.
    """
    print("Buscando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    producto = buscar_producto_por_codigo(codigo)
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
    añadir_producto_nuevo(codigo, nombre, tipo, 0, 0)

def modificar_producto():
    """
    Modify an existing product.
    """
    print("Modificando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    producto = buscar_producto_por_codigo(codigo)
    if producto:
        nombre = leer_texto(2, 30, f"Nombre (de 2 a 30 chars)[{producto.nombre}]").capitalize()
        tipo = leer_texto(2, 30, f"Tipo (de 2 a 30 chars)[{producto.tipo}]").capitalize()
        Producto.modificar(producto.codigo, nombre, tipo, 0, 0)
        print("Producto modificado correctamente.")
    else:
        print("Producto no encontrado.")

def borrar_producto():
    """
    Delete a product.
    """
    print("Borrando un producto...\n")
    codigo = leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
    if borrar_producto_por_codigo(codigo):
        print("Producto borrado correctamente.")
    else:
        print("Producto no encontrado.")

def leer_texto(min_length, max_length, prompt):
    """
    Read a text input from the user.
    """
    text = input(prompt)
    while len(text) < min_length or len(text) > max_length:
        print(f"El texto debe tener entre {min_length} y {max_length} caracteres.")
        text = input(prompt)
    return text

def buscar_producto_por_codigo(codigo):
    """
    Search for a product by its code.
    """
    # Add code here to search for the product by its code
    pass

def añadir_producto_nuevo(codigo, nombre, tipo, arg1, arg2):
    """
    Add a new product.
    """
    # Add code here to add the new product
    pass

def borrar_producto_por_codigo(codigo):
    """
    Delete a product by its code.
    """
    # Add code here to delete the product by its code
    pass


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
