import os

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
AUDIO_DIR = os.path.join(DATA_DIR, "audio")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
TRANSCRIPTIONS_DIR = os.path.join(DATA_DIR, "transcriptions")

# Configuración de FFmpeg
# Configuración de FFmpeg
FFMPEG_PATH = "C:/ProgramData/chocolatey/bin/ffmpeg.exe"
FFPROBE_PATH = "C:/ProgramData/chocolatey/bin/ffprobe.exe"

# Configuración de la aplicación
APP_TITLE = "Analizador de Velocidad Lectora"
LOGO_PATH = os.path.join(BASE_DIR, "app", "web", "static", "logo.jpg")

# Configuración de formatos de audio permitidos
ALLOWED_AUDIO_FORMATS = ["wav", "mp3", "m4a", "ogg", "aac", "opus"]

# Configuración de servicios externos
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
GOOGLE_DRIVE_API_KEY = os.getenv("GOOGLE_DRIVE_API_KEY", "your_google_drive_api_key")