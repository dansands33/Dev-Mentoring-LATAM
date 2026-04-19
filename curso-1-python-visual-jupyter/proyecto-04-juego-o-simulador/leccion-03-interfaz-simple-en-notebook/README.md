# Lección 03 — Interfaz Simple en Notebook

## Objetivo

Usar widgets para crear una interfaz que permita jugar, sin salir del notebook.

## ¿Qué vas a construir?

Un juego de dados con botones, puntaje visible y mensajes de resultado actualizables.

## Conceptos nuevos

- **Estado del juego:** variables que guardan el progreso entre acciones.
- **`widgets.Output`:** área donde aparece el resultado de cada acción.
- **`output.clear_output(wait=True)`:** limpiar y redibujar la salida.
- **Botones con `on_click`:** ejecutar código al hacer clic.

## Pasos

1. Abre `interfaz.ipynb`.
2. Ejecuta todas las celdas.
3. Interactúa: haz clic en los botones para jugar.
4. Observa cómo el estado persiste entre clics.

## ¿Qué debería pasar?

Cada clic del botón ejecuta una ronda, actualiza el puntaje y muestra el resultado. El puntaje se acumula entre rondas.

## Mini reto

Agrega un botón "Reiniciar" que ponga el puntaje de vuelta a 0 y limpie el historial.

## Errores comunes

| Error | Causa probable |
|---|---|
| El puntaje reinicia en cada clic | La variable de puntaje está dentro de la función del botón. Muévela afuera. |
| `output` no muestra nada | Olvidaste hacer `display(output)` o no usaste el contexto `with output:`. |
