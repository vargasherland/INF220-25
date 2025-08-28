# Estructuras estáticas
# listas, tuplas y diccionarios
""" Ejemplo de estructura estática: usando
    listas, tuplas y diccionarios.
    En esta ocasión solamente usaré algunos
    elementos de cada estructura.
    Diccionario de 3 productos con su nombre, precio
    y cantidad disponible.
"""
Producto = {
    'P001': {'nombre': 'Laptop HP 15',
             'precio': 1200,
             'cantidad': 10},
    'P002': {'nombre': 'Mouse Inalámbrico',
             'precio': 25,
             'cantidad': 50},
    'P003': {'nombre': 'Teclado Mecánico',
             'precio': 80,
             'cantidad': 15}
}


def mostrar_productos():
    """Función para mostrar los productos"""
    print('\n Los productos disponibles son:')
    print('#' * 40)
    for clave, valor in Producto.items():
        print(f'Código: {clave}')
        print(f'  Nombre: {valor["nombre"]}')
        print(f'  Precio: ${valor["precio"]}')
        print(f'  Cantidad: {valor["cantidad"]}')
        print('-' * 40)


def comprar_producto():
    """Función para comprar un producto"""
    codigo = input("Ingresa el código del producto a comprar: ")
    
    if codigo in Producto:
        if Producto[codigo]['cantidad'] > 0:
            Producto[codigo]['cantidad'] -= 1
            print(f"✅ Compra exitosa de: {Producto[codigo]['nombre']}")
            print(f"   Precio: ${Producto[codigo]['precio']}")
            print(f"   Cantidad restante: {Producto[codigo]['cantidad']}")
        else:
            print("❌ No hay stock disponible")
    else:
        print("❌ Código no válido")


def main():
    """Función principal donde voy a elegir el producto
    que quiero comprar y luego mostrar el stock
    """
    print("🛍️ SISTEMA DE PRODUCTOS")
    print("=" * 20)
    
    while True:
        print("\nOpciones:")
        print("1. Ver productos")
        print("2. Comprar producto") 
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            comprar_producto()
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida")


if __name__ == '__main__':
    main()
