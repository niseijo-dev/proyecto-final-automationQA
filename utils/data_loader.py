import csv
import json
import os

def load_csv_data(filename):
    """Lee un archivo CSV de la carpeta datos/ y devuelve una lista de diccionarios"""
    data = []
    # Construye la ruta absoluta para evitar errores de 'file not found'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_path, "datos", filename)
    
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {filename} en {path}")
        return []

def load_json_data(filename):
    """Lee un archivo JSON de la carpeta datos/"""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_path, "datos", filename)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {filename} en {path}")
        return []