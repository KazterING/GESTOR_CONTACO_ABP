# gestor.py
from contactos.contacto import Contacto
import os, json

class GestorContactos:
    def __init__(self):
        self._contactos = []
        self._idx = {}
        self._next_id = 1

    def _reindexar(self):
        self._idx = {c["id"]: i for i, c in enumerate(self._contactos)}
        self._next_id = max(self._idx.keys(), default=0) + 1

    def registrar(self, nombre, telefono, correo, direccion):
        c = Contacto(self._next_id, nombre, telefono, correo, direccion)
        self._contactos.append(c.to_dict())
        self._reindexar()
        return c

    def listar(self):
        return [Contacto.from_dict(c) for c in self._contactos]

    def buscar(self, term):
        term = term.lower()
        return [
            Contacto.from_dict(c)
            for c in self._contactos
            if term in c["nombre"].lower() or term in c["telefono"]
        ]

    def obtener(self, cid):
        return Contacto.from_dict(self._contactos[self._idx[cid]])

    def editar(self, cid, **kwargs):
        pos = self._idx[cid]
        actual = Contacto.from_dict(self._contactos[pos])
        for key, value in kwargs.items():
            if value is not None:
                setattr(actual, key, value)
        self._contactos[pos] = actual.to_dict()
        return actual

    def eliminar(self, cid):
        pos = self._idx[cid]
        self._contactos.pop(pos)
        self._reindexar()

    def guardar_json(self, ruta):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf8") as f:
            json.dump(self._contactos, f, indent=2, ensure_ascii=False)

    def cargar_json(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf8") as f:
                self._contactos = json.load(f)
            self._reindexar()
