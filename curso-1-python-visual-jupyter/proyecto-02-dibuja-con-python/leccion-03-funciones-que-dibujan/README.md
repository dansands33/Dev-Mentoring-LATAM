# Lección 03 — Funciones que Dibujan

## Objetivo

Definir funciones con parámetros y reutilizarlas para dibujar sin repetir código.

## ¿Qué vas a construir?

Funciones que dibujan flores, casas o estrellas, que puedes llamar muchas veces con diferentes parámetros.

## Conceptos nuevos

- **`def nombre_funcion(parametro1, parametro2):`** cómo definir una función.
- **Parámetros:** los "controles" de la función.
- **Reutilización:** llamar la misma función con distintos valores.
- **Parámetros por defecto:** valores que se usan cuando no se especifica uno.

## Pasos

1. Abre `funciones_dibujo.ipynb`.
2. Lee la función `dibujar_flor` y entiende qué hace cada parámetro.
3. Llama la función con distintos valores y observa el resultado.

## ¿Qué debería pasar?

Una función escrita una vez puede dibujar el mismo elemento en diferentes posiciones, colores y tamaños. Eso es reutilización.

## Mini reto

Crea tu propia función `dibujar_estrella(x, y, tamaño, color)` que dibuje algo en esa posición. Puede ser simple: un círculo con un punto en el centro, por ejemplo.

## Errores comunes

| Error | Causa probable |
|---|---|
| `TypeError: función() missing argument` | Faltó pasar un argumento requerido. |
| La figura aparece en el lugar equivocado | Los parámetros `x` e `y` no se están usando correctamente dentro de la función. |
