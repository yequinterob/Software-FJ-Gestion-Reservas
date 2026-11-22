
"""
Módulo de gestión de servicios
Proyecto: Software FJ
"""

from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


class Servicio(Entidad):
    """
    Clase abstracta para los servicios ofrecidos
    por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa, disponible=True):

        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        if not isinstance(disponible, bool):
            raise DatosInvalidosError("La disponibilidad debe ser verdadera o falsa.")

        self.__nombre = nombre.strip()
        self.__tarifa = tarifa
        self.__disponible = disponible

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa(self):
        return self.__tarifa

    @property
    def disponible(self):
        return self.__disponible

    def cambiar_disponibilidad(self, estado):
        """Permite cambiar el estado del servicio."""

        if not isinstance(estado, bool):
            raise DatosInvalidosError("El estado debe ser booleano.")

        self.__disponible = estado

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo del servicio.
        Admite parámetros opcionales para impuestos y descuentos.
        """

        self.validar_parametros(duracion)

        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no está disponible."
            )

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        subtotal = self.__tarifa * duracion
        valor_descuento = subtotal * (descuento / 100)
        subtotal_con_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_con_descuento * (impuesto / 100)

        return round(subtotal_con_descuento + valor_impuesto, 2)

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parámetros específicos del servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describe las características del servicio."""
        pass

    def mostrar_informacion(self):
        return (
            f"Servicio: {self.__nombre}\n"
            f"Código: {self.identificador}\n"
            f"Tarifa por hora: ${self.__tarifa:,.2f}\n"
            f"Disponible: {'Sí' if self.__disponible else 'No'}"
        )


class ReservaSala(Servicio):
    """Servicio especializado en reservas de salas."""

    def __init__(self, identificador, nombre, tarifa, capacidad,
                 disponible=True):

        super().__init__(identificador, nombre, tarifa, disponible)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")

        self.capacidad = capacidad

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración de la reserva debe ser positiva.")

    def describir_servicio(self):

        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad máxima: {self.capacidad} personas."
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, identificador, nombre, tarifa, tipo_equipo,
                 disponible=True):

        super().__init__(identificador, nombre, tarifa, disponible)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("Debe especificar el tipo de equipo.")

        self.tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("Las horas de alquiler deben ser positivas.")

    def describir_servicio(self):

        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Tipo de equipo: {self.tipo_equipo}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesorías profesionales."""

    def __init__(self, identificador, nombre, tarifa, especialidad,
                 disponible=True):

        super().__init__(identificador, nombre, tarifa, disponible)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Debe especificar la especialidad.")

        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración de la asesoría debe ser positiva.")

    def describir_servicio(self):

        return (
            f"Asesoría especializada: {self.nombre}. "
            f"Especialidad: {self.especialidad}."
        )
