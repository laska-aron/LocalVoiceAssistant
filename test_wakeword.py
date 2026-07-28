from audio.microphone import MicrophoneManager
from audio.wakeword import WakeWordDetector


mic = MicrophoneManager()

wake = WakeWordDetector()


mic.start()


print("Say wake word...")


while True:

    audio = mic.read()

    if wake.process(audio):

        print("Wake word detected!")