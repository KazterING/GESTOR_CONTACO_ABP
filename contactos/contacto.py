# contacto.py
# Clase que representa un contacto con validaciones
from __future__ import annotations
import re

# Expresión regular para validar formato de correo electrónico
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Contacto:
    """Clase que representa un contacto con sus datos y validaciones"""
    
    def __init__(self, id: int, nombre: str, telefono: str, correo: str, direccion: str):
        """Inicializa un contacto con sus datos"""
        self.__id = int(id)  # ID único e inmutable
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    @property
    def id(self):
        """Obtiene el ID del contacto (solo lectura)"""
        return self.__id

    @property
    def nombre(self):
        """Obtiene el nombre del contacto"""
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        """Valida y asigna el nombre (no puede estar vacío)"""
        value = value.strip()
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = value

    @property
    def telefono(self):
        """Obtiene el teléfono del contacto"""
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        """Valida y asigna el teléfono (debe tener 6-15 dígitos)"""
        value = value.strip()
        normalized = value.replace(" ", "").replace("-", "")
        if not re.fullmatch(r"\+?\d{6,15}", normalized):
            raise ValueError("Teléfono inválido. Debe contener al menos 6 dígitos(puede incluir '+' al inicio).")
        self.__telefono = value

    @property
    def correo(self):
        """Obtiene el correo del contacto"""
        return self.__correo

    @correo.setter
    def correo(self, value):
        """Valida y asigna el correo (debe tener formato válido)"""
        value = value.strip()
        if not _EMAIL_RE.match(value):
            raise ValueError("Correo inválido. Debe tener el formato: usuario@dominio.extension (ejemplo: usuario@gmail.com)")
        self.__correo = value

    @property
    def direccion(self):
        """Obtiene la dirección del contacto"""
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        """Valida y asigna la dirección (no puede estar vacía)"""
        value = value.strip()
        if not value:
            raise ValueError("Dirección inválida.")
        self.__direccion = value

    def __str__(self):
        """Representación en texto del contacto"""
        return f"[ID: {self.id}] {self.nombre} - Tel: {self.telefono} - Email: {self.correo} - Dir: {self.direccion}"

    def __repr__(self):
        """Representación técnica del contacto"""
        return f"Contacto(id={self.id}, nombre='{self.nombre}', telefono='{self.telefono}', correo='{self.correo}', direccion='{self.direccion}')"

    def to_dict(self):
        """Convierte el contacto a un diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion,
        }

    @staticmethod
    def from_dict(d):
        """Crea un contacto desde un diccionario"""
        return Contacto(d["id"], d["nombre"], d["telefono"], d["correo"], d["direccion"])
