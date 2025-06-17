import pandas as pd
import numpy as np
from openpyxl import load_workbook

# Ruta del archivo
ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

# Leer la hoja productos
productos = pd.read_excel(ruta_excel, sheet_name='productos')

# Definimos rangos de costo según categoría (en proporción al precio_unitario)
rangos_costo = {
    'Artículos de Perfumería': (0.35, 0.50),
    'Belleza': (0.30, 0.45),
    'Cuidado Personal': (0.35, 0.50),
    'Especialidad Medicinal': (0.25, 0.35),
    'Farmacia': (0.30, 0.50),
    'Insumos Hospitalarios': (0.20, 0.30),
    'Productos Médicos': (0.25, 0.40)
}

# Función para asignar costo
def asignar_costo(row):
    rango = rangos_costo.get(row['categoria'], (0.3, 0.5))  # default si categoría no encontrada
    factor = np.random.uniform(rango[0], rango[1])
    return row['precio_unitario'] * factor

# Generar columna costo
productos['costo'] = productos.apply(asignar_costo, axis=1).round(2)

# Guardar cambios en el mismo archivo Excel, hoja productos (sobrescribir)
with pd.ExcelWriter(ruta_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    productos.to_excel(writer, sheet_name='productos', index=False)

# Imprimir mensaje de éxito
print("Columna 'costo' agregada exitosamente a la hoja 'productos'.")