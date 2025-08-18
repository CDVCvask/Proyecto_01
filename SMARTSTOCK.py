class MENU:
    def Menu(self):
        print("\nBienvenido al inventario BingBong")
        print("1.Registrar producto")
        print("2.Mostrar productos registrados y ordenarlos")
        print("3.Bucar productos registrados")
        print("4.Administración de productos")
        print("5.Salir")
    def Q_S_Menu(self):
        print("\nDe que forma desea ordenar los productos? ")
        print("1.Por nombre")
        print("2.Por stock")
        print("3.Por precio")
        print("4.Volver al menú principal")
    def Administracion_Menu(self):
        print("1.Vender productos")
        print("2.Cambiar precios")
        print("3.Eliminar productos")
        print("4.Mostrar ganancia de ventas")
        print("5.Volver al menú principal")
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
        self.productos[producto.codigo] = {'Nombre': producto.nombre,'Categoria':producto.categoria,'Stock': producto.stock,
                                           'Precio': producto.precio}
    def Mostrar(self):
        for codigo, producto in self.productos.items():
            print(f"\nCodigo: {codigo}, Nombre:{producto['Nombre']}, Categoría: {producto['Categoria']}")
            print(f"Stock {producto['Stock']} Precio {producto['Precio']}")
    def Revisar(self):
        if len(self.productos) < 1:
            return -1
        else:
            return 1
    def Busqueda(self):
        encontrar = "-2"
        cont = 0
        cont1 = 0
        if len(self.productos) < 1:
            return "-2"
        else:
            buscar = input("ingrese el código/nombre/categoria del producto que busca: ")
            for codigo, producto in self.productos.items():
                if buscar == codigo:
                    print("Producto encontrado")
                    print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                          f" Stock {producto['Stock']} Precio {producto['Precio']}")
                    encontrar = codigo
                    return encontrar
            for codigo, producto in self.productos.items():
                if buscar.lower() == producto['Categoria'].lower():
                    print("Producto encontrado")
                    print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                          f" Stock {producto['Stock']} Precio {producto['Precio']}")
                    cont = cont + 1
            print(f"Se han encontrado {cont} coincidencias en categoría")
            print(" ")

            for codigo, producto in self.productos.items():
                if buscar.lower() == producto['Nombre'].lower():
                    print("Producto encontrado")
                    print(f"Código: {codigo}, Nombre: {producto['Nombre']} Categoría: {producto['Categoria']}"
                          f" Stock {producto['Stock']} Precio {producto['Precio']}")
                    cont1 = cont1 + 1
            print(f"Se han encontrado {cont1} coincidencias en nombre")
            encontrar = "-1"
            return encontrar

    def Q_S_Nombre(self, productos=None):
        if productos == None:
            productos = self.productos
        piv = ""
        lower = {}
        same = {}
        upper = {}
        if len(productos) <= 1:
            return productos
        else:
            for key, value in productos.items():
                piv = value['Nombre']
                break
            for key, value in productos.items():
                if value['Nombre'] < piv:
                    lower[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Nombre'] == piv:
                    same[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                 'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Nombre'] > piv:
                    upper[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
            return {**self.Q_S_Nombre(lower), **same, **self.Q_S_Nombre(upper)}

    def Q_S_Stock(self, productos=None):
        if productos == None:
            productos = self.productos
        piv = ""
        lower = {}
        same = {}
        upper = {}
        if len(productos) <= 1:
            return productos
        else:
            for key, value in productos.items():
                piv = value['Stock']
                break
            for key, value in productos.items():
                if value['Stock'] < piv:
                    lower[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Stock'] == piv:
                    same[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                 'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Stock'] > piv:
                    upper[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
            return {**self.Q_S_Stock(upper), **same, **self.Q_S_Stock(lower)}

    def Q_S_Precio(self, productos=None):
        if productos == None:
            productos = self.productos
        piv = ""
        lower = {}
        same = {}
        upper = {}
        if len(productos) <= 1:
            return productos
        else:
            for key, value in productos.items():
                piv = value['Precio']
                break
            for key, value in productos.items():
                if value['Precio'] < piv:
                    lower[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Precio'] == piv:
                    same[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                 'Stock': value['Stock'], 'Precio': value['Precio']}
                if value['Precio'] > piv:
                    upper[key] = {'Nombre': value['Nombre'], 'Categoria': value['Categoria'],
                                  'Stock': value['Stock'], 'Precio': value['Precio']}
            return {**self.Q_S_Precio(upper), **same, **self.Q_S_Precio(lower)}


class Administracion_productos:
    def __init__(self, mod_productos):
        self.mod = mod_productos
        self.ganancias=0

    def Eliminar(self):
        print("Eliminar productos en su totalidad")
        codigo = input("\nIngrese el codigo del producto que desea eliminar: ")
        if codigo in self.mod.productos:
            print("Producto encontrado exitosamente")
            print("Eliminando producto...")
            del self.mod.productos[codigo]
            print("\nProducto eliminado exitosamente")
            input("Preione Enter para continuar")
        else:
            print("El codigo ingresado no pertenece a ningún producto")
    def Vender(self):
        codigo = input("\nIngrese el codigo del producto que desea vender: ")
        if codigo in self.mod.productos:
            print("Producto encontrado exitosamente")
            cantidad=int(input("\nIngrese la cantidad de productos que desea vender:"))
            if cantidad <=0:
                print("Cantidad invalida")
            elif cantidad>self.mod.productos[codigo]['Stock']:
                print("No hay suficientes productos para realizar la venta")
            else:
                self.mod.productos[codigo]['Stock'] -= cantidad

                precio_unitario = self.mod.productos[codigo]['Precio']
                total_venta = cantidad * precio_unitario
                self.ganancias += total_venta
                print("Venta realizada exitosamente")
                print(f"Nueva cantidad de productos disponibles: {self.mod.productos[codigo]['Stock']}")
                print(f"Ganancia de esta venta: {total_venta}")
                print(f"Ganancia acumulada: {self.ganancias}")
                input("Preione Enter para continuar")
        else:
            print("El codigo ingresado no pertenece a ningún producto")
    def CambiarPrecios(self):
        codigo = input("Ingrese el codigo del producto al cual se le cambiara el precio: ")
        if codigo in self.mod.productos:
            print("")
            precio_nuevo= int(input("\nIngrese el nuevo precio: "))
            if precio_nuevo <= 0:
                print("Precio invalido")
            else:
                self.mod.productos[codigo]["Precio"]=precio_nuevo
                print("Precio actualizado")
                print(f"Ahora su precio sera de {precio_nuevo}")
                input("Preione Enter para continuar")
        else:
            print("El codigo ingresado no pertenece a ningún producto")

menu = MENU()
mod = Mod_Producto()
admin = Administracion_productos(mod)
allow = False
cont = 0
while allow == False:
    try:
        menu.Menu()
        opt = input("Ingrese la opción que desee (Use unicamente números enteros): ")
        match opt:
            case "1":
                #Ahora solo voy a hacer el ingreso imaginando que todo está bien y cuando ya funcione
                # le agregamos lo de que no permita dejar espacios vacios y así
                print("\nREGISTRO DE PRODUCTOS")
                num = int(input("Cuantos productos desea ingresar (Use unicamente números enteros): ? "))
                if num < 1 or num > 10:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(num):
                        while 0 != 1:
                            print(" ")
                            print(f"Ingreso del producto: {i+1}")
                            nombre = input("Ingrese el nombre del producto: ")
                            if nombre == "":
                                print("No puede dejar este espacio vacio")
                            else:
                                categoría = input("Ingrese la categoria del producto: ")
                                if categoría == "":
                                    print("No puede dejar este espacio vacio")
                                else:
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
                                            print("Producto agregado exitosamente")
                                            break
                    print("Voliendo al menú principal...")
                    input("Preione Enter para continuar")
            case "2":
                check = mod.Revisar()
                if check == -1:
                    print("No hay ningún dato que mostrar")
                else:
                    while True:
                        print("\nPRODUCTOS DISPONIBLES")
                        menu.Q_S_Menu()
                        opt1 = input("Ingrese la forma en que desea ordenar los productos: ")
                        if opt1 in ["1", "2","3","4"]:
                            match opt1:
                                case "1":
                                    ordenado = mod.Q_S_Nombre()
                                    for codigo,producto in ordenado.items():
                                        print(f"Código: {codigo}, Nombre: {producto['Nombre']} "
                                            f"Categoría: {producto['Categoria']}"  f" Stock {producto['Stock']}"
                                            f" Precio {producto['Precio']}")
                                    input("Preione Enter para continuar")
                                case "2":
                                    ordenado = mod.Q_S_Stock()
                                    for codigo,producto in ordenado.items():
                                        print(f"Código: {codigo}, Nombre: {producto['Nombre']} "
                                            f"Categoría: {producto['Categoria']}"  f" Stock {producto['Stock']}"
                                            f" Precio {producto['Precio']}")
                                    input("Preione Enter para continuar")
                                case "3":
                                    ordenado = mod.Q_S_Precio()
                                    for codigo, producto in ordenado.items():
                                        print(f"Código: {codigo}, Nombre: {producto['Nombre']} "
                                            f"Categoría: {producto['Categoria']}"  f" Stock {producto['Stock']}"
                                            f" Precio {producto['Precio']}")
                                    input("Preione Enter para continuar")
                                case "4":
                                    print("Voliendo al menú principal...")
                                    input("Preione Enter para continuar")
                                    break
                        else:
                            print("Opcion invalida")
            case "3":
                check = mod.Revisar()
                if check == -1:
                    print("No hay ningún dato que buscar")
                else:
                    print("\nBUSQUEDA DE PRODUCTOS")
                    encontrar = mod.Busqueda()
                    if encontrar == "-2":
                        print("No hay datos para buscar")
                        #No pude probar la busqueda al 100 pero yo creo que jala jaja
                    print("Voliendo al menú principal...")
                    input("Preione Enter para continuar")
            case "4":
                check = mod.Revisar()
                if check == -1:
                    print("No hay ningún dato que administrar")
                else:
                    while True:
                        #aun falta la suma de los productos vendidos
                        #falta correcion de errores
                        print("\nADMINISTRACION DE PRODUCTOS")
                        mod.Mostrar()
                        menu.Administracion_Menu()
                        opcion=input("Elija la opcion que desee (Use unicamente números enteros): ")
                        if opcion in ["1", "2", "3", "4","5"]:
                            match opcion:
                                case "1":
                                    admin.Vender()
                                case "2":
                                    admin.CambiarPrecios()
                                case "3":
                                    admin.Eliminar()
                                case "4":
                                    print(f"Ganancias acumuladas: {admin.ganancias}")
                                    input("Preione Enter para continuar")
                                case "5":
                                    print("Voliendo al menú principal...")
                                    input("Preione Enter para continuar")
                                    break
                        else:
                            print("Opcion invalida")
            case "5":
                print("Saliendo del Menú")
                allow = True
            case _:
                print("La opción seleccionada no es valida")
    except ValueError:
        print("El tipo de dato ingresado no es valido")
    #El try lo puse nomás para que se guíe jaja no está al 100