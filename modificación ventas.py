import pandas as pd
import numpy as np

ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

# Leer hojas
ventas = pd.read_excel(ruta_excel, sheet_name='ventas', engine='openpyxl')
detalle_ventas = pd.read_excel(ruta_excel, sheet_name='detalle_ventas', engine='openpyxl')

# Rango fechas
fecha_inicio = pd.to_datetime("2024-05-01")
fecha_fin = pd.to_datetime("2025-04-30")

# Fechas aleatorias para cada venta
np.random.seed(42)
num_filas = len(ventas)
fechas_random = pd.to_datetime(np.random.randint(fecha_inicio.value // 10**9,
                                                fecha_fin.value // 10**9,
                                                num_filas), unit='s')
ventas['fecha'] = fechas_random

# Calcular monto_total sumando subtotal de detalle_ventas agrupado por id_venta
totales = detalle_ventas.groupby('id_venta')['subtotal'].sum().reset_index()
totales.rename(columns={'subtotal': 'monto_total'}, inplace=True)

# Merge para actualizar ventas con montos correctos
ventas_actualizadas = ventas.merge(totales, on='id_venta', how='left')

# Actualizamos monto_total con el valor recién calculado
ventas_actualizadas['monto_total'] = ventas_actualizadas['monto_total_y'].combine_first(ventas_actualizadas['monto_total_x'])

# Borrar columnas intermedias y precio_unitario
ventas_actualizadas.drop(columns=['monto_total_x', 'monto_total_y'], inplace=True, errors='ignore')
if 'precio_unitario' in ventas_actualizadas.columns:
    ventas_actualizadas.drop(columns=['precio_unitario'], inplace=True)

# Guardar la tabla actualizada, reemplazando la hoja ventas
with pd.ExcelWriter(ruta_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    ventas_actualizadas.to_excel(writer, sheet_name='ventas', index=False)

print("Ventas actualizadas con fechas entre 01/05/2024 y 30/04/2025, monto_total recalculado y precio_unitario eliminado.")
