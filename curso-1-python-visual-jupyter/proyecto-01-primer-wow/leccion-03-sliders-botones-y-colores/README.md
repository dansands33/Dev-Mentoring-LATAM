# Lección 03 — Sliders, Botones y Colores

## Objetivo

Usar `ipywidgets` para controlar tu código con sliders, botones y selectores, sin escribir código nuevo cada vez.

## ¿Qué vas a construir?

Un panel interactivo donde mover un slider o hacer clic en un botón cambia lo que aparece en pantalla en tiempo real.

## Conceptos nuevos

- **`ipywidgets`:** librería para crear controles visuales en Jupyter.
- **`interact()`:** función mágica que conecta un widget con una función.
- **`IntSlider`:** un control deslizante para números enteros.
- **`ColorPicker`:** un selector de color visual.
- **`Button`:** un botón que ejecuta código al hacer clic.

## Pasos

1. Abre `widgets.ipynb`.
2. Ejecuta la celda de importaciones.
3. En cada sección, mueve el slider o haz clic en el botón.
4. Observa cómo cambia la figura sin tener que ejecutar la celda de nuevo.

## ¿Qué debería pasar?

Al mover el slider, el gráfico se actualiza automáticamente. Al hacer clic en el botón, algo visible cambia. El código no cambia, solo tus controles.

## Mini reto

Agrega un segundo slider que controle el color (entre 0 y 255) y úsalo para cambiar el tono de rojo de la figura.

## Errores comunes

| Error | Causa probable |
|---|---|
| Los widgets no aparecen, solo texto | Faltó instalar o activar `ipywidgets`. Reinstala con el venv activo. |
| `interact` no actualiza | Asegúrate de que la función dentro de `interact` usa los parámetros correctos. |
| El botón no hace nada | Revisa que el evento `on_click` esté conectado después de crear el botón. |
