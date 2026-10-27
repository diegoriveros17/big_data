import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import duckdb

    DATABASE_URL = "ventas.csv"
    engine = duckdb.connect('analisis.duckdb', read_only=False)
    return (engine,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM READ_CSV_AUTO('ventas.csv')
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        CREATE TABLE IF NOT EXISTS ventas as SELECT * FROM READ_CSV_AUTO('ventas.csv')
        """,
        engine=engine
    )
    return


@app.cell
def _():
    # con.sql("""
    # select distinct(region) from read_csv_auto('ventas.csv')""")
    return


@app.cell
def _():
    # con.sql("""
    #         select sum(unit_price) as total  from read_csv_auto('ventas.csv')  """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM ventas
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT DISTINCT region FROM ventas;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT DISTINCT channel	FROM ventas
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
