import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tablas: customers, orders, order_details, products y employees
    1. customers: guarda las empresas que compran algunos de los datos que incluye son nombre de la empresa, contacto, cargo, dirección, ciudad, país, telefono, etc.
    Clave primaria: customer_id
    Claves foráneas:
    2. orders: guarda los pedido, algunos de los datos que incluye son fecha del pedido, la fecha requerida, la fecha de envío, el costo de flete (freight) y los datos del destino (ship_city, ship_country, etc.).
    Clave primaria: order_id.
    Claves foráneas: customer_id y employee_id .
    3. order_details: guarda los productos que tiene cada pedido, con el precio unitario, la cantidad y el descuento.
    Clave primaria: formada por order_id, product_id.
    Claves foráneas: order_id y product_id.
    4. products: guarda los productos algunos de los datos que incluye son nombre, precio, stock, unidades pedidas, nivel de reposición y si está discontinuado, etc.
    Clave primaria: product_id.
    Claves foráneas:category_id y supplier_id.
    5. employees: guarda: los empleados de la empresa, algunos de los datos que incluye son nombre, cargo, fecha de nacimiento, fecha de contratación, dirección, notas, etc.
    Clave primaria: employee_id.
    Clave foránea:
    """)
    return


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
        SELECT product_name, unit_price FROM products WHERE unit_price > 20 ORDER BY unit_price DESC
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT company_name, city, country FROM customers ORDER BY company_name ASC
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
        SELECT od.order_id, p.product_name, od.quantity, od.unit_price FROM  products p JOIN  order_details od ON p.product_id = od.product_id;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT  o.*, e.first_name, e.last_name FROM orders as o JOIN employees as e ON e.employee_id = o.employee_id
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT COUNT(*) FROM customers
        """,
        engine=engine
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Representa la cantidad de clientes distintos (empresas) registrados.
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT COUNT(*) FROM products
        """,
        engine=engine
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Representa la cantidad de productos distintos que ofrece la empresa.
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT COUNT(*) FROM orders
        """,
        engine=engine
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Representa la cantidad de pedidos realizados en total.
    """)
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM products
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        INSERT INTO products (product_id, product_name, unit_price, discontinued) VALUES (78, 'Yerba', 25.50, 0);
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM products WHERE product_name LIKE '%Yerba%'
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        BEGIN;
        UPDATE products SET unit_price = 30.0 WHERE product_id = 78;
        SELECT product_id, product_name, unit_price FROM products WHERE product_id = 78;
        ROLLBACK;
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT product_id, product_name, unit_price FROM products WHERE product_id = 78;
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
