# cli.py
from contactos.gestor import GestorContactos

DATA_FILE = "data/contactos.json"

def pedir(msg):
    return input(msg).strip()

def menu():
    g = GestorContactos()
    g.cargar_json(DATA_FILE)

    while True:
        print("\n" + "="*50)
        print("📇 SISTEMA DE GESTIÓN DE CONTACTOS")
        print("="*50)
        print("1) 📝 Registrar contacto")
        print("2) ✏️  Editar contacto")
        print("3) 🗑️  Eliminar contacto")
        print("4) 🔍 Buscar contacto")
        print("5) 📋 Listar todos")
        print("6) 🚪 Salir")
        print("="*50)
        op = pedir("👉 Selecciona una opción: ")

        if op == "1":
            try:
                c = g.registrar(
                    pedir("Nombre: "),
                    pedir("Teléfono: "),
                    pedir("Correo: "),
                    pedir("Dirección: ")
                )
                g.guardar_json(DATA_FILE)
                print("✅ Contacto registrado exitosamente:", c)
            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        elif op == "2":
            try:
                cid = int(pedir("ID: "))
                c = g.editar(
                    cid,
                    nombre=pedir("Nuevo nombre: ") or None,
                    telefono=pedir("Nuevo teléfono: ") or None,
                    correo=pedir("Nuevo correo: ") or None,
                    direccion=pedir("Nueva dirección: ") or None
                )
                g.guardar_json(DATA_FILE)
                print("✅ Contacto editado exitosamente:", c)
            except ValueError as e:
                print(f"❌ Error: {e}")
            except KeyError:
                print("❌ Error: No existe un contacto con ese ID.")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        elif op == "3":
            try:
                cid = int(pedir("ID: "))
                g.eliminar(cid)
                g.guardar_json(DATA_FILE)
                print("✅ Contacto eliminado exitosamente.")
            except ValueError as e:
                print(f"❌ Error: {e}")
            except KeyError:
                print("❌ Error: No existe un contacto con ese ID.")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        elif op == "4":
            res = g.buscar(pedir("Buscar: "))
            if res:
                print(f"\n📋 Se encontraron {len(res)} contacto(s):")
                for c in res:
                    print(f"  • {c}")
            else:
                print("❌ No se encontraron contactos con ese criterio.")

        elif op == "5":
            contactos = g.listar()
            if contactos:
                print(f"\n📋 Total de contactos: {len(contactos)}")
                for c in contactos:
                    print(f"  • {c}")
            else:
                print("📭 No hay contactos registrados.")

        elif op == "6":
            print("👋 ¡Hasta luego!")
            break
        
        else:
            print("⚠️  Opción inválida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    menu()
