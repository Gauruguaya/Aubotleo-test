from core.utils import get_audio_duration
import whisper

class SpeechRecognizer:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)
    
    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return {
            "text": result["text"],
            "words": result["text"].split(),
            "duration": get_audio_duration(audio_path)
        }