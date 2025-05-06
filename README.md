# analizador-velocidad-lectura

Objetivo: usar ASR para calcular la velocidad de lectura de un usuario.


## Configuración de variables de entorno

Crea un archivo llamado `variablesEntorno.env` en la raíz del proyecto basado en el archivo de ejemplo `variablesEntorno.env.example`. Configura las siguientes variables:

- `FFMPEG_PATH`: Ruta al ejecutable de FFmpeg.
- `FFPROBE_PATH`: Ruta al ejecutable de FFprobe.
- `DATA_DIR`: Directorio donde se almacenan los datos.
- `ALLOWED_AUDIO_FORMATS`: Formatos de audio permitidos (separados por comas).
