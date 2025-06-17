import pandas as pd
import numpy as np

# Ruta del archivo original
ruta_archivo = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

# Leer el Excel y la hoja productos
df_productos = pd.read_excel(ruta_archivo, sheet_name='productos')

# Cantidad total de productos
n = len(df_productos)

# Proporciones y rangos de precios
proporciones = [0.06, 0.80, 0.10, 0.04]
rangos = [
    (11000, 20000),
    (20000, 50000),
    (50000, 120000),
    (120000, 200000)
]

# Crear array con índices aleatorios para cada rango según proporción
indices = np.arange(n)
np.random.shuffle(indices)

# Calcular cantidades por rango
cantidades = [int(p * n) for p in proporciones]

# Ajustar última cantidad para que la suma sea igual a n
cantidades[-1] = n - sum(cantidades[:-1])

# Generar precios para cada segmento
precios = np.empty(n)

inicio = 0
for i, (cantidad, (min_p, max_p)) in enumerate(zip(cantidades, rangos)):
    fin = inicio + cantidad
    precios_segmento = np.random.uniform(min_p, max_p, cantidad)
    precios[inicio:fin] = precios_segmento
    inicio = fin

# Asignar precios redondeados a la columna precio_unitario
df_productos['precio_unitario'] = np.round(precios, 2)

# Sobrescribir solo la hoja productos manteniendo el resto del archivo
with pd.ExcelWriter(ruta_archivo, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_productos.to_excel(writer, sheet_name='productos', index=False)

print("Columna 'precio_unitario' actualizada con precios realistas y archivo guardado correctamente.")
