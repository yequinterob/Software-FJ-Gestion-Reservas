
"""
Módulo de gestión de reservas
Proyecto: Software FJ
"""

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError
)


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion):

        if not identificador:
            raise ReservaInvalidaError(
                "El identificador de la reserva es obligatorio."
            )

        if cliente is None:
            raise ReservaInvalidaError(
                "Debe asociar un cliente a la reserva."
            )

        if servicio is None:
            raise ReservaInvalidaError(
                "Debe seleccionar un servicio."
            )

        servicio.validar_parametros(duracion)

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self, impuesto=0, descuento=0):
        """Confirma la reserva y calcula su costo."""

        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

        except ServicioNoDisponibleError:
            raise

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible procesar el costo de la reserva."
            ) from error

        else:
            self.__estado = "Confirmada"
            return self.__costo

        finally:
            print(
                f"Proceso de confirmación finalizado: "
                f"Reserva {self.__identificador}"
            )

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise OperacionNoPermitidaError(
                "La reserva no se puede cancelar."
            )

        self.__estado = "Cancelada"

        return "Reserva cancelada correctamente."

    def procesar(self):
        """Procesa una reserva confirmada."""

        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        self.__estado = "Procesada"

        return "Reserva procesada correctamente."

    def mostrar_informacion(self):
        """Presenta los datos de la reserva."""

        return (
            f"\n--- INFORMACIÓN DE LA RESERVA ---\n"
            f"Código: {self.__identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}"
        )
