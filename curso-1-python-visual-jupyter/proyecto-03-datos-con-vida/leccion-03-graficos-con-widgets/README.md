# Lección 03 — Gráficos con Widgets

## Objetivo

Conectar widgets de ipywidgets con gráficos de pandas/matplotlib para explorar datos de forma interactiva.

## ¿Qué vas a construir?

Un explorador de datos interactivo donde cambiar un dropdown actualiza el gráfico automáticamente.

## Conceptos nuevos

- **`Dropdown`:** widget para seleccionar entre varias opciones.
- **`interact` con datos:** usar `interact` para filtrar y graficar según la selección.
- **Función que grafica:** combinar pandas y matplotlib dentro de una función.

## Pasos

1. Abre `graficos_widgets.ipynb`.
2. Ejecuta todas las celdas en orden.
3. Usa los dropdowns para explorar diferentes vistas del dataset.

## ¿Qué debería pasar?

Al cambiar la selección del dropdown, el gráfico se actualiza con los datos filtrados.

## Mini reto

Agrega un segundo dropdown que permita elegir entre mostrar "calificacion" o "horas_promedio" en el eje Y del gráfico.

## Errores comunes

| Error | Causa probable |
|---|---|
| El gráfico no se actualiza | La función no usa los parámetros del widget. Revisa los nombres. |
| `KeyError` dentro del widget | El nombre de la columna tiene un error tipográfico. |
