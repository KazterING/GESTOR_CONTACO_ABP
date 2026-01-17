# main.py
# Interfaz de línea de comandos para el sistema de gestión de contactos
from contactos.gestor import GestorContactos

# Archivo donde se guardan los contactos
DATA_FILE = "data/contactos.json"

def pedir(msg):
    """Solicita entrada del usuario y elimina espacios"""
    return input(msg).strip()

def menu():
    """Función principal que muestra el menú y gestiona las opciones"""
    g = GestorContactos()
    g.cargar_json(DATA_FILE)  # Carga contactos al iniciar

    while True:
        # Muestra el menú principal
        print("\n" + "="*50)
        print("SISTEMA DE GESTION DE CONTACTOS")
        print("="*50)
        print("1) Registrar contacto")
        print("2) Editar contacto")
        print("3) Eliminar contacto")
        print("4) Buscar contacto")
        print("5) Listar todos")
        print("6) Salir")
        print("="*50)
        op = pedir("Selecciona una opcion: ")

        # Opción 1: Registrar nuevo contacto
        if op == "1":
            try:
                c = g.registrar(
                    pedir("Nombre: "),
                    pedir("Teléfono: "),
                    pedir("Correo: "),
                    pedir("Dirección: ")
                )
                g.guardar_json(DATA_FILE)
                print("Contacto registrado exitosamente:", c)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # Opción 2: Editar contacto existente
        elif op == "2":
            try:
                print("\n--- EDITAR CONTACTO ---")
                id_input = pedir("ID del contacto a editar: ")
                if not id_input:
                    print("Error: Debe ingresar un ID válido.")
                    continue
                cid = int(id_input)
                print("\nNota: Si no desea cambiar un campo, déjelo en blanco y presione Enter.\n")
                c = g.editar(
                    cid,
                    nombre=pedir("Nuevo nombre: ") or None,
                    telefono=pedir("Nuevo teléfono: ") or None,
                    correo=pedir("Nuevo correo: ") or None,
                    direccion=pedir("Nueva dirección: ") or None
                )
                g.guardar_json(DATA_FILE)
                print("Contacto editado exitosamente:", c)
            except ValueError as e:
                print(f"Error: {e}")
            except KeyError:
                print("Error: No existe un contacto con ese ID.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # Opción 3: Eliminar contacto
        elif op == "3":
            try:
                cid = int(pedir("ID: "))
                g.eliminar(cid)
                g.guardar_json(DATA_FILE)
                print("Contacto eliminado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")
            except KeyError:
                print("Error: No existe un contacto con ese ID.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # Opción 4: Buscar contacto por nombre o teléfono
        elif op == "4":
            res = g.buscar(pedir("Buscar: "))
            if res:
                print(f"\nSe encontraron {len(res)} contacto(s):")
                for c in res:
                    print(f"  - {c}")
            else:
                print("No se encontraron contactos con ese criterio.")

        # Opción 5: Listar todos los contactos
        elif op == "5":
            contactos = g.listar()
            if contactos:
                print(f"\nTotal de contactos: {len(contactos)}")
                for c in contactos:
                    print(f"  - {c}")
            else:
                print("No hay contactos registrados.")

        # Opción 6: Salir del programa
        elif op == "6":
            print("Hasta luego!")
            break
        
        # Opción inválida
        else:
            print("Opcion invalida. Por favor, selecciona una opcion del 1 al 6.")

if __name__ == "__main__":
    menu()  # Inicia el programa
