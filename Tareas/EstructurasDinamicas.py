# Estructura Dinámica - Lista de Tareas
tareas = []
""" programa que simula una lista de tareas 
    usando una lista dinámica.
"""

def agregar_tarea():
    """Función para agregar tareas a la lista."""
    tarea = input("Tarea a agregar: ")
    tareas.append(tarea)
    print(f"✅ '{tarea}' agregada")

def ver_tareas():
    """Función para mostrar todas las tareas."""
    print("\n📝 Lista de Tareas:", tareas)

def main():
    """Función principal del programa."""
    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            break

if __name__ == '__main__':
    main()
