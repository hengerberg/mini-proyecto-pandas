import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/User/Documents/python/ejercicios_chatgpt/mini-proyecto-sem-3/data/dataset_ventas.csv")
# Fecha   Producto  Precio_Unitario  Cantidad   Sucursal  Total_Venta

df["Fecha"] = pd.to_datetime(df["Fecha"])

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

# analisis por sucrusal

#¿Qué sucursal vendió más (en cantidad y en euros)?

#¿Cuál fue el ingreso promedio diario por sucursal?

#¿Cómo varían las ventas entre las sucursales? (puedes graficar esto si quieres)

sucursales = df.groupby("Sucursal").agg({
    "Cantidad":"sum",
    "Total_Venta":"sum"
})
id_sucursal_mayor_ventas = sucursales["Total_Venta"].idxmax()
sucursal_mayor_ventas = sucursales.loc[id_sucursal_mayor_ventas]

ingresos_sucursales = df.groupby(["Fecha","Sucursal"])["Total_Venta"].mean()

df_ordenado_fecha = df.sort_values(by="Fecha")



#¿Cuál fue el promedio diario de ventas?

#¿Qué tendencia se observa si agrupas las ventas por semana?

#¿Qué producto se vendió más en la primera semana de enero?

promedio_diario_ventas = df.groupby("Fecha")["Total_Venta"].mean()

df_ventas_semanal = df.resample("W", on="Fecha")["Total_Venta"].sum()

df_semana1 = df.loc[0:6]
productos_vendido_semana1 = df_semana1.groupby("Producto")["Cantidad"].max()
producto_mas_vendido_semana1 = productos_vendido_semana1.idxmax()

print("---------------------------------------")
print("            Análisis general           ")
print("---------------------------------------")

print("¿Cuál es el total de ventas generado en todo el periodo?")
print("El total de ventas generado en todo el periodo es de: ", total_ventas)

print("\n¿Cuántas ventas totales se registraron por producto?")
print(ventas_totales_productos["Total_Venta"])

print("\n¿Qué día se registró la mayor venta (en euros)?")
print(f'La mayor venta se realizo el dia {mayor_venta["Fecha"]} con un total de ${mayor_venta["Total_Venta"]}')

print("---------------------------------------")
print("        Análisis por Productos         ")
print("---------------------------------------")

print("¿Cuál fue el producto más vendido en cantidad total?")
print(productos["Cantidad"])

print("\n¿Cuál fue el producto que generó más ingresos?")
print(producto_mayor_ingreso)

print("\n¿Cuál fue el precio promedio por producto?")
print(productos["Precio_Unitario"])

print("---------------------------------------")
print("        Análisis por Sucursal          ")
print("---------------------------------------")

print("¿Qué sucursal vendió más (en cantidad y en euros)?")
print(f'Sucursal: {id_sucursal_mayor_ventas}\nCantidad: {sucursal_mayor_ventas["Cantidad"]}\nEuros: {sucursal_mayor_ventas["Total_Venta"]}')

print("\n¿Cuál fue el ingreso promedio diario por sucursal?")
print(ingresos_sucursales)

print("\n¿Cómo varían las ventas entre las sucursales?")
df_ordenado_fecha.plot(x="Fecha",y="Total_Venta")
plt.figure(figsize=(8, 4))
plt.title("Ventas por Sucursal")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.show()

print("---------------------------------------")
print("         Análisis por Fecha            ")
print("---------------------------------------")

print("\n¿Cuál fue el promedio diario de ventas?")
print(promedio_diario_ventas)

print("\n¿Qué tendencia se observa si agrupas las ventas por semana?")
df_ventas_semanal.plot(x="Fecha",y="Total_Venta")
plt.figure(figsize=(8, 4))
plt.title("Tendencia de ventas Semanal")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.show()

print("\n¿Qué producto se vendió más en la primera semana de enero?")
print(producto_mas_vendido_semana1)