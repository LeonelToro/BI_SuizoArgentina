import pandas as pd
from faker import Faker
import random

# Inicializar Faker en español (Argentina)
fake = Faker('es_AR')

# Ruta del archivo original
ruta_excel = r'C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx'

# Leer la hoja de usuarios
usuarios = pd.read_excel(ruta_excel, sheet_name='usuarios_farmaonline')

# Generar nuevos nombres
def generar_nombre_usuario():
    nombre = fake.first_name()
    apellido = fake.last_name()
    return f"{nombre} {apellido}"

usuarios['nombre_usuario'] = [generar_nombre_usuario() for _ in range(len(usuarios))]

# Generar mails
def generar_email(nombre_completo):
    nombre_completo = nombre_completo.lower().strip()
    nombre_completo = nombre_completo.replace(' ', '.')
    dominio = '@gmail.com'
    return nombre_completo + dominio

usuarios['email'] = usuarios['nombre_usuario'].apply(generar_email)
# Sobrescribir en el archivo
with pd.ExcelWriter(ruta_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    usuarios.to_excel(writer, sheet_name='usuarios_farmaonline', index=False)

print("✔️ Se actualizaron los nombres de usuario en la hoja 'usuarios_farmaonline' correctamente.")
