import sqlite3
def consultar_estudiantes(
    umbral: float = 4.0,
    nombre_bd: str = "estudiantes.db"
) -> None:
    """Muestra estudiantes con nota igual o superior al umbral."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT nombre, nota
        FROM estudiantes
        WHERE nota >= ?
        ORDER BY nota DESC
        """,
        (umbral,)
    )
    resultados = cur.fetchall()
    print(f"\nEstudiantes con nota >= {umbral}")
    print("--------------------------------")
    for nombre, nota in resultados:
        print(f"{nombre:10s} | {nota:.2f}")
    conn.close()