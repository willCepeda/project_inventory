# Definition the Producto class
class Producto:

    # Definition of a constructor
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre     = nombre
        self.__categoria  = categoria
        self.set_precio(precio) # We use the setter to validate the price
        self.set_cantidad(cantidad) # We use the setter to validate the amount

    #Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return  self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    #Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self, precio):
        try:
            if precio >0 :
                self.__precio = precio
            else:
                raise ValueError("El precio debe ser mayor que 0")
        except ValueError as e:
            print(f"Error al establecer el precio: {e}")  #Print the price must be greater than 0
    def set_cantidad(self, cantidad):
        try:
            if cantidad >=0 :
                self.__cantidad = cantidad
            else:
                raise ValueError("La cantidad debe ser mayor o igual a 0")
        except ValueError as e:
            print(f"Error al establecer la cantidad: {e}") #Print the amount must be greater than or equal 0


    def __str__(self):
        return (f"Producto: {self.__nombre}, Precio: {self.__precio}€, Cantidad: {self.__cantidad}, Categoria: {self.__categoria}")

# Definition the Inventario class
class Inventario:

    def __init__(self):
        self.productos = [] #List for save object of type Product

    #
    def agregar_un_producto(self, producto):
        # Verify that the product is not exist
        self.productos.append(producto)

    def actualizar_un_producto(self,nombre_producto ,nuevo_precio=None, nueva_cantidad=None):
        # Verify that the product exist
        for producto in self.productos:
            if producto.get_nombre() == nombre_producto:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                print(f"Producto {producto.get_nombre()} actualizado: Precio: {producto.get_precio()}€, Cantidad: {producto.get_cantidad()}" )
                return
        print(f"Producto '{nombre_producto}' no encontrado en el inventario")


    # method to delete product by the name
    def eliminar_un_producto(self, nombre):

        for producto in self.productos:
            if producto.get_nombre() == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario")
                return

        print(f"Producto '{nombre}' no encontrado en el inventario")
   # method to list of all product
    def mostrar_inventario(self):
        indice=0
        for producto in self.productos:
            if producto.get_cantidad() >0 :
                indice = indice + 1
                print(f"{indice}.- {producto}")


        if indice == 0:
            print("No hay productos disponibles por el momento")

    def buscar_un_producto(self, nombre):
        for producto in self.productos:
            if producto.get_nombre() == nombre:
                print(f"Detalles del producto: {producto.get_nombre()} ")
                print(f"Categoria: {producto.get_categoria()} ")
                print(f"Precio: {producto.get_precio()}")
                print(f"Cantidad: {producto.get_cantidad()}")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario")

def Menu():
    # Creation of inventory
    mi_inventario = Inventario()
    print("--Welcome to Inventory of Products--")
    while True:
        print("Elige una opcion:")
        print("1.- Crear producto")
        print("2.- Actualizar producto")
        print("3.- Eliminar producto")
        print("4.- Buscar producto")
        print("5.- Mostar inventario")
        print("0.- Salir")

        opcion = int(input("Selecciona una opción: "))
        if opcion == 1: # Create a new product
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            categoria = input("Categoría del producto: ")
            #Create the product
            nuevo_producto = Producto(nombre,categoria,precio,cantidad)
            # Add the product to the inventory
            mi_inventario.agregar_un_producto(nuevo_producto)

        elif opcion == 2: # Update a product
            nombre = input("Nombre del producto a actualizar:")
            nuevo_precio = input("Nuevo precio (deja en blanco para no cambiar el precio): ")
            nueva_cantidad = input("Nueva cantidad (deja en blanco para no cambiar la cantidad): ")
            # We convert values to numeric type only if they were entered
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            mi_inventario.actualizar_un_producto(nombre, nuevo_precio,nueva_cantidad)

        elif opcion == 3: # Delete a product
            nombre = input("Nombre del producto a eliminar: ")
            mi_inventario.eliminar_un_producto(nombre)

        elif opcion == 4: #Search a product
            nombre = input("Nombre del producto a buscar: ")
            mi_inventario.buscar_un_producto(nombre)

        elif opcion == 5: #Show all the products of inventory
            mi_inventario.mostrar_inventario()

        elif opcion == 0: #Finish the program
            print("Saliendo del programa - !Hasta pronto¡")
            break
        else:
            print("Opción no válida. Inténtelo nuevamente")

#Main
Menu()



