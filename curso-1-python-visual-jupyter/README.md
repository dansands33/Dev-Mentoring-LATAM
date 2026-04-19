# Curso 1 — Python Visual con Jupyter

Bienvenido. Este curso está hecho para que aprendas Python de forma visual, interactiva y sin frustraciones.

No necesitas saber nada de programación para empezar. Solo necesitas curiosidad y ganas de experimentar.

---

## ¿Qué vas a aprender?

| Proyecto | Lo que construyes |
|---|---|
| 01 — Primer Wow | Controlas colores, textos y figuras con sliders y botones |
| 02 — Dibuja con Python | Creas patrones y figuras usando bucles y funciones |
| 03 — Datos con Vida | Exploras datos reales con gráficos interactivos |
| 04 — Juego o Simulador | Construyes un mini juego funcional en el notebook |

---

## ¿Cómo instalar el entorno?

### En Windows

```bash
# 1. Abre la terminal (busca "cmd" o "PowerShell")
python -m venv venv
venv\Scripts\activate

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Abre Jupyter
jupyter notebook
```

### En Mac

```bash
# 1. Abre la terminal
python3 -m venv venv
source venv/bin/activate

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Abre Jupyter
jupyter notebook
```

> Si ves un mensaje de error al activar el entorno en Windows, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## ¿Cómo abrir Jupyter?

1. Activa tu entorno virtual (pasos de arriba).
2. Desde la carpeta del curso, ejecuta `jupyter notebook`.
3. Se abrirá una ventana en tu navegador.
4. Navega hasta la carpeta del proyecto y abre el archivo `.ipynb`.

---

## ¿Cómo recorrer el curso?

Sigue el orden de los proyectos y las lecciones.  
Cada lección tiene su propio `README.md` con instrucciones paso a paso.

```
proyecto-01-primer-wow/
  leccion-01-hola-jupyter/      ← empieza aquí
  leccion-02-variables/
  ...
```

---

## Consejos para no frustrarte

- Si algo no funciona, lee el mensaje de error completo. Casi siempre dice exactamente qué pasó.
- No copies el código sin leerlo. Cambia una cosa y observa qué pasa.
- Está bien no entender todo a la primera. Sigue adelante y vuelve después.
- Pregunta. Siempre vale la pena preguntar.

---

## Reglas simples de trabajo

1. Lee el README antes de abrir el notebook.
2. Ejecuta cada celda en orden, de arriba hacia abajo.
3. Cuando termines una lección, intenta el mini reto al final.
4. Guarda tu trabajo con `Ctrl+S` (o `Cmd+S` en Mac).

---

## Estructura del curso

```
curso-1-python-visual-jupyter/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── plan_del_curso.md
│   ├── guia_profesor.md
│   └── guia_instalacion_windows_mac.md
├── shared/
│   ├── data/
│   ├── images/
│   └── utils/
├── proyecto-01-primer-wow/
├── proyecto-02-dibuja-con-python/
├── proyecto-03-datos-con-vida/
└── proyecto-04-juego-o-simulador/
```

---

¡Buena suerte! Recuerda: el objetivo no es terminar rápido, sino entender lo que estás construyendo.
