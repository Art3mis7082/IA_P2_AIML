# VolpeBot AIML

Autor: Beatriz Almaraz Garcia
Materia: Inteligencia Artificial
Profesor: Dr. José Fidel Urquiza Yllescas
Semestre 2027-1

Chatbot sencillo desarrollado con Python y AIML. El programa tiene como fin, responder dudas frecuentes sobre el reglamento del torneo de EsportsFQ, de Volperix Esports Club, para ello creamos una carpeta de intenciones.

## Archivos

- `main.py`: inicia el chatbot, carga las bases de conocimientos y recibe los mensajes.
- `intenciones/`: contiene las preguntas y respuestas separadas por tema.

`main.py` y la carpeta `intenciones/` deben permanecer en la misma carpeta.

## Etiquetas AIML utilizadas

Las intenciones utilizan estas etiquetas y recursos de AIML:

- `<category>`: agrupa una intención completa del bot.
- `<pattern>`: define el texto que activa una intención.
- `<template>`: define la respuesta del bot.
- `<random>`: selecciona una respuesta aleatoria.
- `<li>`: representa una opción dentro de `random` o `condition`.
- `<set>`: guarda un valor, como el nickname o nametag del jugador, en una variable.
- `<get>`: recupera el valor guardado en una variable.
- `<condition>`: selecciona una respuesta según una variable guardada.
- `<that>`: activa una intención dependiendo de la respuesta anterior del bot.
- `<srai>`: redirige una intención hacia otra intención existente.
- `<star/>`: recupera el texto capturado por el comodín `*`.
- `*`: comodín que captura una o más palabras.
- `_`: comodín que captura una o más palabras con prioridad de coincidencia alta.


### Bases de intenciones

- `00_general.aiml`: saludo, ayuda y respuestas generales.
- `01_reglamento.aiml`: convivencia, trampas, faltas, cuentas y roles.
- `02_inscripciones.aiml`: registro, requisitos, equipos y suplentes.
- `03_juegos.aiml`: preguntas específicas de cada videojuego.
- `04_partidas.aiml`: formato, horarios, pausas, comunicación y premios.
- `05_datos.aiml`: datos solicitados, menores de edad y derechos ARCO.

## Dificultades encontradas

### Normalización de caracteres Unicode

Las preguntas con acentos no coincidían con los patrones AIML sin acentos. Se solucionó usando `unicodedata.normalize()` para limpiar la entrada antes de procesarla.

### Compatibilidad con `time.clock`

La biblioteca AIML utiliza la función antigua `time.clock()`, eliminada desde Python 3.8. Se solucionó agregando temporalmente ese atributo con `setattr` y `time.perf_counter`.


## Requisitos

- Python 3.8 o posterior.
- Instalar la biblioteca de AIML

## Windows: entorno virtual

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

## Uso

Al iniciar el programa se mostrara un mensaje indicando que el bot esta listo. Escribe una pregunta y presiona Enter.


### NOTA: El bot no recibe mensajes

Como el programa utiliza `input()`, ejecutalo en una terminal. En VS Code usa **Run Python File in Terminal**, no la ventana **Output** de Code Runner.
