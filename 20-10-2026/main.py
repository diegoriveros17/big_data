import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import os
    import sqlalchemy

    _password = os.environ.get("postgres_password")
    DATABASE_URL = f"postgresql://postgres:{_password}@localhost:5432/northwind"
    engine = sqlalchemy.create_engine(DATABASE_URL)
    return (engine,)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM customers LIMIT 10;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM products LIMIT 10;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM orders LIMIT 10;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT product_name, unit_price FROM products WHERE unit_price > 20
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT company_name, city, country FROM customers WHERE country LIKE '%Germany%'
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT  o.order_id, o.order_date, c.company_name FROM customers as c JOIN orders as o ON c.customer_id = o.customer_id
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT od.order_id, p.product_name, od.quantity, od.unit_price FROM  products p INNER JOIN  order_details od ON p.product_id = od.product_id;
        -- SELECT od.order_id, p.product_name, od.quantity, od.unit_price FROM  products p, order_details od WHERE p.product_id = od.product_id;

        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
