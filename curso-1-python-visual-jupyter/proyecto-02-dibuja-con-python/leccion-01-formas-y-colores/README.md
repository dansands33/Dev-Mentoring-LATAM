# Lección 01 — Formas y Colores

## Objetivo

Aprender a dibujar formas básicas con matplotlib: puntos, líneas, círculos y rectángulos.

## ¿Qué vas a construir?

Una hoja de formas donde cada celda agrega un elemento nuevo al lienzo.

## Conceptos nuevos

- **`plt.figure` / `plt.axes`:** el lienzo y el área de dibujo.
- **`plt.scatter`:** dibuja puntos.
- **`plt.plot`:** dibuja líneas.
- **`plt.Circle` / `patches.Rectangle`:** formas geométricas.
- **Coordenadas (x, y):** cómo posicionar elementos en el lienzo.

## Pasos

1. Abre `formas.ipynb`.
2. Ejecuta la primera celda para entender el sistema de coordenadas.
3. Prueba cambiar posiciones y colores en cada celda.

## ¿Qué debería pasar?

Cada celda muestra una figura diferente. Al cambiar los números de posición, la figura se mueve. Al cambiar el color, cambia su apariencia.

## Mini reto

Dibuja 3 figuras diferentes (una de cada tipo) en el mismo lienzo, cada una con un color distinto.

## Errores comunes

| Error | Causa probable |
|---|---|
| La figura aparece vacía | Olvidaste `ax.add_patch(forma)` o los límites son incorrectos. |
| El punto no aparece | Las coordenadas están fuera del rango de `xlim`/`ylim`. |
