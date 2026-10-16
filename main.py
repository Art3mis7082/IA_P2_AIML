# Importamos las bibliotecas
import time
import aiml
import os

if not hasattr(time, "clock"):
    time.clock = time.perf_counter

# Definimos la función para iniciar nuestro chatbot
def iniciar_bot():
    # 1. Crear el kernel (motor) de AIML
    kernel = aiml.Kernel()

    # 2. Cargar el archivo AIML
    archivo_aiml = "bot.aiml"

    # En este bloque pasamos el archivo y mandamos error en caso de que no encuentre la base de conocimientos
    if os.path.isfile(archivo_aiml):
        print(f"Cargando {archivo_aiml}...")
        kernel.learn(archivo_aiml)
    else:
        print(f"Error: No se encontró el archivo {archivo_aiml}.")
        return

    print("\n--- Bot Iniciado ---")
    print("Escribe 'salir' para terminar la conversación.\n")

    # 3. Ciclo  infinito para chatear
    while True:
        entrada_usuario = input("> Tú: ")
        
        # Condición para salir del bucle
        if entrada_usuario.lower() in ['salir', 'exit', 'quit']:
            print("> Bot: ¡Hasta luego! Que tengas un buen día.")
            break
        
        # Las reglas de AIML suelen evaluarse mejor en mayúsculas y sin acentos
        entrada_limpia = entrada_usuario.upper().replace("Ó", "O").replace("¿", "").replace("?", "")
        
        # Obtener la respuesta del bot
        respuesta = kernel.respond(entrada_limpia)
        print(f"> Bot: {respuesta}")

if __name__ == "__main__":
    iniciar_bot()
