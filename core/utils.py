from pydub.utils import mediainfo

def get_audio_duration(audio_path):
    info = mediainfo(audio_path)
    return float(info["duration"])