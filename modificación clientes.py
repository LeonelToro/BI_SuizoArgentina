import pandas as pd
import numpy as np
from faker import Faker

ruta_archivo = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

df_clientes = pd.read_excel(ruta_archivo, sheet_name='clientes')

fake = Faker('es_AR')

n = len(df_clientes)

# 6 provincias y proporciones aproximadas (ajustadas)
provincias = [
    'Buenos Aires',
    'Ciudad Autónoma de Buenos Aires',
    'Córdoba',
    'Santa Fe',
    'Mendoza',
    'Tucumán',
    'Entre Ríos'
]

proporciones = [
    0.32,  # Buenos Aires
    0.12,  # CABA
    0.10,  # Córdoba
    0.09,  # Santa Fe
    0.06,  # Mendoza
    0.06,  # Tucumán
    0.05   # Entre Ríos
]
# Ajustar para que sumen 1 (normalizar proporciones)
total_p = sum(proporciones)
proporciones = [p/total_p for p in proporciones]

# Cantidad de clientes por provincia
cantidades = [int(p * n) for p in proporciones]

# Ajuste por redondeo
diferencia = n - sum(cantidades)
cantidades[0] += diferencia  # sumamos la diferencia en Buenos Aires

# Crear lista provincias según cantidades
lista_provincias = []
for provincia, cant in zip(provincias, cantidades):
    lista_provincias.extend([provincia] * cant)

# Mezclar aleatoriamente
np.random.shuffle(lista_provincias)

# Generar nombres y apellidos
nombres = [fake.first_name() for _ in range(n)]
apellidos = [fake.last_name() for _ in range(n)]

df_clientes['nombre'] = nombres
df_clientes['apellido'] = apellidos
df_clientes['provincia'] = lista_provincias
df_clientes['nombre_completo'] = df_clientes['nombre'] + ' ' + df_clientes['apellido']

with pd.ExcelWriter(ruta_archivo, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_clientes.to_excel(writer, sheet_name='clientes', index=False)

print("Tabla 'clientes' actualizada con nombres reales y 6 provincias según población.")

