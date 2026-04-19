# Lección 02 — Variables que Cambian el Mundo

## Objetivo

Usar variables para controlar lo que ves en pantalla: tamaño, cantidad, color y texto.

## ¿Qué vas a construir?

Un notebook donde cambiar el valor de una variable transforma inmediatamente lo que aparece en pantalla.

## Conceptos nuevos

- **Variable numérica:** guarda un número (`edad = 20`).
- **Variable de texto:** guarda texto (`color = "rojo"`).
- **`matplotlib`:** librería para hacer gráficos y figuras.
- **`fig, ax`:** la figura y el área de dibujo en matplotlib.

## Pasos

1. Abre `variables_mundo.ipynb`.
2. En la primera sección, cambia el valor de `cantidad` y ejecuta.
3. Observa cómo cambia lo que ves.
4. Sigue con cada sección en orden.

## ¿Qué debería pasar?

Al cambiar variables como `cantidad`, `color` o `tamaño`, la figura en pantalla cambia de inmediato. Eso demuestra que la variable es el control de lo que aparece.

## Mini reto

Haz que aparezcan exactamente 7 círculos azules, todos del mismo tamaño.  
Luego cambia el color a verde sin tocar el resto del código.

## Errores comunes

| Error | Causa probable |
|---|---|
| `ModuleNotFoundError: matplotlib` | El venv no está activo o faltó instalar requirements.txt |
| La figura sale vacía | Olvidaste ejecutar la celda de importación al inicio |
| El color no cambia | Asegúrate de escribir el nombre del color en inglés o en formato `"#RRGGBB"` |
