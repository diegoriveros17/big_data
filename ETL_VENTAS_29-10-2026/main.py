import duckdb
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
SQL_DIR = BASE_DIR / "sql"

# Asegura que la carpeta de salida exista antes de guardar
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print(BASE_DIR)

def read_sql(filename: str): 
    path = SQL_DIR / filename
    return path.read_text(encoding="utf-8")

def count(con, table):
    # Retorna el valor numérico del conteo
    return con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]

def main():
    try:
        con = duckdb.connect("analisis.duckdb")

        print("#### PROCESO DE EXTRACCION ###")

        con.execute(
            read_sql(filename="extract.sql"), [str(DATA_DIR / "ventas.csv")]
        )

        print("Valores extraidos:", count(con, "ventas_raw"))

        print("### Validacion ###")

        con.execute(read_sql(filename="validations.sql"))
        
        print("Valores rechazados:", count(con, "ventas_rechazadas"))
        print("Valores validas:", count(con, "ventas_validas"))

        print("### Transformaciones ###")
        con.execute(read_sql(filename="transforms.sql"))

        print("Valores transformadas:", count(con, "ventas_transformadas"))

        df = con.execute(read_sql(filename="export.sql")).df()
        df.to_parquet(str(OUTPUT_DIR / "ventas.parquet"))

        print("### Datos exportados correctamente ###")
    except Exception as e:
        print("Error al procesar los datos", e)


if __name__ == "__main__":
    main()