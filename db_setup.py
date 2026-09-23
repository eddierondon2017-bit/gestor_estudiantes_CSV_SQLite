import sqlite3
def crear_base(nombre_bd: str = "estudiantes.db") -> None:
    """Crea la base de datos y la tabla estudiantes."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    nota REAL
    )
    """)
    conn.commit()
    conn.close()
    print(f"[OK] Base de datos {nombre_bd} preparada.")