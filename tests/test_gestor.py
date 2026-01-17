# tests/test_gestor.py
import unittest
from contactos.gestor import GestorContactos

class TestGestor(unittest.TestCase):
    def setUp(self):
        self.g = GestorContactos()

    def test_registrar(self):
        c = self.g.registrar("Ana", "+56911111111", "ana@correo.com", "Calle 1")
        self.assertEqual(c.id, 1)

    def test_buscar(self):
        self.g.registrar("Juan", "123456", "j@c.com", "D1")
        res = self.g.buscar("Juan")
        self.assertEqual(len(res), 1)

if __name__ == "__main__":
    unittest.main()
