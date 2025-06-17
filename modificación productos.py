import pandas as pd
from faker import Faker
import random

ruta_excel = r'C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Suizo\proyecto_suizo_dataset.xlsx'

# Cargo archivo Excel
xls = pd.ExcelFile(ruta_excel)
df_productos = pd.read_excel(xls, sheet_name='productos')

# Definimos listas con nombres reales por categoría
nombres_por_categoria = {
    'Artículos de Perfumería': [
        'Perfume Aqua Fresh', 'Esmalte de Uñas Satinado', 'Loción Corporal Rosas', 'Desodorante Invisible',
        'Spray Fixador', 'Crema Manos Suave', 'Gel de Ducha Floral', 'Bronceador Natural SPF15',
        'Aceite Corporal Relajante', 'Crema Facial Antiarrugas', 'Loción Aftershave', 'Sérum Antioxidante',
        'Desodorante Roll-on', 'Polvo Compacto Mate'
    ],
    'Belleza': [
        'Serum Vitamina C', 'Base Líquida Natural', 'Máscara de Pestañas Volumen', 'Exfoliante Facial Suave',
        'Corrector Tono Medio', 'Bronceador Solar SPF30', 'Rubor en Polvo', 'Iluminador Facial',
        'Bálsamo Labial Hidratante', 'Tónico Facial Refrescante', 'Crema Contorno de Ojos', 'Esmalte de Labios',
        'Gel Fijador de Cejas', 'Mascarilla Capilar Reparadora'
    ],
    'Cuidado Personal': [
        'Jabón Líquido Antibacterial', 'Pasta Dental Blanqueadora', 'Cepillo de Dientes', 'Shampoo Hidratante',
        'Acondicionador Reparador', 'Protector Labial SPF15', 'Enjuague Bucal', 'Desodorante en Spray',
        'Hilo Dental', 'Toallitas Húmedas', 'Crema de Manos Nutritiva', 'Espuma de Afeitar',
        'Loción Corporal Hidratante', 'Gel Antiséptico'
    ],
    'Especialidad Medicinal': [
        'Ibuprofeno 400mg', 'Paracetamol 500mg', 'Amoxicilina 500mg', 'Metformina 850mg',
        'Omeprazol 20mg', 'Loratadina 10mg', 'Diclofenac 50mg', 'Salbutamol Inhalador',
        'Clonazepam 0.5mg', 'Fluoxetina 20mg', 'Lorazepam 1mg', 'Prednisona 5mg',
        'Ranitidina 150mg', 'Aspirina 100mg'
    ],
    'Farmacia': [
        'Tiritas Antisépticas', 'Alcohol en Gel 70%', 'Termómetro Digital', 'Guantes de Látex',
        'Gasas Estériles', 'Vendas Elásticas', 'Esparadrapo Médico', 'Jeringa Descartable 10ml',
        'Mascarilla Quirúrgica', 'Compresas Frías', 'Sonda Nasogástrica', 'Bata Quirúrgica',
        'Catéter Urinario', 'Sueros Endovenosos'
    ],
    'Insumos Hospitalarios': [
        'Catéter Intravenoso', 'Sutura Absorbible', 'Mascarilla Quirúrgica', 'Bata Desechable',
        'Jeringa 5ml', 'Monitor de Signos Vitales', 'Guantes Estériles', 'Cánula Nasal',
        'Bolsas para Sangre', 'Pinzas Quirúrgicas', 'Tubos Endotraqueales', 'Sistemas de Infusión',
        'Torundas Estériles', 'Cubre Zapatos Desechables'
    ],
    'Productos Médicos': [
        'Nebulizador Portátil', 'Tensiómetro Digital', 'Oxímetro de Pulso', 'Silla de Ruedas Plegable',
        'Andador Ajustable', 'Termómetro Infrarrojo', 'Cama Hospitalaria Eléctrica', 'Monitor ECG',
        'Bomba de Infusión', 'Ventilador Mecánico', 'Lámpara Quirúrgica', 'Electrocardiógrafo',
        'Mesa de Examen', 'Cojín Ortopédico'
    ]
}


# Función para asignar nombre basado en la categoría
def asignar_nombre_producto(categoria):
    if categoria in nombres_por_categoria:
        return random.choice(nombres_por_categoria[categoria])
    else:
        return 'Producto Genérico'

# Aplico la función para reemplazar la columna 'nombre_producto'
df_productos['nombre_producto'] = df_productos['categoria'].apply(asignar_nombre_producto)

# Guardar Excel manteniendo las demás hojas intactas
hojas = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
hojas['productos'] = df_productos

with pd.ExcelWriter(ruta_excel, engine='xlsxwriter') as writer:
    for sheet_name, df in hojas.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
# Mensaje de éxito
print("Los nombres de los productos han sido actualizados exitosamente en el archivo Excel.")