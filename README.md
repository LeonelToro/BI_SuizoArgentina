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
  - Facturación por categoría de producto 🧴  
  - Facturación por provincia 🗺️  
  - Facturación por canal de venta 🛒  
  - Evolución temporal de facturación y margen 🕒  

---

## 🧾 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| `Generación Tablas - Suizo Argentina.py` | Script principal de generación de datos (clientes, productos, ventas, farmacias, usuarios) |
| `generación costo.py` | Generación de costos por producto |
| `generación detalle_venta.py` | Generación del detalle de cada venta |
| `modificación clientes.py` | Ajustes comerciales y demográficos en la tabla de clientes |
| `modificación farmacia.py` | Enriquecimiento de atributos para farmacias |
| `modificación fechas.py` | Simulación realista de fechas de operación |
| `modificación precio.py` | Modificación de precios según categoría |
| `modificación productos.py` | Ajustes de categorías, marcas y presentación |
| `modificación provincias.py` | Asignación de provincias por lógica de distribución |
| `modificación usuarios.py` | Simulación de usuarios del canal digital |
| `modificación ventas.py` | Cálculos adicionales y refinamiento de la tabla de ventas |
| `proyecto_suizo_dataset.xlsx` | Dataset final integrado y listo para carga en Power BI |
| `Dashboard Suizo Argentina.pbix` | Archivo de Power BI con el dashboard ejecutivo mensual |
| `Screenshot reporte ejecutivo.png` | Captura del tablero visual final |

---

## 🖼️ Vista previa del Dashboard

![Screenshot del reporte](Screenshot%20reporte%20ejecutivo.png)

---

## 📬 Contacto

📧 leoneltoro.dev@gmail.com  
🔗 [Mi LinkedIn](https://www.linkedin.com/in/leonel-toro/)
