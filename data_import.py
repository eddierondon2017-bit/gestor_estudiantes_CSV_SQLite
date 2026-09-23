import csv
import sqlite3
    def importar_datos(
    csv_file: str,
    nombre_bd: str = "estudiantes.db"
) -> None:
    """Importa registros desde CSV hacia SQLite."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    with open(
    csv_file,
    newline="",
    encoding="utf-8"
    ) as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
        try:
            cur.execute(
                """
                INSERT INTO estudiantes
                (nombre, correo, nota)
                VALUES (?, ?, ?)
                """,
                (
                fila["nombre"],
                fila["correo"],
                float(fila["nota"]),
                )
            )
        except sqlite3.IntegrityError:
            print(
                "[ADVERTENCIA] Registro duplicado:",
                fila["correo"]
          )
    conn.commit()
    conn.close()
    print("[OK] Importacion finalizada.")