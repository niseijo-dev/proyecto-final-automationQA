Proyecto Final - Framework de Automatización de Pruebas

# 1. Propósito del Proyecto
Este proyecto consiste en un framework de automatización de pruebas híbrido desarrollado en Python. Su objetivo es validar la calidad del software tanto en el Frontend (UI) como en el Backend (API) automáticamente.
El framework asegura que los flujos críticos de negocio (como el login, la gestión del carrito de compras y la administración de usuarios) funcionen correctamente, integrando prácticas de Page Object Model (POM), Data-Driven Testin y Reportes de ejecución.

# 2. Tecnologías Utilizadas
- Selenium WebDriver: Para la automatización de la interfaz web (UI).
- Requests: Para la automatización de servicios REST (API).
- Pytest: Framework de ejecución de pruebas.
- Pytest-HTML: Para generación de reportes visuales.
- Faker: Para generación de datos de prueba aleatorios.
- GitHub Actions: Integración Continua (CI/CD).

# 3. Estructura del Proyecto
El código está organizado siguiendo buenas prácticas de modularización:

* pages/: Implementación del patrón POM. Cada archivo representa una pantalla del sitio web.
* tests/: Contiene los scripts de prueba, separados por funcionalidad (UI y API).
* datos/: Archivos externos (CSV y JSON) para pruebas parametrizadas (Data-Driven).
* utils/: Funciones auxiliares (Loggers, cargadores de datos).
* reports/: Carpeta donde se generan los resultados de las pruebas y capturas de pantalla.
* logs/: Registro detallado de la ejecución paso a paso.

# 4. ¿Cómo instalar las dependencias?
1.  Abrir terminal en la carpeta del proyecto.
2.  Ejecutar el comando:
    ```bash
    pip install -r requirements.txt
    ```

## 5. ¿Cómo ejecutar las pruebas?
Existen dos formas de correr la suite de pruebas:

**Opción A: Script Automático (Recomendado)**
Ejecuta el script que configura y lanza todo automáticamente:
```bash
python run_tests.py

![CI Status](https://github.com/niseijo-dev/proyecto-final-automation-testing-Nicolas-Seijo/actions/workflows/ci.yml/badge.svg)