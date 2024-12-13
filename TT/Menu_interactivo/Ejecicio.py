inventario = []


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese la cantidad: ")
    inventario.append({"nombre": nombre, "cantidad": cantidad})
    print(f" '{nombre}' con cantidad {cantidad} fue agregado al inventario\n")


def ver_inventario():
    if inventario:
        print("Productos del inventario:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto['nombre']} Cantidad: {producto['cantidad']} \n")
    else:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("No hay prductos que mostar")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<< \n")

while True:
    print("<<<<<<<<<<<<<<<<<<<<<")
    print("Gestion de productos")
    print("<<<<<<<<<<<<<<<<<<<<< \n")
    print("1 Agregar producto")
    print("2 Ver inventario")
    print("3 Salir")

    opcion = input("Seleccione una opcion: ")


    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_inventario()
    elif opcion == "3":
        break
