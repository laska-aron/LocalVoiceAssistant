from __future__ import annotations

import pyttsx3


class TextToSpeech:

    def __init__(self):

        self.rate = 170


    def speak(self, text: str):

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            self.rate
        )

        engine.say(
            text
        )

        engine.runAndWait()

        engine.stop()