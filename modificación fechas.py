import pandas as pd

ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

# Leer la hoja ventas
ventas = pd.read_excel(ruta_excel, sheet_name='ventas', engine='openpyxl')

# Verificamos que exista la columna fecha
if 'fecha' not in ventas.columns:
    raise ValueError("La columna 'fecha' no existe en la hoja ventas")

# Ordenar las fechas ascendentemente
fechas_ordenadas = ventas['fecha'].sort_values().reset_index(drop=True)

# Ordenar ventas por id_venta para asignar las fechas ordenadas en ese orden
ventas = ventas.sort_values('id_venta').reset_index(drop=True)

# Reemplazar la columna fecha con la lista ordenada
ventas['fecha'] = fechas_ordenadas

# Guardar la hoja ventas con las fechas reordenadas reemplazando la hoja existente
with pd.ExcelWriter(ruta_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    ventas.to_excel(writer, sheet_name='ventas', index=False)

print("Fechas en hoja 'ventas' reordenadas y asignadas correctamente.")
