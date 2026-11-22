
"""
Módulo de excepciones personalizadas
Proyecto: Software FJ
"""

class ErrorSistema(Exception):
    """Excepción base del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se genera cuando un cliente no existe."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta inconsistencias."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass
 
