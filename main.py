
"""
Programa principal
Sistema Integral de Gestion Software FJ

Ejecuta las simulaciones del sistema y demuestra
el funcionamiento de clientes, servicios y reservas.
"""

from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from gestor import GestorSistema

from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)


def ejecutar_prueba(numero, descripcion, operacion, gestor):
    """
    Ejecuta una operación de forma controlada.
    Si ocurre un error, lo registra y continúa.
    """

    print("\n" + "=" * 65)
    print(f"SIMULACION {numero}: {descripcion}")
    print("=" * 65)

    try:
        resultado = operacion()

    except Exception as error:
        gestor.logger.exception(
            "Simulacion %s fallida: %s",
            numero,
            descripcion
        )
        print(f"ERROR CONTROLADO: {error}")

    else:
        print("RESULTADO:", resultado)
        gestor.logger.info(
            "Simulacion %s ejecutada correctamente: %s",
            numero,
            descripcion
        )


def ejecutar_sistema():

    print("\n")
    print("*" * 65)
    print("       SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("*" * 65)

    gestor = GestorSistema()

    # ------------------------------------------------
    # SIMULACIONES DE CLIENTES
    # ------------------------------------------------

    cliente1 = Cliente(
        "1001",
        "Carlos Ramirez",
        "carlos@gmail.com",
        "3001234567"
    )

    cliente2 = Cliente(
        "1002",
        "Maria Rodriguez",
        "maria@gmail.com",
        "3101234567"
    )

    ejecutar_prueba(
        1,
        "Registro de un cliente valido",
        lambda: gestor.registrar_cliente(cliente1),
        gestor
    )

    ejecutar_prueba(
        2,
        "Registro de un segundo cliente valido",
        lambda: gestor.registrar_cliente(cliente2),
        gestor
    )

    ejecutar_prueba(
        3,
        "Intento de registrar un cliente duplicado",
        lambda: gestor.registrar_cliente(cliente1),
        gestor
    )

    ejecutar_prueba(
        4,
        "Intento de crear un cliente con correo invalido",
        lambda: Cliente(
            "1003",
            "Pedro Gomez",
            "correo_incorrecto",
            "3201234567"
        ),
        gestor
    )

    # ------------------------------------------------
    # SIMULACIONES DE SERVICIOS
    # ------------------------------------------------

    sala = ReservaSala(
        "S01",
        "Sala de reuniones",
        50000,
        15
    )

    equipo = AlquilerEquipo(
        "E01",
        "Computador portatil",
        25000,
        "Equipo tecnologico"
    )

    asesoria = AsesoriaEspecializada(
        "A01",
        "Asesoria de software",
        80000,
        "Desarrollo de software"
    )

    servicio_no_disponible = AlquilerEquipo(
        "E02",
        "Proyector",
        30000,
        "Equipo audiovisual",
        False
    )

    ejecutar_prueba(
        5,
        "Registro de una sala de reuniones",
        lambda: gestor.registrar_servicio(sala),
        gestor
    )

    ejecutar_prueba(
        6,
        "Registro de un equipo tecnologico",
        lambda: gestor.registrar_servicio(equipo),
        gestor
    )

    ejecutar_prueba(
        7,
        "Registro de una asesoria especializada",
        lambda: gestor.registrar_servicio(asesoria),
        gestor
    )

    ejecutar_prueba(
        8,
        "Registro de un servicio no disponible",
        lambda: gestor.registrar_servicio(servicio_no_disponible),
        gestor
    )

    ejecutar_prueba(
        9,
        "Intento de crear un servicio con tarifa invalida",
        lambda: ReservaSala(
            "S02",
            "Sala invalida",
            -5000,
            10
        ),
        gestor
    )

    # ------------------------------------------------
    # SIMULACIONES DE RESERVAS
    # ------------------------------------------------

    ejecutar_prueba(
        10,
        "Creacion de una reserva valida",
        lambda: gestor.crear_reserva(
            "R001", "1001", "S01", 2
        ),
        gestor
    )

    ejecutar_prueba(
        11,
        "Confirmacion de una reserva con impuesto y descuento",
        lambda: gestor.confirmar_reserva(
            "R001", impuesto=19, descuento=10
        ),
        gestor
    )

    ejecutar_prueba(
        12,
        "Procesamiento de una reserva confirmada",
        lambda: gestor.procesar_reserva("R001"),
        gestor
    )

    ejecutar_prueba(
        13,
        "Intento de crear reserva con cliente inexistente",
        lambda: gestor.crear_reserva(
            "R002", "9999", "S01", 2
        ),
        gestor
    )

    ejecutar_prueba(
        14,
        "Intento de crear reserva con duracion invalida",
        lambda: gestor.crear_reserva(
            "R003", "1001", "S01", -3
        ),
        gestor
    )

    ejecutar_prueba(
        15,
        "Intento de reservar un servicio no disponible",
        lambda: (
            gestor.crear_reserva(
                "R004", "1002", "E02", 2
            )
        ),
        gestor
    )

    ejecutar_prueba(
        16,
        "Creacion de una segunda reserva",
        lambda: gestor.crear_reserva(
            "R005", "1002", "A01", 1
        ),
        gestor
    )

    ejecutar_prueba(
        17,
        "Cancelacion de una reserva pendiente",
        lambda: gestor.cancelar_reserva("R005"),
        gestor
    )

    ejecutar_prueba(
        18,
        "Intento de procesar una reserva cancelada",
        lambda: gestor.procesar_reserva("R005"),
        gestor
    )

    # ------------------------------------------------
    # RESUMEN DEL SISTEMA
    # ------------------------------------------------

    print("\n")
    print("*" * 65)
    print("             RESUMEN DEL SISTEMA SOFTWARE FJ")
    print("*" * 65)

    print("\nCLIENTES REGISTRADOS:")

    for cliente in gestor.listar_clientes():
        print(cliente.mostrar_informacion())
        print("-" * 40)

    print("\nSERVICIOS REGISTRADOS:")

    for servicio in gestor.listar_servicios():
        print(servicio.describir_servicio())
        print("-" * 40)

    print("\nRESERVAS REGISTRADAS:")

    for reserva in gestor.listar_reservas():
        print(reserva.mostrar_informacion())
        print("-" * 40)

    print("\n")
    print("*" * 65)
    print("EJECUCION DEL SISTEMA FINALIZADA")
    print("Los eventos y errores fueron registrados en logs/sistema.log")
    print("*" * 65)

    gestor.logger.info("Ejecucion principal finalizada.")


if __name__ == "__main__":
    ejecutar_sistema()
