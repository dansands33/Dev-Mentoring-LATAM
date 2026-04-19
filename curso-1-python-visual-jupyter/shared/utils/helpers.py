"""Funciones de apoyo reutilizables para los notebooks del curso."""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def mostrar_color(color, titulo="Mi color"):
    """Muestra un rectángulo del color indicado."""
    fig, ax = plt.subplots(figsize=(4, 2))
    rect = patches.Rectangle((0, 0), 1, 1, color=color)
    ax.add_patch(rect)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(titulo)
    plt.show()


def dibujar_circulo(x, y, radio, color="blue", ax=None):
    """Dibuja un círculo en la posición dada."""
    if ax is None:
        fig, ax = plt.subplots()
    circ = plt.Circle((x, y), radio, color=color)
    ax.add_patch(circ)
    return ax


def barra_simple(etiquetas, valores, color="steelblue", titulo="Gráfico"):
    """Crea un gráfico de barras simple."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(etiquetas, valores, color=color)
    ax.set_title(titulo)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
