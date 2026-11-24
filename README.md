# Texto a Voz (TTS) - Piper & Gradio

Aplicación web local desarrollada con **Gradio** y **Piper TTS** para convertir texto en audio `.wav` de manera ultrarrápida, sin límites de caracteres, completamente privada y sin necesidad de tarjeta gráfica dedicada (GPU).

---

## Características

- **Rápido y eficiente:** Utiliza el motor ONNX de Piper TTS, diseñado para sintetizar voz con alto rendimiento directamente en CPU.
- **100% Local y Privado:** Sin llamadas a servicios externos en la nube, sin cuotas, suscripciones ni límites de caracteres.
- 🇲**Voz en español:** Utiliza la voz `es_MX-ald-medium` (Español de México).
- **Descarga automática:** Si el modelo no está presente, la aplicación lo descarga automáticamente desde Hugging Face al iniciar por primera vez.
- **Interfaz Web Intuitiva:** Desarrollada con Gradio para escribir o pegar textos, generar el audio y escucharlo o descargarlo al instante.
- **Guardado automático:** Almacena los audios generados en la carpeta `outputs/` con marca de tiempo.

---

## Requisitos Previos

- Python 3.10 o superior (recomendado Python 3.11).
- Un entorno virtual para gestionar las dependencias de forma aislada.

---

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Butanda1/Texto_a_voz.git
   cd Texto_a_voz
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   # En Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # En Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```
   *(La primera vez descargará automáticamente el modelo de voz de ~60 MB si no existe en la carpeta `voces/`)*.

   Abre en tu navegador la dirección local que aparece en la terminal (por defecto `http://127.0.0.1:7860`).

---

## Estructura del Proyecto

```text
Texto_a_voz/
├── app.py                     # Aplicación principal con la interfaz de Gradio
├── requirements.txt           # Dependencias necesarias (piper-tts, gradio)
├── .gitignore                 # Archivos ignorados por Git (incluye modelos .onnx)
├── README.md                  # Documentación del proyecto
├── voces/                     # Modelos de voz (descargados automáticamente)
│   ├── .gitkeep
│   ├── es_MX-ald-medium.onnx
│   └── es_MX-ald-medium.onnx.json
└── outputs/                   # Audios WAV generados (creado automáticamente)
```

---

## Licencia

Este proyecto está bajo la Licencia MIT.
