CREATE OR REPLACE TABLE ventas_rechazadas AS
SELECT * FROM ventas_raw WHERE 
TRY_CAST(date AS DATE) IS NULL
OR region IS NULL
OR TRIM(region) = ''
OR channel IS NULL
OR TRIM(channel)= ''
OR product IS NULL
OR TRIM(product)=''
OR units IS NULL
OR units <= 0
OR unit_price IS NULL
OR unit_price <= 0
OR revenue IS NULL
OR revenue <=0;

CREATE OR REPLACE TABLE ventas_validas AS
SELECT * FROM ventas_raw WHERE 
TRY_CAST(date AS DATE) IS NOT NULL
AND region IS NOT NULL
AND TRIM(region) <> ''
AND channel IS NOT NULL
AND TRIM(channel)<> ''
AND product IS NOT NULL
AND TRIM(product)<>''
AND units IS NOT NULL
AND units > 0
AND unit_price IS NOT NULL
AND unit_price > 0
AND revenue IS NOT NULL
AND revenue > 0;