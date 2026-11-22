
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas para una empresa dedicada al alquiler de salas, equipos tecnológicos y asesorías especializadas.

El sistema utiliza programación orientada a objetos, almacenamiento mediante listas internas y archivos de registro para controlar eventos y errores, sin utilizar bases de datos.

### 2. Objetivo

Desarrollar una aplicación modular, estable y extensible que implemente los principios de abstracción, herencia, polimorfismo, encapsulamiento y manejo avanzado de excepciones.

### 3. Tecnologías utilizadas

- Python 3.14.3
- Visual Studio Code
- Git
- GitHub
- Programación orientada a objetos
- Módulo logging de Python

### 4. Funcionalidades

- Registro y validación de clientes.
- Administración de servicios.
- Reservas de salas.
- Alquiler de equipos tecnológicos.
- Asesorías especializadas.
- Confirmación y cancelación de reservas.
- Cálculo de costos con impuestos y descuentos.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores mediante logs.
- Simulación de operaciones válidas e inválidas.

### 5. Estructura del proyecto

Software_FJ/
- main.py
- entidades.py
- excepciones.py
- clientes.py
- servicios.py
- reservas.py
- gestor.py
- README.md
- logs/
  - sistema.log

### 6. Ejecución del programa

Para ejecutar el sistema, abre la terminal en la carpeta principal del proyecto y utiliza:

python main.py

El programa ejecutará las simulaciones y mostrará los resultados en la terminal.

### 7. Manejo de errores

El sistema incorpora excepciones personalizadas, bloques try/except, else, finally y encadenamiento de excepciones.

Los eventos y errores se registran automáticamente en:

logs/sistema.log

### 8. Almacenamiento

La información se administra mediante objetos y listas internas de Python. No se utiliza ningún motor de base de datos.

### 9. Autora

**Yenifer Eliana Quintero Bermúdez**

Desarrollo individual del proyecto académico Software FJ.
