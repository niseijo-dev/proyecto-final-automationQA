import pytest
import os
import sys

def main():
    # 1. Crear carpeta de reportes si no existe
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # 2. Definir argumentos de ejecución (igual que en la consola)
    # -v: Verbose (muestra más detalles)
    # --html: Genera el reporte visual
    # --self-contained-html: Guarda estilos dentro del HTML (para poder enviarlo)
    args = [
        "-v",
        "--html=reports/reporte_final.html",
        "--self-contained-html",
        "tests/"  # Carpeta donde busca los tests
    ]

    print("Iniciando ejecución de pruebas automatizadas...")
    
    # 3. Ejecutar Pytest
    retcode = pytest.main(args)
    
    # 4. Mostrar resultado final
    if retcode == 0:
        print("\nTodas las pruebas pasaron correctamente.")
    else:
        print("\n=Algunas pruebas fallaron. Revisar el reporte HTML.")
    
    sys.exit(retcode)

if __name__ == "__main__":
    main()