class MENU:
    def Menu(self):
        print("Bienvenido al inventario BingBong")
        print("1.Registrar producto")
        print("2.Mostrar productos registrados")
        print("3.Bucar productos registrados")
        print("4.Administración de productos")
        print("5.Salir")
    def Q_S_Menu(self):
        print("Mostrar productos ordenados(presione X para salir)")
        print("de que forma desea ordenar los productos? ")
        print("1.Por nombre")
        print("2.Por stock")
        print("3.Por precio")
class Producto:
    def __init__(self, codigo,nombre,categoria, stock, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio
class Mod_Producto:
    def __init__(self):
        self.productos = {}
    def Agregar_producto(self, producto):
        self.productos[producto.codigo] = {'Nombre': producto.nombre,'Categoria':producto.categoria,
                                           'Stock':producto.stock,'Precio':producto.precio}
    def Mostrar(self):
        for codigo, producto in self.productos.items():
            print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                  f" Stock {producto['Stock']} Precio {producto['Precio']}")
    def Busqueda(self):
        encontrar = "-2"
        cont = 0
        cont1 = 0
        if len(self.productos) < 1:
            return "-1"
        else:
            buscar = input("ingrese el código/nombre/categoria del producto que busca: ")
            for codigo, producto in self.productos.items():
                if buscar == producto.codigo:
                    encontrar = producto.codigo
                    return encontrar
            for codigo, producto in self.productos.items():
                if buscar.lower() == producto['Categoria'].lower():
                    print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                          f" Stock {producto['Stock']} Precio {producto['Precio']}")
                    cont = cont + 1
            print(f"Se han encontrado {cont} coincidencias en categoría")
            print(" ")
            for codigo, producto in self.productos.items():
                if buscar.lower() == producto['Nombre'].lower():
                    print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                          f" Stock {producto['Stock']} Precio {producto['Precio']}")
                    cont1 = cont1 + 1
            print(f"Se han encontrado {cont1} coincidencias en nombre")
            encontrar = "-1"
            return encontrar
menu = MENU()
mod = Mod_Producto()
allow = False
try:
    while allow == False:
        menu.Menu()
        opt = input("Ingrese la opción que desee: ")
        match opt:
            case "1":
                #Ahora solo voy a hacer el ingreso imaginando que todo está bien y cuando ya funcione
                # le agregamos lo de que no permita dejar espacios vacios y así
                cont = 0
                num = int(input("Cuantos productos desea ingresar? "))
                if num < 1 or num > 10:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(num):
                        print(" ")
                        print(f"Ingreso del producto: {i}")
                        nombre = input("Ingrese el nombre del producto: ")
                        categoría = input("Ingrese la categoria del producto: ")
                        stock = int(input("Ingrese el stock del producto: "))
                        if stock < 1:
                            print("Cantidad invalida")
                        else:
                            precio = int(input("Ingrese el precio del producto: "))
                            if precio <= 0:
                                print("Valor invalido")
                            else:
                                codigo = f"P{cont}"
                                producto = Producto(codigo,nombre,categoría,stock,precio)
                                mod.Agregar_producto(producto)
                                cont = cont + 1
            case "2":
                mod.Mostrar()
            case "3":
                encontrar = mod.Busqueda()
                if encontrar == "-2":
                    print("No hay datos para buscar")
                    #No pude probar la busqueda al 100 pero yo creo que jala jaja
            case "4":
                pass
            case "5":
                pass
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Tipo de dato incorrecto")
    #El try lo puse nomás para que se guíe jaja no está al 100