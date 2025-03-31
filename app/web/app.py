import streamlit as st
from pydub import AudioSegment
import os
import sys

# Agregar la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from config import FFMPEG_PATH, ALLOWED_AUDIO_FORMATS, LOGO_PATH  # Importar configuraciones

# Título de la aplicación con logo
col1, col2 = st.columns([1, 6])
with col1:
    st.image(LOGO_PATH, width=100, use_container_width=True)
with col2:
    st.title("Analizador de Velocidad Lectora")

# Configurar la ruta de FFmpeg
AudioSegment.converter = FFMPEG_PATH

# Subida de archivo de audio
audio_subido = st.file_uploader("Sube tu grabación", type=ALLOWED_AUDIO_FORMATS)

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
            with open("temp_audio", "wb") as f:
                f.write(audio_subido.getbuffer())

            # Cargar el archivo con pydub
            audio = AudioSegment.from_file("temp_audio", format=file_extension)

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