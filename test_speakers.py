from TTS.api import TTS


tts = TTS(
    "tts_models/en/vctk/vits"
)


print("Available speakers:")

for speaker in tts.speakers:
    print(speaker)