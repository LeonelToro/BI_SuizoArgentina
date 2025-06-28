# 📊Business Intelligence - Reporte Ejecutivo Comercial Suizo Argentina S.A.

Este proyecto simula un **análisis ejecutivo mensual** para el área comercial de **Suizo Argentina S.A.**, empresa del sector salud que comercializa y distribuye productos médicos, perfumería, medicamentos e insumos hospitalarios en todo el país.  
El objetivo principal fue **diseñar un dashboard funcional en Power BI** que permita hacer seguimiento de KPIs clave como **facturación, margen y costos**, con segmentaciones y visualizaciones relevantes para la toma de decisiones estratégicas.

---

## ⚙️ Generación y procesamiento de datos

El conjunto de datos fue generado íntegramente en Python utilizando las librerías **faker**, **random**, **numpy** y **pandas**, simulando operaciones comerciales realistas con criterios **comerciales y demográficos** propios del rubro salud.

- Se generaron tablas de clientes, productos, ventas, detalle de ventas, farmacias y usuarios del canal digital (Farmaonline).
- Los datos fueron luego **limpiados, transformados y estructurados en tablas relacionadas** listas para ser modeladas en Power BI.
- Se aplicaron ajustes manuales y modificaciones para reforzar la **verosimilitud del dataset**, como precios, fechas, provincias y categorizaciones de productos.

---

## 🧠 Modelado y visualización en Power BI

- En Power BI se diseñó un **modelo de datos optimizado**, utilizando relaciones adecuadas y medidas DAX personalizadas.
- Se implementaron **funciones de inteligencia temporal** para el análisis mensual y cuatrimestral, y se diseñaron visualizaciones alineadas a criterios de **identidad visual de marca**.
- El dashboard incluye filtros interactivos por **cuatrimestre y tipo de cliente**, y visualizaciones que permiten detectar rápidamente tendencias y variaciones clave en el rendimiento comercial.

---

## 📌 Métricas y visualizaciones destacadas

- **KPI Cards:** Facturación total 💰 | Margen promedio 📈 | Costos 💸
- **Gráficos:**
  - Evolución temporal de facturación y margen 🕒 
  - Costo por categoría de producto 🧴  
  - Facturación por provincia 🗺️  
  - Facturación por canal de venta 🛒  
 

---

## 🧾 Archivos incluidos

| Archivo                                                                                          | Descripción                                                                                     |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [generación costo.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/generación%20costo.py) | Script para simular los costos unitarios de los productos utilizando lógica de márgenes         |
| [generación detalle_venta.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/generación%20detalle_venta.py) | Generación del detalle de ventas con cantidades, precios y referencias cruzadas                 |
| [Generación Tablas - Suizo Argentina.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Generación%20Tablas%20-%20Suizo%20Argentina.py) | Script principal para generar las tablas base del proyecto con datos simulados                  |
| [modificación clientes.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20clientes.py) | Ajuste de clientes según criterios demográficos y segmentación comercial                        |
| [modificación farmacia.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20farmacia.py) | Limpieza y estandarización de datos de farmacias                                                |
| [modificación fechas.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20fechas.py) | Conversión y corrección de formatos de fecha para coherencia temporal                           |
| [modificación precio.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20precio.py) | Ajuste de precios simulados considerando lógicas de margen y estacionalidad                     |
| [modificación productos.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20productos.py) | Revisión y mejora de atributos de producto (categorías, unidades, etc.)                         |
| [modificación provincias.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20provincias.py) | Enriquecimiento de provincias con datos geográficos y comerciales                               |
| [modificación usuarios.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20usuarios.py) | Normalización de datos de usuarios de FarmaOnline                                               |
| [modificación ventas.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20ventas.py) | Ajustes finales sobre la tabla de ventas y verificación de integridad relacional               |
| [proyecto_suizo_dataset.xlsx](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/proyecto_suizo_dataset.xlsx) | Dataset final estructurado para análisis, con todas las relaciones entre tablas                 |
| [Dashboard Suizo Argentina.pbix](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Dashboard%20Suizo%20Argentina.pbix) | Archivo de Power BI con el modelo, medidas DAX y visualizaciones del reporte ejecutivo          |
| [Screenshot reporte ejecutivo.png](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Screenshot%20reporte%20ejecutivo.png) | Captura de pantalla del dashboard con visualizaciones de KPIs, evolución temporal y segmentación |

