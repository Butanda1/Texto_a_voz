# 🎙️ Reddit TTS - Piper (Rápido y Ligero)

Aplicación web local desarrollada con **Gradio** y **Piper TTS** para convertir historias y posts de Reddit (o cualquier texto largo) en audio `.wav` de manera ultrarrápida, sin límites de tokens y sin necesidad de tarjeta gráfica (GPU).

---

## ✨ Características

- ⚡ **Rápido y eficiente:** Utiliza el motor ONNX de Piper TTS, diseñado para sintetizar audio rápidamente incluso en CPUs modestas.
- 🆓 **100% Abierto y Local:** Sin llamadas a APIs externas, sin cuotas ni límites de caracteres.
- 🇲🇽 **Voz en español:** Incluye por defecto la voz `es_MX-ald-medium` (Español México).
- 🖥️ **Interfaz Web Sencilla:** Creada con Gradio para generar y reproducir audios directamente en el navegador.

---

## 📋 Requisitos Previos

- Python 3.9 o superior.
- Recomendado crear un entorno virtual para no afectar otras instalaciones de Python.

---

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/reddit_tts_piper.git
   cd reddit_tts_piper
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar el modelo de voz:**
   Asegúrate de que los archivos del modelo estén presentes en la carpeta `voces/`:
   - `voces/es_MX-ald-medium.onnx`
   - `voces/es_MX-ald-medium.onnx.json`

5. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```
   Abre en tu navegador la URL que muestra la terminal (por defecto `http://127.0.0.1:7860`).

---

## 📂 Estructura del Proyecto

```text
reddit_tts_piper/
├── app.py                     # Script principal con la interfaz Gradio
├── requirements.txt           # Dependencias necesarias (piper-tts, gradio)
├── .gitignore                 # Archivos ignorados por Git
├── README.md                  # Documentación
├── voces/                     # Modelos ONNX de Piper
│   ├── es_MX-ald-medium.onnx
│   └── es_MX-ald-medium.onnx.json
└── outputs/                   # Audios generados (creado automáticamente)
```

---

## 📄 Licencia

El código de esta aplicación está bajo la licencia MIT.
