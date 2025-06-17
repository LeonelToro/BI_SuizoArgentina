import pandas as pd
import numpy as np
import random
from faker import Faker
import os

fake = Faker('es_AR')
random.seed(42)
np.random.seed(42)

# Parámetros
n_productos = 500
n_clientes = 1000
n_farmacias = 300
n_usuarios_farma = 500
n_ventas = 5000
n_cobranzas = 4000

# Categorías de productos
categorias = {
    'Especialidad Medicinal': 'Salud',
    'Productos Médicos': 'Salud',
    'Artículos de Perfumería': 'Cuidado Personal',
    'Insumos Hospitalarios': 'Salud',
    'Belleza': 'Cuidado Personal',
    'Cuidado Personal': 'Cuidado Personal',
    'Farmacia': 'Salud'
}
canales_venta = ['Farmaonline', 'Venta Directa', 'Televentas', 'Visita Comercial']

# Tabla productos
productos = pd.DataFrame({
    'id_producto': range(1, n_productos + 1),
    'nombre_producto': [fake.word() + " " + fake.color_name() for _ in range(n_productos)],
    'categoria': np.random.choice(list(categorias.keys()), size=n_productos),
    'precio_unitario': np.random.uniform(500, 15000, size=n_productos).round(2)
})

# Tabla clientes
clientes = pd.DataFrame({
    'id_cliente': range(1, n_clientes + 1),
    'nombre_cliente': [fake.company() for _ in range(n_clientes)],
    'provincia': [fake.province() for _ in range(n_clientes)],
    'tipo_cliente': np.random.choice(['Farmacia', 'Hospital', 'Clínica'], size=n_clientes)
})

# Tabla farmacias
farmacias = clientes[clientes['tipo_cliente'] == 'Farmacia'][['id_cliente', 'nombre_cliente', 'provincia']]
farmacias = farmacias.rename(columns={
    'id_cliente': 'id_farmacia',
    'nombre_cliente': 'nombre_farmacia'
})

# Tabla usuarios_farmaonline
usuarios_farma = pd.DataFrame({
    'id_usuario': range(1, n_usuarios_farma + 1),
    'nombre_usuario': [fake.name() for _ in range(n_usuarios_farma)],
    'email': [fake.email() for _ in range(n_usuarios_farma)],
    'provincia': [fake.province() for _ in range(n_usuarios_farma)]
})

# Tabla ventas
ventas = pd.DataFrame({
    'id_venta': range(1, n_ventas + 1),
    'id_producto': np.random.choice(productos['id_producto'], n_ventas),
    'cantidad': np.random.randint(1, 20, size=n_ventas),
    'fecha': pd.to_datetime(np.random.choice(pd.date_range(start='2023-01-01', end='2023-12-31'), size=n_ventas)),
    'canal_venta': np.random.choice(canales_venta, size=n_ventas, p=[0.3, 0.4, 0.2, 0.1])
})

# Vinculación cliente o usuario
ventas['id_cliente'] = np.where(
    ventas['canal_venta'] == 'Farmaonline',
    np.nan,
    np.random.choice(clientes['id_cliente'], size=n_ventas)
)

ventas['id_usuario'] = np.where(
    ventas['canal_venta'] == 'Farmaonline',
    np.random.choice(usuarios_farma['id_usuario'], size=n_ventas),
    np.nan
)

# Calculo del total
ventas = ventas.merge(productos[['id_producto', 'precio_unitario']], on='id_producto', how='left')
ventas['monto_total'] = (ventas['cantidad'] * ventas['precio_unitario']).round(2)

# Tabla cobranzas
cobranzas = ventas.sample(n=n_cobranzas).copy()
cobranzas = cobranzas[['id_venta', 'fecha', 'monto_total']].rename(columns={
    'fecha': 'fecha_cobranza',
    'monto_total': 'monto_cobrado'
})
cobranzas['fecha_cobranza'] += pd.to_timedelta(np.random.randint(1, 60, size=n_cobranzas), unit='d')
cobranzas['estado_cobranza'] = np.random.choice(['Pagado', 'Parcial', 'Pendiente'], size=n_cobranzas, p=[0.7, 0.2, 0.1])

# Guardar en Excel
output_path = r'C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx'

with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    productos.to_excel(writer, index=False, sheet_name='productos')
    clientes.to_excel(writer, index=False, sheet_name='clientes')
    farmacias.to_excel(writer, index=False, sheet_name='farmacias')
    usuarios_farma.to_excel(writer, index=False, sheet_name='usuarios_farmaonline')
    ventas.to_excel(writer, index=False, sheet_name='ventas')
    cobranzas.to_excel(writer, index=False, sheet_name='cobranzas')

print("✅ Dataset exportado a Excel en la ruta indicada.")
