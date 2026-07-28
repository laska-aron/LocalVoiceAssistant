from __future__ import annotations

import time

from audio.microphone import MicrophoneManager
from audio.wakeword import WakeWordDetector
from audio.speech import SpeechRecognizer
from audio.tts import TextToSpeech

from assistant.parser import CommandParser
from assistant.dispatcher import Dispatcher


class VoiceAssistant:

    def __init__(self):

        self.microphone = MicrophoneManager()

        self.wakeword = WakeWordDetector()

        self.speech = SpeechRecognizer(
            "models/vosk-model-en-us-0.42-gigaspeech"
        )

        self.tts = TextToSpeech()

        self.parser = CommandParser()

        self.dispatcher = Dispatcher()

        self.pending_action = None

    def say(self, text: str):

        print(
            "Assistant:",
            text
        )

        self.microphone.pause()

        self.tts.speak(
            text
        )

        time.sleep(0.5)

        self.microphone.resume()

    def run(self):

        print("Assistant started.")
        print("Waiting for wake word...")


        self.microphone.start()


        while True:

            audio = self.microphone.read()


            if self.wakeword.process(audio):

                print()
                print("Wake word detected!")


                self.microphone.pause()


                self.say(
                    "Yes sir?"
                )


                time.sleep(0.8)


                self.microphone.resume()


                self.handle_command()



    def handle_command(self):

        text = self.listen_command()


        if self.pending_action:

            self.handle_pending_answer(text)

            return


        command = self.parser.parse(text)


        if text is None:
            return


        command = self.parser.parse(
            text
        )


        if command is None:

            self.say(
                "I did not understand."
            )

            return


        result = self.dispatcher.execute(
            command
        )


        self.handle_result(
            result
        )



    def handle_result(self, result):

        if result is None:
            return


        if result["type"] == "question":

            self.say(
                result["text"]
            )


            answer = self.listen_command()

            print(
                "Answer:",
                answer
            )



        elif result["type"] == "execute":

            self.say(
                result["text"]
            )



    def listen_command(self):

        print(
            "Listening for command..."
        )


        while True:

            audio = self.microphone.read()


            text = self.speech.process_audio(
                audio
            )


            if text:

                print(
                    "Command:",
                    text
                )

                return text

    def handle_pending_answer(self, text):

        action = self.pending_action


        if action["action"] == "play_music":

            app = text.lower()


            self.pending_action = None


            self.say(
                f"Opening {app}."
            )

            print(
                "Would open:",
                app
            )