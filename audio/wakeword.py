from __future__ import annotations

import numpy as np

import openwakeword
from openwakeword.model import Model


class WakeWordDetector:

    def __init__(self):

        openwakeword.utils.download_models()

        self.model = Model(
            wakeword_models=[
                "hey_jarvis"
            ]
        )


    def process(self, audio: bytes) -> bool:

        audio_array = np.frombuffer(
            audio,
            dtype=np.int16
        )

        prediction = self.model.predict(
            audio_array
        )

        for value in prediction.values():

            if value > 0.5:
                return True

        return False