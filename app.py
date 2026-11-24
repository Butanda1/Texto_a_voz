import os
import wave
import urllib.request
from datetime import datetime
import gradio as gr
from piper.voice import PiperVoice

# Configuración de voz y rutas
VOICES_DIR = "voces"
MODEL_NAME = "es_MX-ald-medium"
MODEL_PATH = os.path.join(VOICES_DIR, f"{MODEL_NAME}.onnx")
CONFIG_PATH = os.path.join(VOICES_DIR, f"{MODEL_NAME}.onnx.json")

BASE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/ald/medium"
MODEL_URL = f"{BASE_URL}/{MODEL_NAME}.onnx"
CONFIG_URL = f"{BASE_URL}/{MODEL_NAME}.onnx.json"

def asegurar_modelo():
    """Descarga automáticamente el modelo de voz si no existe localmente."""
    os.makedirs(VOICES_DIR, exist_ok=True)
    archivos = [
        (CONFIG_PATH, CONFIG_URL),
        (MODEL_PATH, MODEL_URL)
    ]
    for path, url in archivos:
        if not os.path.exists(path):
            print(f"Descargando {os.path.basename(path)} desde Hugging Face...")
            urllib.request.urlretrieve(url, path)
            print(f"Descarga finalizada: {path}")

# Asegurar que los archivos del modelo estén disponibles
asegurar_modelo()

def generar(texto):
    if not texto or not texto.strip():
        return None, "Error: El texto está vacío."
    
    # Cargar el motor Piper
    voice = PiperVoice.load(MODEL_PATH, config_path=CONFIG_PATH)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"outputs/Audio_{timestamp}.wav"
    
    # Crear carpeta de salida si no existe
    os.makedirs("outputs", exist_ok=True)
    
    # Generar el audio
    with wave.open(output_path, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(voice.config.sample_rate)
        for chunk in voice.synthesize(texto):
            wav_file.writeframes(chunk.audio_int16_bytes)
        
    return output_path, f"Audio generado con éxito: {output_path}"

# Interfaz visual con Gradio
with gr.Blocks(title="Texto a Voz - Piper TTS") as demo:
    gr.Markdown("# 🎙️ Piper TTS: Texto a Voz")
    gr.Markdown("Convierte texto a audio WAV de forma local, rápida y sin límites.")
    
    with gr.Row():
        with gr.Column():
            entrada = gr.Textbox(label="Texto a sintetizar", lines=12, placeholder="Escribe o pega aquí el texto...")
            boton = gr.Button("GENERAR AUDIO", variant="primary")
        with gr.Column():
            salida_audio = gr.Audio(label="Audio Generado", type="filepath")
            log = gr.Textbox(label="Estado")

    boton.click(generar, inputs=entrada, outputs=[salida_audio, log])

if __name__ == "__main__":
    demo.launch()
