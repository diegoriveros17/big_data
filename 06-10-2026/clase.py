import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    return


@app.cell
def _():
    import os
    import sqlalchemy

    _password = os.environ.get("_password")
    DATABASE_URL = f"postgresql://postgres:{_password}@localhost:5432/clase_sql"
    engine = sqlalchemy.create_engine(DATABASE_URL)
    return (engine,)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        DROP TABLE IF EXISTS peliculas;

        CREATE TABLE peliculas (
            id                    INTEGER PRIMARY KEY,
            titulo                TEXT NOT NULL,
            anio                  INTEGER NOT NULL,
            genero                TEXT,
            duracion_min          INTEGER,
            rating                NUMERIC(3,1),
            recaudacion_millones  NUMERIC(8,1),
            pais                  TEXT
        );

        INSERT INTO peliculas
            (id, titulo, anio, genero, duracion_min, rating, recaudacion_millones, pais)
        VALUES
            (1,  'El Padrino',                     1972, 'Drama',           175, 9.2,  246.0, 'EEUU'),
            (2,  'Pulp Fiction',                   1994, 'Crimen',          154, 8.9,  214.0, 'EEUU'),
            (3,  'El secreto de sus ojos',         2009, 'Drama',           129, 8.2,   33.0, 'Argentina'),
            (4,  'Relatos salvajes',               2014, 'Comedia',         122, 8.1,   30.0, 'Argentina'),
            (5,  'Parasite',                       2019, 'Thriller',        132, 8.5,  263.0, 'Corea del Sur'),
            (6,  'El viaje de Chihiro',            2001, 'Animación',       125, 8.6,  395.0, 'Japón'),
            (7,  'Interstellar',                   2014, 'Ciencia ficción', 169, 8.7,  701.0, 'EEUU'),
            (8,  'Inception',                      2010, 'Ciencia ficción', 148, 8.8,  836.0, 'EEUU'),
            (9,  'Matrix',                         1999, 'Ciencia ficción', 136, 8.7,  467.0, 'EEUU'),
            (10, 'Toy Story',                      1995, 'Animación',        81, 8.3,  373.0, 'EEUU'),
            (11, 'Coco',                           2017, 'Animación',       105, 8.4,  807.0, 'EEUU'),
            (12, 'Nueve reinas',                   2000, 'Thriller',        114, 7.9,   NULL, 'Argentina'),
            (13, 'Amores perros',                  2000, 'Drama',           154, 8.0,   20.0, 'México'),
            (14, 'El laberinto del fauno',         2006, 'Fantasía',        118, 8.2,   83.0, 'España'),
            (15, 'Oldboy',                         2003, 'Thriller',        120, 8.3,   15.0, 'Corea del Sur'),
            (16, 'Your Name',                      2016, 'Animación',       106, 8.4,  358.0, 'Japón'),
            (17, 'Ciudad de Dios',                 2002, 'Crimen',          130, 8.6,   30.0, 'Brasil'),
            (18, 'La historia oficial',            1985, 'Drama',           112, 7.8,   NULL, 'Argentina'),
            (19, 'Mad Max: Furia en el camino',    2015, 'Acción',          120, 8.1,  380.0, 'Australia'),
            (20, 'Gladiador',                      2000, 'Acción',          155, 8.5,  460.0, 'EEUU'),
            (21, 'Un cuento chino',                2011, 'Comedia',          93, 7.3,   NULL, 'Argentina'),
            (22, 'Shrek',                          2001, 'Animación',        90, 7.9,  488.0, 'EEUU'),
            (23, 'Joker',                          2019, 'Drama',           122, 8.4, 1074.0, 'EEUU'),
            (24, 'Whiplash',                       2014, 'Drama',           106, 8.5,   49.0, 'EEUU'),
            (25, 'Seven',                          1995, 'Crimen',          127, 8.6,  327.0, 'EEUU'),
            (26, 'El hijo de la novia',            2001, 'Drama',           123, 7.9,   NULL, 'Argentina'),
            (27, 'Akira',                          1988, 'Animación',       124, 8.0,   NULL, 'Japón'),
            (28, 'Proyecto sin título',            2027, NULL,              NULL, NULL, NULL, 'Argentina'),
            (29, 'Blade Runner 2049',              2017, 'Ciencia ficción', 164, 8.0,  260.0, 'EEUU'),
            (30, 'Intensa-Mente',                  2015, 'Animación',        95, 8.1,  858.0, 'EEUU');
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT COUNT(*) FROM peliculas;
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
