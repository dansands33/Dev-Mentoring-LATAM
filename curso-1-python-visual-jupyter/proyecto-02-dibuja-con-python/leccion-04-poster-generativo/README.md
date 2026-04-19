# Lección 04 — Póster Generativo

## Objetivo

Crear una imagen completa generada por código, usando todo lo aprendido en este proyecto.

## ¿Qué vas a construir?

Un póster visual único, generado por tu código. Cada vez que lo ejecutes puede verse diferente.

## Conceptos usados

- Bucles `for` para repetir elementos.
- Funciones para reutilizar formas.
- Variables para controlar el estilo.
- `random` para variación.
- Composición de elementos en un lienzo.

## Pasos

1. Abre `poster.ipynb`.
2. Ejecuta el notebook completo y mira el resultado.
3. Cambia las variables de configuración al inicio para personalizar tu póster.
4. Completa el mini reto final.

## ¿Qué debería pasar?

Verás un póster visual generado completamente por código. Al cambiar parámetros, el póster cambia de aspecto.

## Mini reto

Personaliza el póster con:
- Tu nombre como título
- Tu color favorito como base
- Al menos una forma nueva que no estaba en el original

## Errores comunes

| Error | Causa probable |
|---|---|
| El póster sale vacío | Revisa que `plt.show()` esté al final. |
| Los elementos se salen del lienzo | Genera posiciones usando `random.uniform(margen, 1-margen)` para mantenerte dentro. |
