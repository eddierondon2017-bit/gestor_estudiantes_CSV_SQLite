import csv
    def generar_csv(nombre_archivo: str = "estudiantes.csv") -> None:
    """Genera un archivo CSV con datos iniciales."""
    datos = [
            
        ["nombre", "correo", "nota"],
        ["Ana", "ana@mail.com", 4.5],
        ["Luis", "luis@mail.com", 3.8],
        ["Sara", "sara@mail.com", 4.2],
    ]
    with open(
        nombre_archivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)
    print(f"[OK] Archivo {nombre_archivo} generado.")