# gestor.py
# Clase que gestiona las operaciones CRUD de contactos
from contactos.contacto import Contacto
import os, json

class GestorContactos:
    """Gestiona la colección de contactos y operaciones sobre ellos"""
    
    def __init__(self):
        """Inicializa el gestor con una lista vacía"""
        self._contactos = []  # Lista de contactos (diccionarios)
        self._idx = {}        # Índice para búsqueda rápida por ID
        self._next_id = 1     # Próximo ID a asignar

    def _reindexar(self):
        """Actualiza el índice de IDs y calcula el siguiente ID disponible"""
        self._idx = {c["id"]: i for i, c in enumerate(self._contactos)}
        self._next_id = max(self._idx.keys(), default=0) + 1

    def registrar(self, nombre, telefono, correo, direccion):
        """Registra un nuevo contacto y lo agrega a la lista"""
        c = Contacto(self._next_id, nombre, telefono, correo, direccion)
        self._contactos.append(c.to_dict())
        self._reindexar()
        return c

    def listar(self):
        """Devuelve todos los contactos"""
        return [Contacto.from_dict(c) for c in self._contactos]

    def buscar(self, term):
        """Busca contactos por nombre o teléfono"""
        term = term.lower()
        return [
            Contacto.from_dict(c)
            for c in self._contactos
            if term in c["nombre"].lower() or term in c["telefono"]
        ]

    def obtener(self, cid):
        """Obtiene un contacto específico por su ID"""
        return Contacto.from_dict(self._contactos[self._idx[cid]])

    def editar(self, cid, **kwargs):
        """Edita los campos de un contacto existente"""
        pos = self._idx[cid]
        actual = Contacto.from_dict(self._contactos[pos])
        for key, value in kwargs.items():
            if value is not None:
                setattr(actual, key, value)
        self._contactos[pos] = actual.to_dict()
        return actual

    def eliminar(self, cid):
        """Elimina un contacto por su ID"""
        pos = self._idx[cid]
        self._contactos.pop(pos)
        self._reindexar()

    def guardar_json(self, ruta):
        """Guarda los contactos en un archivo JSON"""
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf8") as f:
            json.dump(self._contactos, f, indent=2, ensure_ascii=False)

    def cargar_json(self, ruta):
        """Carga los contactos desde un archivo JSON"""
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf8") as f:
                self._contactos = json.load(f)
            self._reindexar()
