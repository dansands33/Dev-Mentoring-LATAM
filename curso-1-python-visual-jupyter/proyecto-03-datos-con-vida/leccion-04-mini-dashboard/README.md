# Lección 04 — Mini Dashboard

## Objetivo

Construir un panel que combine tabla resumen, gráfico y controles en una sola vista.

## ¿Qué vas a construir?

Un mini dashboard de videojuegos con métricas clave, gráfico principal y filtros interactivos.

## Conceptos usados

- `widgets.Output` para mostrar tabla y gráfico juntos.
- `widgets.VBox` / `HBox` para organizar el layout.
- `interactive_output` para conectar múltiples controles.
- `df.describe()` y `groupby` para resúmenes estadísticos.

## Pasos

1. Abre `dashboard.ipynb`.
2. Ejecuta todas las celdas.
3. Interactúa con el dashboard completo.

## ¿Qué debería pasar?

Verás un panel con controles a la izquierda y un gráfico a la derecha. Al cambiar los controles, todo el panel se actualiza.

## Mini reto

Agrega una tarjeta de "Datos clave" que muestre en texto:
- El juego mejor calificado del filtro actual
- El juego con más horas del filtro actual

## Errores comunes

| Error | Causa probable |
|---|---|
| El dashboard no se actualiza | Ejecuta todas las celdas en orden desde el inicio. |
| La tabla aparece cortada | Usa `pd.set_option("display.max_rows", 20)` al inicio. |
