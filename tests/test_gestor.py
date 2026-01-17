# tests/test_gestor.py
import unittest
from contactos.gestor import GestorContactos
from contactos.contacto import Contacto

class TestGestor(unittest.TestCase):
    def setUp(self):
        """Configuración inicial antes de cada test"""
        self.g = GestorContactos()

    # ===== PRUEBAS DE CREACIÓN (CREATE) =====
    def test_registrar(self):
        """Test 1: Registrar un contacto correctamente"""
        c = self.g.registrar("Ana", "+56911111111", "ana@correo.com", "Calle 1")
        self.assertEqual(c.id, 1)
        self.assertEqual(c.nombre, "Ana")
        self.assertEqual(len(self.g.listar()), 1)

    def test_registrar_multiples(self):
        """Test 2: Registrar múltiples contactos"""
        c1 = self.g.registrar("Juan", "123456", "juan@correo.com", "Dir 1")
        c2 = self.g.registrar("Maria", "654321", "maria@correo.com", "Dir 2")
        self.assertEqual(c1.id, 1)
        self.assertEqual(c2.id, 2)
        self.assertEqual(len(self.g.listar()), 2)

    def test_registrar_telefono_invalido(self):
        """Test 3: Validar que rechaza teléfono inválido"""
        with self.assertRaises(ValueError):
            self.g.registrar("Pedro", "123", "pedro@correo.com", "Dir 3")

    def test_registrar_correo_invalido(self):
        """Test 4: Validar que rechaza correo inválido"""
        with self.assertRaises(ValueError):
            self.g.registrar("Luis", "123456", "correo_invalido", "Dir 4")

    # ===== PRUEBAS DE LECTURA (READ) =====
    def test_listar_vacio(self):
        """Test 5: Listar cuando no hay contactos"""
        self.assertEqual(len(self.g.listar()), 0)

    def test_listar_con_datos(self):
        """Test 6: Listar contactos existentes"""
        self.g.registrar("Ana", "123456", "ana@correo.com", "Dir 1")
        self.g.registrar("Juan", "654321", "juan@correo.com", "Dir 2")
        lista = self.g.listar()
        self.assertEqual(len(lista), 2)

    def test_buscar(self):
        """Test 7: Buscar contacto por nombre"""
        self.g.registrar("Juan", "123456", "j@c.com", "D1")
        res = self.g.buscar("Juan")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].nombre, "Juan")

    def test_buscar_por_telefono(self):
        """Test 8: Buscar contacto por teléfono"""
        self.g.registrar("Maria", "999888", "maria@correo.com", "Dir 1")
        res = self.g.buscar("999888")
        self.assertEqual(len(res), 1)

    def test_buscar_sin_resultados(self):
        """Test 9: Buscar contacto inexistente"""
        self.g.registrar("Ana", "123456", "ana@correo.com", "Dir 1")
        res = self.g.buscar("Pedro")
        self.assertEqual(len(res), 0)

    # ===== PRUEBAS DE ACTUALIZACIÓN (UPDATE) =====
    def test_editar_nombre(self):
        """Test 10: Editar nombre de contacto"""
        c = self.g.registrar("Juan", "123456", "juan@correo.com", "Dir 1")
        c_editado = self.g.editar(c.id, nombre="Juan Carlos")
        self.assertEqual(c_editado.nombre, "Juan Carlos")
        self.assertEqual(c_editado.telefono, "123456")

    def test_editar_telefono(self):
        """Test 11: Editar teléfono de contacto"""
        c = self.g.registrar("Maria", "123456", "maria@correo.com", "Dir 1")
        c_editado = self.g.editar(c.id, telefono="999888777")
        self.assertEqual(c_editado.telefono, "999888777")

    def test_editar_correo(self):
        """Test 12: Editar correo de contacto"""
        c = self.g.registrar("Pedro", "123456", "pedro@correo.com", "Dir 1")
        c_editado = self.g.editar(c.id, correo="nuevo@correo.com")
        self.assertEqual(c_editado.correo, "nuevo@correo.com")

    def test_editar_id_inexistente(self):
        """Test 13: Intentar editar contacto inexistente"""
        with self.assertRaises(KeyError):
            self.g.editar(999, nombre="Test")

    # ===== PRUEBAS DE ELIMINACIÓN (DELETE) =====
    def test_eliminar(self):
        """Test 14: Eliminar un contacto"""
        c = self.g.registrar("Ana", "123456", "ana@correo.com", "Dir 1")
        self.g.eliminar(c.id)
        self.assertEqual(len(self.g.listar()), 0)

    def test_eliminar_id_inexistente(self):
        """Test 15: Intentar eliminar contacto inexistente"""
        with self.assertRaises(KeyError):
            self.g.eliminar(999)

    # ===== PRUEBAS DE PERSISTENCIA (JSON) =====
    def test_guardar_y_cargar_json(self):
        """Test 16: Guardar y cargar contactos desde JSON"""
        import tempfile
        import os
        
        # Crear archivo temporal
        fd, temp_file = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        
        try:
            # Registrar contactos y guardar
            self.g.registrar("Juan", "123456", "juan@correo.com", "Dir 1")
            self.g.registrar("Maria", "654321", "maria@correo.com", "Dir 2")
            self.g.guardar_json(temp_file)
            
            # Crear nuevo gestor y cargar
            g2 = GestorContactos()
            g2.cargar_json(temp_file)
            
            # Verificar que se cargaron correctamente
            self.assertEqual(len(g2.listar()), 2)
            self.assertEqual(g2.listar()[0].nombre, "Juan")
        finally:
            # Limpiar archivo temporal
            if os.path.exists(temp_file):
                os.remove(temp_file)

if __name__ == "__main__":
    unittest.main()
