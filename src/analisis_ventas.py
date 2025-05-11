'''
Análisis general
¿Cuál es el total de ventas generado en todo el periodo? = total_ventas

¿Cuántas ventas totales se registraron por producto? = ventas_totales_productos["Total_Venta"]
 
¿Qué día se registró la mayor venta (en euros)? = mayor_venta

Por producto
¿Cuál fue el producto más vendido en cantidad total? = producto["Cantidad"]

¿Cuál fue el producto que generó más ingresos? = producto_mayor_ingreso

¿Cuál fue el precio promedio por producto? = producto["Precio_Unitario"]

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
# Fecha   Producto  Precio_Unitario  Cantidad   Sucursal  Total_Venta

total_ventas = df["Total_Venta"].sum()

ventas_totales_productos = df.groupby("Producto").agg({
    "Total_Venta":['sum','max'],
    "Precio_Unitario":"mean",
    "Cantidad":"max"
})

id_max_venta = df["Total_Venta"].idxmax()
mayor_venta = df.loc[id_max_venta]
# fecha_mayor_venta = mayor_venta["Fecha"]

productos = df.groupby("Producto").agg({
    "Precio_Unitario":"mean",
    "Cantidad":"sum",
    "Total_Venta":"sum"
    
})
mayor_ingreso = productos["Total_Venta"].idxmax()
producto_mayor_ingreso = productos.loc[mayor_ingreso]
print(productos)
print(productos.loc[mayor_ingreso])