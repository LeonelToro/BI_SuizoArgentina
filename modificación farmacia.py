import pandas as pd
import random
from faker import Faker

faker = Faker('es_AR')

# Cargar Excel original
ruta_excel = r'C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx'
df_farmacias = pd.read_excel(ruta_excel, sheet_name='farmacias')

# Prefijos y sufijos
prefijos = [
    "Farmacia", "Droguería", "Centro de Salud", "Salud Total",
    "Pharma", "Tu Salud", "Farmared", "Vida Sana", "Bienestar",
    "Farmacia Saludable", "Red Farma"
]
sufijos = ["del pueblo", "central", "del barrio", "24 hs", "norte", "de la victoria"]

nombres_generados = []

for _ in range(len(df_farmacias)):
    tipo = random.choices(
        ["normal", "apellido", "localidad"],
        weights=[75, 15, 10]
    )[0]

    if tipo == "apellido":
        apellido = faker.last_name()
        nombre = f"Farmacia {apellido}"

    elif tipo == "localidad":
        localidad = faker.city()
        nombre = f"Farmacia {localidad}"

    else:
        prefijo = random.choice(prefijos)
        sufijo = random.choice(sufijos)
        nombre = f"{prefijo} {sufijo}"

    nombres_generados.append(nombre)

# Reemplazar la columna existente
df_farmacias["nombre_farmacia"] = nombres_generados

# Guardar en el mismo archivo Excel, reemplazando solo esa hoja
with pd.ExcelWriter(ruta_excel, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    df_farmacias.to_excel(writer, sheet_name="farmacias", index=False)

print("✅ Nombres de farmacias actualizados exitosamente.")
