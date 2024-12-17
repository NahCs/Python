import sqlite3
con = sqlite3.connect('inventario.db')

inventario = []

def mostrar_productos():
    if inventario:
        print("Productos del inventario:")
        for producto in inventario:
            print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']} \n")
    else:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("No hay prductos que mostar")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<< \n")

def registrar_producto():
    id = int(input("ingrese el id del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario.append({"id": id, "nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f" '{nombre}' con cantidad {cantidad} fue agregado al inventario con el numero de id: {id}\n")

def actualizar_producto():
       #solicito el ID del producto para luego guardarlo en la variable
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    producto_encontrado = None

    for producto in inventario:
        #Aca comparo el numero guardado en variable con los ya ingresados en la tabla
        if producto["id"] == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado:
        print(f"Producto encontrado: ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']} | Categoria: {producto['categoria']} \n")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto_encontrado["cantidad"] = nueva_cantidad
        producto_encontrado["precio"] = nuevo_precio
        print(f"Producto actualizado!")
    else:
        print(f"No se encontró un producto con el ID {id_producto}")


def eliminar_producto():
    print("aca se podran eleminar los productos")

def buscar_producto():
    print("Aca vas a poder buscar productos")

def reporte_bajo_stock():
    print("aca vas a poder quejarte de lo que hay")


while True:
    print("<<<<<<<<<<<<<<<<<<<<<")
    print("Gestion de productos")
    print("<<<<<<<<<<<<<<<<<<<<< \n")
    print("1 Agregar producto")
    print("2 Ver inventario")
    print("3 Actualizar producto")
    print("4 Eliminar producto")
    print("5 Buscar producto")
    print("6 ¿Bajo stock?")
    print("7 Salir")

    opcion = input("Seleccione una opcion: ")


    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "7":
        break
