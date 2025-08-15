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
menu = MENU()
allow = False
try:
    while allow == False:
        menu.Menu()
        opt = input("Ingrese la opción que desee: ")
        match opt:
            case "1":
                cont = 0
                num = int(input("Cuantos productos desea ingresar? "))
                if num < 1 or num > 10:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(num):
                        prin("")
                       print(f"Ingreso del producto: {i}")

            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Tipo de dato incorrecto")
    #El try lo puse nomás para que se guíe jaja no está al 100