from TTS.api import TTS
import sounddevice as sd
import numpy as np


class TextToSpeech:

    def __init__(self):

        print("Loading TTS model...")


        self.tts = TTS(
            "tts_models/en/vctk/vits"
        )


        print("TTS model loaded.")


    def speak(self, text):

        audio = self.tts.tts(
            text=text,
            speaker="p267",
            speed=0.9
        )


        # hangerő növelése
        audio = np.array(audio)

        max_volume = max(abs(audio))

        if max_volume > 0:
            audio = audio / max_volume

        audio = audio * 0.8


        # clipping védelem
        audio = np.clip(
            audio,
            -1,
            1
        )


        sd.play(
            audio,
            samplerate=22050
        )

        sd.wait()