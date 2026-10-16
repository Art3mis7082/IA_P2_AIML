# Importamos las bibliotecas
import time
import aiml
import os
import unicodedata


if not hasattr(time, "clock"):
    setattr(time, "clock", time.perf_counter)

# Definimos la función para iniciar el chatbot
def iniciar_bot():
    # 1. Crear el kernel (motor) de AIML
    kernel = aiml.Kernel()

    # 2. Cargar las bases AIML modulares
    carpeta_intenciones = "intenciones"
    if os.path.isdir(carpeta_intenciones):
        archivos_aiml = sorted(
            os.path.join(carpeta_intenciones, nombre)
            for nombre in os.listdir(carpeta_intenciones)
            if nombre.lower().endswith(".aiml")
        )
    else:
        archivos_aiml = []

    if not archivos_aiml:
        print(f"Error: No se encontraron archivos AIML en {carpeta_intenciones}.")
        return

    for archivo_aiml in archivos_aiml:
        print(f"Cargando {archivo_aiml}...")
        kernel.learn(archivo_aiml)

    print("\n--- Bot Iniciado ---")
    print("Escribe 'salir' para terminar la conversación.\n")

    # 3. Ciclo  infinito para chatear
    while True:
        entrada_usuario = input("> Tú: ")
        
        # Condición para salir del bucle
        if entrada_usuario.lower() in ['salir', 'exit', 'quit']:
            print("> Bot: ¡Hasta luego! Que tengas un buen día.")
            break
        
        # Las reglas AIML se comparan en mayúsculas y sin acentos
        entrada_limpia = unicodedata.normalize("NFD", entrada_usuario.upper())
        entrada_limpia = "".join(
            caracter for caracter in entrada_limpia
            if unicodedata.category(caracter) != "Mn"
        )
        entrada_limpia = entrada_limpia.replace("¿", "").replace("?", "")
        
        # Obtener la respuesta del bot
        respuesta = kernel.respond(entrada_limpia)
        print(f"> Bot: {respuesta}")

if __name__ == "__main__":
    iniciar_bot()
