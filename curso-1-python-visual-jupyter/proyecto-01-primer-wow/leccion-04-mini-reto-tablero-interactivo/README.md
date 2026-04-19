# Lección 04 — Mini Reto: Tablero Interactivo

## Objetivo

Crear un panel visual completo que combine todo lo aprendido: variables, texto, figuras y widgets.

## ¿Qué vas a construir?

Un tablero con controles que cambian figura, color, tamaño y mensaje al mismo tiempo.

## Conceptos nuevos

- **`widgets.HBox` / `widgets.VBox`:** organizar widgets en filas o columnas.
- **`interactive_output`:** conectar múltiples widgets a una función.
- **Composición:** combinar varias cosas aprendidas en una sola.

## Pasos

1. Abre `tablero.ipynb`.
2. Ejecuta todas las celdas en orden.
3. Interactúa con el tablero completo.
4. Luego prueba personalizar al menos una cosa.

## ¿Qué debería pasar?

Verás un panel con sliders, un selector de color y un dropdown. Al cambiar cualquier control, el tablero completo se actualiza.

## Mini reto

Agrega un control extra: un slider de `opacidad` (entre 0.1 y 1.0) que haga la figura más transparente o más sólida.

## Errores comunes

| Error | Causa probable |
|---|---|
| Los controles se ven pero no actualizan | Celda de función no ejecutada. Ejecuta todo desde arriba con `Kernel > Restart & Run All`. |
| `AttributeError: 'NoneType'` | Alguna variable no fue definida. Revisa el orden de ejecución. |
