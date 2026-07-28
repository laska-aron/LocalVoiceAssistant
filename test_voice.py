from audio.microphone import MicrophoneManager
from audio.speech import SpeechRecognizer


MODEL_PATH = (
    "models/vosk-model-en-us-0.42-gigaspeech"
)


microphone = MicrophoneManager()

recognizer = SpeechRecognizer(
    MODEL_PATH
)


microphone.start()


print("Listening...")


try:

    while True:

        data = microphone.read()

        text = recognizer.process_audio(data)

        if text:

            print(
                "You said:",
                text
            )


except KeyboardInterrupt:

    print("Stopping...")

    microphone.stop()