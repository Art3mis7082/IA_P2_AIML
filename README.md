# Chatbot AIML

Chatbot sencillo desarrollado con Python y AIML. El programa carga las reglas de `bot.aiml` y permite conversar desde la terminal.

## Archivos

- `main.py`: inicia el chatbot, carga la base de conocimientos y recibe los mensajes.
- `bot.aiml`: contiene las preguntas y respuestas del bot.

Los dos archivos deben permanecer en la misma carpeta.

## Requisitos

- Python 3.8 o posterior.
- Acceso a Internet para instalar `aiml`.

Python no necesita compilarse como un programa en C. En este proyecto se ejecuta directamente con el interprete de Python.

## Windows: entorno virtual

Abre PowerShell en la carpeta donde estan `main.py` y `bot.aiml`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install aiml
```

Si PowerShell no permite activar el entorno, puedes ejecutar el programa directamente:

```powershell
& ".\.venv\Scripts\python.exe" ".\main.py"
```

Con el entorno activado, tambien puedes ejecutar:

```powershell
python main.py
```

## Linux: entorno virtual

Abre una terminal en la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install aiml
python main.py
```

Si el comando `python3 -m venv .venv` falla, instala el modulo de entornos virtuales. En Ubuntu o Debian:

```bash
sudo apt update
sudo apt install python3-venv
```

Para salir del entorno virtual:

```bash
deactivate
```

## Uso

Al iniciar el programa se mostrara un mensaje indicando que el bot esta listo. Escribe una pregunta y presiona Enter.

Ejemplos:

```text
Hola
Que juegos incluye el torneo
Cuanto cuesta la inscripcion
Como funcionan las faltas
Que premio hay
```

Para terminar la conversacion escribe:

```text
salir
```

Tambien se aceptan `exit` y `quit`.

## Problemas frecuentes

### No se encuentra `aiml`

El programa se esta ejecutando con otro interprete de Python. Activa `.venv` o usa directamente la ruta del interprete del entorno virtual.

### No se encuentra `bot.aiml`

Ejecuta `main.py` desde la carpeta que contiene ambos archivos:

```text
main.py
bot.aiml
```

### El bot no recibe mensajes

Como el programa utiliza `input()`, ejecutalo en una terminal. En VS Code usa **Run Python File in Terminal**, no la ventana **Output** de Code Runner.
