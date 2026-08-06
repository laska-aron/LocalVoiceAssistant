from __future__ import annotations

import time

from audio.microphone import MicrophoneManager
from audio.wakeword import WakeWordDetector
from audio.speech import SpeechRecognizer
from audio.tts import TextToSpeech

from assistant.parser import CommandParser
from assistant.dispatcher import Dispatcher

from assistant.command_loader import CommandLoader
from assistant.api import AssistantAPI

import re

from assistant.state import AssistantState

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

        self.command_loader = CommandLoader()

        self.commands = self.command_loader.load()

        self.api = AssistantAPI(
            self
        )

        self.state = AssistantState.WAITING_WAKEWORD

    def say(self, text: str):

        self.state = AssistantState.SPEAKING

        print(
            "Assistant:",
            text
        )

        self.microphone.pause()

        self.tts.speak(
            text
        )

        #time.sleep(0.5)

        self.microphone.resume()

    def run(self):

        print("Assistant started.")
        print("Waiting for wake word...")


        self.microphone.start()


        while True:

            if self.state != AssistantState.WAITING_WAKEWORD:

                time.sleep(0.01)

                continue

            audio = self.microphone.read()

            if self.wakeword.process(audio):

                self.wakeword.reset()

                print()
                print("Wake word detected!")

                self.say(
                    "Yes sir?"
                )

                #time.sleep(0.5)

                self.handle_command()

                # kis idő a saját hang lecsengésére
                time.sleep(1)

                print()
                print("Waiting for wake word...")


    def execute_command(self, text):

        text = text.lower().strip()


        for command in self.commands:

            for trigger in command["triggers"]:

                match = re.search(
                    trigger,
                    text
                )


                if match:

                    command["execute"](
                        self.api,
                        match
                    )

                    return True


        return False

    def handle_command(self):

        self.state = AssistantState.LISTENING_COMMAND

        text = self.listen_command()

        if text is None:

            self.state = AssistantState.WAITING_WAKEWORD

            return

        self.state = AssistantState.EXECUTING_COMMAND

        handled = self.execute_command(
            text
        )

        if not handled:

            self.say(
                "I don't know that command."
            )

        self.wakeword.reset()

        self.state = AssistantState.WAITING_WAKEWORD

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