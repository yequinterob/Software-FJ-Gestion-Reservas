
"""
Módulo de gestión de clientes
Proyecto: Software FJ
"""

import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        """Verifica que los datos del cliente sean correctos."""

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise DatosInvalidosError("El nombre del cliente es obligatorio.")

        if not re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.-]+", self.__correo):
            raise DatosInvalidosError("El correo electrónico no es válido.")

        if not self.__telefono.isdigit() or len(self.__telefono) < 7:
            raise DatosInvalidosError("El teléfono debe contener al menos 7 dígitos.")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        """Muestra la información del cliente."""

        return (
            f"Identificación: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
