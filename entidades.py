
"""
Módulo de entidades generales
Proyecto: Software FJ
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self.__identificador = identificador

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self.__identificador

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass
