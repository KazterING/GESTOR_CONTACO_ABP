# contacto.py
from __future__ import annotations
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Contacto:
    def __init__(self, id: int, nombre: str, telefono: str, correo: str, direccion: str):
        self.__id = int(id)
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        value = value.strip()
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = value

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        value = value.strip()
        normalized = value.replace(" ", "").replace("-", "")
        if not re.fullmatch(r"\+?\d{6,15}", normalized):
            raise ValueError("Teléfono inválido. Debe contener entre 6 y 15 dígitos (puede incluir '+' al inicio).")
        self.__telefono = value

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, value):
        value = value.strip()
        if not _EMAIL_RE.match(value):
            raise ValueError("Correo inválido. Debe tener el formato: usuario@dominio.extension (ejemplo: usuario@gmail.com)")
        self.__correo = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Dirección inválida.")
        self.__direccion = value

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion,
        }

    @staticmethod
    def from_dict(d):
        return Contacto(d["id"], d["nombre"], d["telefono"], d["correo"], d["direccion"])
