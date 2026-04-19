# Lección 02 — Explora Datos con Filtros

## Objetivo

Usar pandas para filtrar datos y responder preguntas concretas sobre el dataset.

## ¿Qué vas a construir?

Un notebook donde haces preguntas al dataset y obtienes respuestas visuales.

## Conceptos nuevos

- **Filtro:** `df[df["columna"] > valor]` — selecciona filas que cumplen una condición.
- **`.value_counts()`:** cuenta cuántas veces aparece cada valor.
- **`.groupby()`:** agrupa datos por una categoría.
- **`.mean()`:** calcula el promedio.
- **Comparaciones:** `>`, `<`, `==`, `>=`, `!=`

## Pasos

1. Abre `filtros.ipynb`.
2. Lee cada pregunta antes de ejecutar la celda.
3. Modifica los filtros para hacer tus propias preguntas.

## ¿Qué debería pasar?

Cada celda responde una pregunta diferente sobre el dataset con texto o un gráfico.

## Mini reto

Responde esta pregunta con código: ¿Cuál género tiene mayor calificación promedio?

## Errores comunes

| Error | Causa probable |
|---|---|
| `KeyError: 'columna'` | El nombre de la columna está mal escrito. |
| El filtro devuelve 0 filas | La condición es demasiado estricta. Prueba con valores menos extremos. |
