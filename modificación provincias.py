import pandas as pd
import numpy as np

# Ruta del archivo
ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx"

# Provincias y sus proporciones de población
provincias = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Ciudad Autónoma de Buenos Aires", "Mendoza",
    "Tucumán", "Entre Ríos", "Salta", "Misiones", "Chaco", "Corrientes", "Santiago del Estero",
    "San Juan", "Jujuy", "Río Negro", "Neuquén", "Formosa", "Chubut", "San Luis", "Catamarca",
    "La Rioja", "La Pampa", "Santa Cruz", "Tierra del Fuego"
]

pesos = np.array([
    0.38, 0.086, 0.076, 0.072, 0.045,
    0.035, 0.03, 0.029, 0.027, 0.025, 0.024, 0.022,
    0.019, 0.018, 0.017, 0.016, 0.014, 0.014, 0.013, 0.011,
    0.009, 0.008, 0.007, 0.005
])
pesos = pesos / pesos.sum() # Normalizar los pesos para que sumen 1
# Abrir todas las hojas necesarias
with pd.ExcelFile(ruta_excel) as xls:
    clientes = pd.read_excel(xls, sheet_name="clientes")
    farmacias = pd.read_excel(xls, sheet_name="farmacias")
    usuarios = pd.read_excel(xls, sheet_name="usuarios_farmaonline")

# Función para asignar provincias con pesos realistas
def asignar_provincias(n):
    return np.random.choice(provincias, size=n, p=pesos)

# Reemplazar columna 'provincia' en cada tabla
clientes['provincia'] = asignar_provincias(len(clientes))
farmacias['provincia'] = asignar_provincias(len(farmacias))
usuarios['provincia'] = asignar_provincias(len(usuarios))

# Guardar en el mismo archivo sin borrar las otras hojas
with pd.ExcelWriter(ruta_excel, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    clientes.to_excel(writer, sheet_name="clientes", index=False)
    farmacias.to_excel(writer, sheet_name="farmacias", index=False)
    usuarios.to_excel(writer, sheet_name="usuarios_farmaonline", index=False)
# Imprimir un mensaje de éxito
print("Provincias asignadas correctamente a las tablas clientes, farmacias y usuarios_farmaonline.")