import sqlite3
conexion = sqlite3.connect('inventario.db')
cur = conexion.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS productos (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre   TEXT    NOT NULL,
    cantidad INTEGER NOT NULL,
    precio   REAL    NOT NULL,
    categoria TEXT    NOT NULL
) ''')
conexion.commit()


inventario = []


def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoria del producto: ")
    consulta = "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (?, ?, ?, ?)"
    cur.execute(consulta, (nombre, cantidad, precio, categoria))
    conexion.commit()
    print(f" '{nombre}' con cantidad {cantidad} fue agregado con exito al inventario!\n")


#Trae la totalidad de los productos ingresados en la base de datos
def mostrar_productos():
    cur.execute("SELECT * FROM productos")
    productos = cur.fetchall()
    if productos:
        print("\nListado de Productos\n")
        for producto in productos:
            print(f"Id: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]} | Categoría: {producto[4]}")
    else:
        print("No hay productos en el inventario :( \n")




def actualizar_producto():
    cur.execute("SELECT * FROM productos")
    productos = cur.fetchall()
    #Trae todos los productos agregados hasta el momento
    if productos:
        print("\nListado de Productos\n")
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]} | Categoría: {producto[4]}")
        print("")

        # A partir de aca, solicito al usuario que ingrese el ID del producto a modificar
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        cur.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cur.fetchone()
        #Aca realizo el cambio para luego guardalo en la base de datos
        if producto:
            print(f"Producto encontrado: Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]}")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            cur.execute("UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?", (nueva_cantidad, nuevo_precio, id_producto))
            conexion.commit()
            print("Producto actualizado con éxito!\n")
        else:
            print(f"No se encontro ningun producto con el ID {id_producto}\n")
    else:
        print("No hay productos disponibles para actualizar\n")


def eliminar_producto():
    id_producto = int(input("Que producto desea eliminar? Ingrese el ID: "))
    # Le pido al usuario un ID y verifico si el producto existe
    cur.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cur.fetchone()
    #Aca o elimino el producto sino, le aviso al usuario que no existe un producto con ese ID
    if producto:
        cur.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print(f"Producto con ID {id_producto} acaba de ser eliminado\n")
    else:
        print(f"No se encontro ningun producto con el ID {id_producto}\n")


#En caso de querer buscar un producto en concreto
def buscar_producto():
    id_producto = int(input("Ingrese el ID del producto que desea buscar: "))

    cur.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cur.fetchone()

    if producto:
        print(f"Producto encontrado! ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]} | Categoría: {producto[4]}")
    else:
        print(f"No se encontro ningun producto con el ID {id_producto} verifique nuevamente\n") #Se que revea el listado antes de hacer una consulta nuevamente


def reporte_bajo_stock():
    limite = int(input("Ingrese la cantidad a buscar: "))
    #Hace la busqueda, verificar si es menor o menor igual
    cur.execute("SELECT * FROM productos WHERE cantidad < ?", (limite,))
    productos = cur.fetchall()
    #Trae todo producto solicitado por el usuario
    if productos:
        print("Estos son los productos que deberia reponer lo antes posible")
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]} | Categoría: {producto[4]}")
    else:
        print("Genial! No hay productos con bajo stock\n")


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
        print("Nos vemos!")
        conexion.close()
        break

