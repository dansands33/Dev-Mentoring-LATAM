# Lección 01 — Primer Gráfico

## Objetivo

Cargar datos desde un archivo CSV y crear un gráfico de barras simple.

## ¿Qué vas a construir?

Un gráfico de barras que muestra las calificaciones de videojuegos populares.

## Conceptos nuevos

- **`pandas`:** librería para trabajar con tablas de datos.
- **`pd.read_csv()`:** cargar un archivo CSV.
- **`df.head()`:** ver las primeras filas.
- **`df["columna"]`:** acceder a una columna.
- **Gráfico de barras:** comparar valores entre categorías.

## Pasos

1. Abre `primer_grafico.ipynb`.
2. Ejecuta la celda de carga y observa la tabla.
3. Ejecuta la celda del gráfico y observa el resultado.
4. Prueba cambiar qué columna se grafica.

## ¿Qué debería pasar?

Verás una tabla con datos de videojuegos y luego un gráfico de barras con sus calificaciones.

## Mini reto

Cambia el gráfico para mostrar las **horas promedio** en vez de la calificación. ¿Cuál juego tiene más horas?

## Errores comunes

| Error | Causa probable |
|---|---|
| `FileNotFoundError` | La ruta al CSV es incorrecta. Verifica la ruta relativa. |
| La columna no existe | Escribe exactamente el nombre de la columna, respetando mayúsculas. |
