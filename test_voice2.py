from TTS.api import TTS
import sounddevice as sd


tts = TTS(
    "tts_models/en/vctk/vits"
)


while True:

    audio = tts.tts(
        text="Good evening sir. All systems are operational.",
        speaker="p267",
        speed=0.9
    )


    sd.play(
        audio,
        samplerate=22050
    )

    sd.wait()