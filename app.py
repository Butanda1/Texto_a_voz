import gradio as gr
from piper.voice import PiperVoice
import wave
import os
from datetime import datetime


# Rutas de los modelos 
MODEL = "voces/es_MX-ald-medium.onnx"
CONFIG = "voces/es_MX-ald-medium.onnx.json"

def generar(texto):
    if not texto: return None, "Error: Texto vacío"
    
    # Cargar el motor Piper
    voice = PiperVoice.load(MODEL, config_path=CONFIG)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"outputs/Audio_{timestamp}.wav"
    
    # Crear carpeta de salida si no existe
    if not os.path.exists("outputs"): os.makedirs("outputs")
    
    # Generar el audio de forma ilimitada
    with wave.open(output_path, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(voice.config.sample_rate)
        for chunk in voice.synthesize(texto):
            wav_file.writeframes(chunk.audio_int16_bytes)
        
    return output_path, f"Audio generado con éxito (Licencia MIT): {output_path}"

# Interfaz visual sencilla
with gr.Blocks() as demo:
    gr.Markdown("# Piper TTS: Texto a Voz")
    
    with gr.Row():
        with gr.Column():
            entrada = gr.Textbox(label="Contenido", lines=12, placeholder="Texto")
            boton = gr.Button("GENERAR AUDIO COMPLETO", variant="primary")
        with gr.Column():
            salida_audio = gr.Audio(label="Audio Final")
            log = gr.Textbox(label="Estado")

    boton.click(generar, inputs=entrada, outputs=[salida_audio, log])

if __name__ == "__main__":
    demo.launch()