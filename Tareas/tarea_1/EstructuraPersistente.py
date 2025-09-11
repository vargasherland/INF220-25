""" Importamos la librería json para manejar archivos JSON
    para más simplicidad en la persistencia de datos y de
    paso os para poder eliminar el json porque no es un
    archivo que nos interese en realidad.
"""
import json
import os


""" Programa que simula una lista de contactos persistente
    usando un archivo JSON.
"""

def cargar_contactos():
    """Carga los contactos desde el archivo JSON."""
    try:
        with open('contactos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_contactos(contactos):
    """Guarda los contactos en el archivo JSON."""
    with open('contactos.json', 'w') as archivo:
        json.dump(contactos, archivo, indent=4)


def eliminar_archivo():
    """Elimina el archivo JSON si existe."""
    if os.path.exists('contactos.json'):
        os.remove('contactos.json')
        print("🗑️ Archivo contactos.json eliminado")
    else:
        print("❌ El archivo no existe")


def agregar_contacto():
    """Agrega un nuevo contacto a la lista."""
    contacto = input("Nuevo contacto: ")
    contactos = cargar_contactos()
    contactos.append(contacto)
    guardar_contactos(contactos)
    print(f"✅ Contacto agregado: {contacto}")


def ver_contactos():
    """Muestra todos los contactos guardados."""
    contactos = cargar_contactos()
    print("\n📞 Lista de Contactos:")
    print("=" * 30)
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto}")
    print("=" * 30)


def main():
    """Función principal del programa."""
    print("✅ SISTEMA DE CONTACTOS PERSISTENTE")
    print("=" * 35)
    
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Eliminar archivo JSON")
        print("4. Salir")
        
        opcion = input("Seleccione opción (1-4): ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            eliminar_archivo()
        elif opcion == "4":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida")


if __name__ == '__main__':
    main()
