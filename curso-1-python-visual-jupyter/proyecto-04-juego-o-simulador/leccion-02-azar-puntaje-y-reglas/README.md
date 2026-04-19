# Lección 02 — Azar, Puntaje y Reglas

## Objetivo

Agregar azar y un sistema de puntaje que se acumula entre rondas.

## ¿Qué vas a construir?

Un juego de dados por texto donde el puntaje sube con cada tirada ganadora.

## Conceptos nuevos

- **`random.randint(a, b)`:** número entero aleatorio entre a y b (inclusive).
- **`random.choice(lista)`:** elige un elemento al azar de una lista.
- **Acumular puntaje:** usar `puntaje += puntos` para sumar.
- **`for` para rondas:** repetir una ronda N veces.

## Pasos

1. Abre `azar.ipynb`.
2. Ejecuta el dado virtual y observa los resultados.
3. Prueba cambiar las reglas para ver cómo afecta el puntaje final.

## ¿Qué debería pasar?

Cada vez que ejecutes la celda principal, el resultado es diferente (es aleatorio). El puntaje se acumula según los resultados.

## Mini reto

Modifica el juego para que si el jugador saca dos dados iguales en la misma ronda, obtenga el doble de puntos esa ronda.

## Errores comunes

| Error | Causa probable |
|---|---|
| `random` no está importado | Agrega `import random` al inicio. |
| El puntaje siempre es 0 | No estás usando `puntaje +=`, sino `puntaje =` (reinicia en cada iteración). |
