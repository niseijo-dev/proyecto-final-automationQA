import logging
import os

def get_logger():
    # Crea la carpeta logs si no existe
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    # Configura el logger
    logging.basicConfig(
        filename=os.path.join(log_dir, "test_execution.log"),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True # Fuerza la re-configuración si ya existe
    )
    return logging.getLogger("TalentoLab")