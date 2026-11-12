CREATE OR REPLACE TABLE ventas_transformadas AS
SELECT date as fecha,
region AS region,
product AS nombre_producto,
channel AS canal_venta,
units AS cantidad,
unit_price AS precio_unitario,
units * unit_price AS total_calculado,
revenue AS total_dolares
FROM ventas_validas;