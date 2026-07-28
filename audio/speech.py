from __future__ import annotations

import json

from vosk import Model, KaldiRecognizer


class SpeechRecognizer:

    def __init__(self, model_path: str):

        print("Loading speech model...")

        self.model = Model(model_path)

        self.recognizer = KaldiRecognizer(
            self.model,
            16000
        )

        print("Speech model loaded.")


    def process_audio(self, data: bytes) -> str | None:

        if self.recognizer.AcceptWaveform(data):

            result = json.loads(
                self.recognizer.Result()
            )

            text = result.get("text")

            if text:
                return text

        return None