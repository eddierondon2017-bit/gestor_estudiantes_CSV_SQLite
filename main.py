from pathlib import Path
from csv_generator import generar_csv
from db_setup import crear_base
from data_import import importar_datos
from queries import consultar_estudiantes
CSV_FILE = "estudiantes.csv"
DB_FILE = "estudiantes.db"
if __name__ == "__main__":
    if not Path(CSV_FILE).exists():
    generar_csv(CSV_FILE)
    crear_base(DB_FILE)
    importar_datos(CSV_FILE, DB_FILE)
    consultar_estudiantes(
    umbral=4.0,
    nombre_bd=DB_FILE
    )