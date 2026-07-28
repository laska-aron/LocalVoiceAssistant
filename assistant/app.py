from audio.microphone import MicrophoneManager


class VoiceAssistant:

    def __init__(self):

        self.microphone = MicrophoneManager()

    def run(self):

        print()

        print("Detected microphones:\n")

        for device in self.microphone.scan():

            print(
                f"[{device.index}] "
                f"{device.name} "
                f"({device.channels} channels)"
            )