---

## 🖼️ Vista previa del Dashboard

![Screenshot del reporte](Screenshot%20reporte%20ejecutivo.png)

---

# 📊 Business Intelligence Analysis - Executive Commercial Report Suizo Argentina S.A.

This project simulates a **monthly executive analysis** for the commercial area of **Suizo Argentina S.A.**, a healthcare company that markets and distributes medical products, perfumery, medicines, and hospital supplies across the country.  
The main goal was to **design a functional Power BI dashboard** that enables tracking of key KPIs such as **revenue, margin, and costs**, with relevant slicers and visualizations for strategic decision-making.

---

## ⚙️ Data Generation and Processing

The dataset was fully generated in Python using **faker**, **random**, **numpy**, and **pandas** libraries, simulating realistic commercial operations with **business and demographic** criteria specific to the healthcare sector.

- Tables were generated for customers, products, sales, sales details, pharmacies, and digital channel users (Farmaonline).
- The data was then **cleaned, transformed, and structured into related tables** ready to be modeled in Power BI.
- Manual adjustments and modifications were applied to enhance the **dataset’s realism**, such as prices, dates, provinces, and product categorizations.

---

## 🧠 Modeling and Visualization in Power BI

- An **optimized data model** was designed in Power BI, using appropriate relationships and custom DAX measures.
- **Time intelligence functions** were implemented for monthly and quarterly analysis, and visualizations were designed following **brand visual identity** principles.
- The dashboard includes interactive filters by **quarter and customer type**, and visualizations that allow quick detection of key trends and variations in commercial performance.

---

## 📌 Key Metrics and Visualizations

- **KPI Cards:** Total Revenue 💰 | Average Margin 📈 | Costs 💸
- **Charts:**  
  - Revenue by product category 🧴  
  - Revenue by province 🗺️  
  - Revenue by sales channel 🛒  
  - Revenue and margin temporal evolution 🕒  

---

## 🧾 Included Files

| File                                                                                          | Description                                                                                     |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [generación costo.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/generación%20costo.py) | Script to simulate unit costs of products using margin logic                                   |
| [generación detalle_venta.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/generación%20detalle_venta.py) | Generation of sales detail with quantities, prices, and cross-references                       |
| [Generación Tablas - Suizo Argentina.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Generación%20Tablas%20-%20Suizo%20Argentina.py) | Main script to generate the base tables with simulated data                                   |
| [modificación clientes.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20clientes.py) | Customer adjustments based on demographic and commercial segmentation criteria                 |
| [modificación farmacia.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20farmacia.py) | Cleaning and standardizing pharmacy data                                                      |
| [modificación fechas.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20fechas.py) | Conversion and correction of date formats for temporal consistency                            |
| [modificación precio.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20precio.py) | Adjustment of simulated prices considering margin and seasonality logic                      |
| [modificación productos.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20productos.py) | Review and improvement of product attributes (categories, units, etc.)                      |
| [modificación provincias.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20provincias.py) | Enrichment of provinces with geographic and commercial data                                  |
| [modificación usuarios.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20usuarios.py) | Normalization of Farmaonline user data                                                       |
| [modificación ventas.py](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/modificación%20ventas.py) | Final adjustments on the sales table and integrity checks                                   |
| [proyecto_suizo_dataset.xlsx](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/proyecto_suizo_dataset.xlsx) | Final structured dataset for analysis, with all relational tables                            |
| [Dashboard Suizo Argentina.pbix](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Dashboard%20Suizo%20Argentina.pbix) | Power BI file containing the model, DAX measures, and executive report visualizations       |
| [Screenshot reporte ejecutivo.png](https://github.com/LeonelToro/BI_SuizoArgentina/blob/main/Screenshot%20reporte%20ejecutivo.png) | Screenshot of the dashboard showing KPIs, temporal evolution, and filtering                   |

---

## 🖼️ Dashboard Preview

![Report Screenshot](Screenshot%20reporte%20ejecutivo.png)

---


