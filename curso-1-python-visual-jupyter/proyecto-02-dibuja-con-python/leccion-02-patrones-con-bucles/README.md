# Lección 02 — Patrones con Bucles

## Objetivo

Entender qué es un bucle `for` usándolo para dibujar patrones repetitivos.

## ¿Qué vas a construir?

Patrones visuales: filas de círculos, cuadrículas de colores, espirales y más.

## Conceptos nuevos

- **`for i in range(n)`:** repite el bloque `n` veces.
- **`i`:** variable que cambia en cada vuelta del bucle.
- **Cálculo de posición:** usar `i` para calcular dónde dibujar cada figura.
- **`range(inicio, fin, paso)`:** controlar el bucle con más precisión.

## Pasos

1. Abre `patrones.ipynb`.
2. En la primera sección, observa cómo `i` cambia la posición de cada círculo.
3. Modifica el `range` y mira qué pasa con el patrón.

## ¿Qué debería pasar?

Verás cómo un bucle dibuja 10, 20 o 50 figuras con una sola instrucción. Al cambiar parámetros del bucle, el patrón cambia por completo.

## Mini reto

Crea un patrón de 5 filas de 5 cuadrados, donde cada fila tenga un color diferente.

## Errores comunes

| Error | Causa probable |
|---|---|
| Todos los círculos están encima del mismo punto | No estás usando `i` para calcular la posición x. |
| El bucle no termina | Pusiste un `while` sin condición de parada. Reinicia el kernel. |
