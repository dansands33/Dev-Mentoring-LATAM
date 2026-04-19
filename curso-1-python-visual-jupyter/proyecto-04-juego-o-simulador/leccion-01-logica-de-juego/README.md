# Lección 01 — Lógica de Juego

## Objetivo

Aprender a usar `if`, `elif` y `else` para crear reglas y condiciones en tu código.

## ¿Qué vas a construir?

Un sistema de reglas simples: decisiones que el código toma según los valores de las variables.

## Conceptos nuevos

- **`if condición:`** ejecuta el bloque si la condición es verdadera.
- **`elif otra_condición:`** revisa otra condición si la anterior fue falsa.
- **`else:`** ejecuta si ninguna condición anterior fue verdadera.
- **Comparaciones:** `>`, `<`, `==`, `!=`, `>=`, `<=`
- **`and` / `or`:** combinar condiciones.

## Pasos

1. Abre `logica.ipynb`.
2. Lee cada sección antes de ejecutar.
3. Cambia los valores de las variables y observa qué rama se ejecuta.

## ¿Qué debería pasar?

El código toma decisiones diferentes según los valores. Cambiar una variable puede cambiar completamente qué mensaje o acción se ejecuta.

## Mini reto

Escribe un sistema de nivel: si el puntaje es menor a 30 es "Principiante", entre 30 y 70 es "Intermedio", mayor a 70 es "Experto". Si el puntaje llega a 100, agrega "¡Perfecto!".

## Errores comunes

| Error | Causa probable |
|---|---|
| `IndentationError` | El bloque después de `if` no tiene sangría correcta. |
| El `else` nunca se ejecuta | Todas las condiciones anteriores son siempre `True`. |
| `=` en vez de `==` | Asignación vs comparación. `=` asigna, `==` compara. |
