'''
Análisis general
¿Cuál es el total de ventas generado en todo el periodo?

¿Cuántas ventas totales se registraron por producto?

¿Qué día se registró la mayor venta (en euros)?

Por producto
¿Cuál fue el producto más vendido en cantidad total?

¿Cuál fue el producto que generó más ingresos?

¿Cuál fue el precio promedio por producto?

Por sucursal
¿Qué sucursal vendió más (en cantidad y en euros)?

¿Cuál fue el ingreso promedio diario por sucursal?

¿Cómo varían las ventas entre las sucursales? (puedes graficar esto si quieres)

Por fecha
¿Cuál fue el promedio diario de ventas?

¿Qué tendencia se observa si agrupas las ventas por semana?

¿Qué producto se vendió más en la primera semana de enero?

'''

import pandas as pd

df = pd.read_csv("C:/Users/User/Documents/python/ejercicios_chatgpt/mini-proyecto-sem-3/data/dataset_ventas.csv")

print(df.head())
print(df.info())