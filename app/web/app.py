import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Configuración CLAVE para Windows (usa rutas absolutas)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CORE_DIR = PROJECT_ROOT / "core"

# Limpia entradas duplicadas y elimina rutas incorrectas en sys.path
sys.path = list(dict.fromkeys(sys.path))
sys.path = [p for p in sys.path if not p.endswith(('app.py', 'app/web'))]

# Agregar CORE_DIR al sys.path si no está presente
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, "/mount/src/aubotleo-test/core")
print("sys.path después de agregar CORE_DIR:", sys.path)

# Importa después de configurar el path
from core.whisper_wrapper import SpeechRecognizer

import streamlit as st
from pydub import AudioSegment
import config

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
FFMPEG_PATH = os.getenv("FFMPEG_PATH")
FFPROBE_PATH = os.getenv("FFPROBE_PATH")
DATA_DIR = os.getenv("DATA_DIR")
ALLOWED_AUDIO_FORMATS = os.getenv("ALLOWED_AUDIO_FORMATS").split(",")

# Título de la aplicación con logo
col1, col2 = st.columns([1, 6])
with col1:
    st.image(config.LOGO_PATH, width=100, use_container_width=True)
with col2:
    st.title("Analizador de Velocidad Lectora")

# Configurar las rutas de FFmpeg y FFprobe
AudioSegment.converter = config.FFMPEG_PATH
AudioSegment.ffprobe = config.FFPROBE_PATH

# Subida de archivo de audio
audio_subido = st.file_uploader("Sube tu grabación", type=config.ALLOWED_AUDIO_FORMATS)

# Campo para pegar el texto de referencia
texto_referencia = st.text_area("Pega el texto a leer")

# Mostrar el texto y el archivo subido (para depuración)
if texto_referencia:
    st.write("Texto de referencia:")
    st.write(texto_referencia)

if audio_subido:
    st.write("Archivo de audio subido:")
    st.audio(audio_subido)

    # Obtener la extensión del archivo
    file_extension = audio_subido.name.split(".")[-1].lower()

    # Convertir el audio a WAV si no está en ese formato
    if file_extension == "wav":
        st.write("El archivo ya está en formato WAV.")
        audio_wav = audio_subido
    else:
        st.write(f"Convirtiendo el archivo {file_extension.upper()} a WAV...")
        try:
            # Guardar el archivo subido temporalmente
            temp_audio_path = os.path.join(config.DATA_DIR, "temp_audio")
            with open(temp_audio_path, "wb") as f:
                f.write(audio_subido.getbuffer())

            # Cargar el archivo con pydub
            audio = AudioSegment.from_file(temp_audio_path, format=file_extension)

            # Convertir a WAV
            audio_wav_path = "temp_audio.wav"
            audio.export(audio_wav_path, format="wav")

            # Mostrar el archivo convertido
            st.write("Archivo convertido a WAV:")
            st.audio(audio_wav_path)

            # Eliminar el archivo temporal
            os.remove("temp_audio")
        except Exception as e:
            st.error(f"Error al convertir el archivo: {e}")
            st.write("Por favor, verifica que el archivo sea válido y esté en un formato soportado.")

print("sys.path después de limpiar:", sys.path)
print("PROJECT_ROOT:", PROJECT_ROOT)
print("CORE_DIR:", CORE_DIR)
print("sys.path:", sys.path)



