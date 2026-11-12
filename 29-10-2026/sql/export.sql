SELECT nombre_producto, SUM(cantidad) AS total_vendido,
SUM(total_calculado) AS ingreso_calculado,
SUM(total_dolares),
FROM ventas_transformadas
GROUP BY  nombre_producto
ORDER BY ingreso_calculado DESC;