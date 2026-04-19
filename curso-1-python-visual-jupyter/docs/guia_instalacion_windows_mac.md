# Guía de Instalación

Sigue los pasos de tu sistema operativo. No te saltes ninguno.

---

## Windows

### 1. Verifica que tienes Python instalado

Abre la terminal (busca "cmd" en el menú de inicio) y escribe:

```
python --version
```

Deberías ver algo como `Python 3.10.x` o superior.  
Si ves un error, descarga Python desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar "Add Python to PATH" durante la instalación.

---

### 2. Clona o descarga el repositorio

**Opción A — con Git:**
```
git clone https://github.com/tu-usuario/curso-1-python-visual-jupyter.git
cd curso-1-python-visual-jupyter
```

**Opción B — sin Git:**  
Descarga el ZIP desde GitHub, descomprímelo y entra a la carpeta.

---

### 3. Crea el entorno virtual

```
python -m venv venv
```

---

### 4. Activa el entorno virtual

```
venv\Scripts\activate
```

Si aparece un error de permisos, ejecuta primero (una sola vez):
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando el entorno esté activo, verás `(venv)` al inicio de la línea.

---

### 5. Instala las dependencias

```
pip install -r requirements.txt
```

Espera a que termine. Puede tardar unos minutos la primera vez.

---

### 6. Abre Jupyter

```
jupyter notebook
```

Se abrirá una ventana en tu navegador. Si no se abre automáticamente, copia la URL que aparece en la terminal (algo como `http://localhost:8888/...`).

---

### 7. Para cerrar

- Cierra la pestaña del navegador.
- En la terminal, presiona `Ctrl + C` para detener el servidor.
- Desactiva el entorno con: `deactivate`

---

## MacOS

### 1. Verifica que tienes Python instalado

Abre la terminal y escribe:

```bash
python3 --version
```

Deberías ver `Python 3.10.x` o superior.  
Si no está instalado, instala [Homebrew](https://brew.sh/) y luego:

```bash
brew install python
```

---

### 2. Clona o descarga el repositorio

```bash
git clone https://github.com/tu-usuario/curso-1-python-visual-jupyter.git
cd curso-1-python-visual-jupyter
```

---

### 3. Crea el entorno virtual

```bash
python3 -m venv venv
```

---

### 4. Activa el entorno virtual

```bash
source venv/bin/activate
```

Verás `(venv)` al inicio de la línea cuando esté activo.

---

### 5. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

### 6. Abre Jupyter

```bash
jupyter notebook
```

---

### 7. Para cerrar

- Cierra la pestaña del navegador.
- En la terminal: `Ctrl + C`
- Desactiva el entorno: `deactivate`

---

## Problemas comunes

| Problema | Solución |
|---|---|
| `python` no se reconoce en Windows | Instala Python y marca "Add to PATH" |
| Error de permisos en Windows | Ejecuta el comando `Set-ExecutionPolicy` indicado arriba |
| Los widgets no aparecen | Asegúrate de instalar desde `requirements.txt` dentro del venv |
| El notebook no carga | Cierra Jupyter, reactiva el venv y vuelve a ejecutar `jupyter notebook` |
| `ModuleNotFoundError` | El venv no está activo. Actívalo y vuelve a intentar |
