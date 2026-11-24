# Texto a Voz (TTS) con Piper y Gradio

Aplicación web local desarrollada en Python utilizando **Gradio** y **Piper TTS** para la síntesis de texto a voz en formato `.wav`. Ejecuta la inferencia de manera local en CPU mediante modelos ONNX, sin depender de APIs externas ni requerir GPU dedicada.

---

## Funcionalidad

- **Síntesis local en CPU:** Emplea el motor ONNX de Piper TTS para generar audio directamente en el equipo local sin envío de datos a servicios externos.
- **Modelo en español:** Configurado con el modelo acústico `es_MX-ald-medium` (español de México).
- **Gestión automática del modelo:** Verifica al iniciar si los archivos `.onnx` y `.onnx.json` existen en `voces/`; en caso contrario, los descarga automáticamente desde Hugging Face.
- **Interfaz web:** Permite ingresar texto, reproducir el resultado en el navegador y exportar el archivo generado mediante Gradio.
- **Almacenamiento organizado:** Guarda cada archivo `.wav` en el directorio `outputs/` utilizando una marca de tiempo en el nombre para evitar sobrescrituras.

---

## Stack Tecnológico

- **Lenguaje:** Python 3.10+
- **Motor de síntesis:** Piper TTS (ONNX Runtime)
- **Interfaz de usuario:** Gradio

---

## Requisitos Previos

- Python 3.10 o superior (probado en Python 3.11).
- `pip` y soporte para entornos virtuales (`venv`).

---

## Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Butanda1/Texto_a_voz.git
   cd Texto_a_voz
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```
   En la primera ejecución se descargarán los archivos del modelo de voz (~60 MB) dentro de `voces/`. Una vez iniciado el servidor, accede a la interfaz en `[http://127.0.0.1:7860](http://127.0.0.1:7860)`.

---

## Estructura del Proyecto

```text
Texto_a_voz/
├── app.py                     # Lógica de síntesis e interfaz web en Gradio
├── requirements.txt           # Dependencias del proyecto (piper-tts, gradio)
├── .gitignore                 # Exclusión de entorno virtual, audios y modelos .onnx
├── README.md                  # Documentación
├── voces/                     # Directorio para modelos ONNX (descarga automática)
│   └── .gitkeep
└── outputs/                   # Directorio de salida para archivos .wav generados
```

---

## Licencia

Distribuido bajo la Licencia MIT.
