import os
import sys
from pathlib import Path

# Agrega la ruta al directorio 'core' al sys.path
CORE_DIR = Path(__file__).resolve().parent.parent / "app" / "core"
sys.path.insert(0, str(CORE_DIR))

# Importa después de configurar el path
from whisper_wrapper import SpeechRecognizer

from core.whisper_wrapper import SpeechRecognizer

# Agregar la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path = list(dict.fromkeys(sys.path))  # Elimina duplicados en sys.path

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
            st.write("Por favor, verifica que el archivo sea válido y esté en un formato soportado.")

st.write(f"Rutas en sys.path: {sys.path}")


