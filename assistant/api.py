from __future__ import annotations
from assistant.state import AssistantState

class AssistantAPI:


    def __init__(self, assistant):

        self.assistant = assistant



    def say(self, text: str):
        text = text.replace(
            ",",
            ", "
        )

        text = text.replace(
            ".",
            ". "
        )

        self.assistant.say(text)



    def question(self, text):

        self.assistant.state = (
            AssistantState.LISTENING_QUESTION
        )


        self.assistant.say(
            text
        )


        answer = (
            self.assistant.listen_command()
        )


        self.assistant.state = (
            AssistantState.EXECUTING_COMMAND
        )


        return answer



    def confirm(self, text):

        self.assistant.state = (
            AssistantState.LISTENING_QUESTION
        )

        self.assistant.say(text)

        answer = (
            self.assistant.listen_command()
        )

        self.assistant.state = (
            AssistantState.EXECUTING_COMMAND
        )

        if answer is None:
            return False

        answer = answer.lower()

        yes_words = [
            "yes",
            "yeah",
            "correct",
            "sure",
            "okay",
            "ok"
        ]

        no_words = [
            "no",
            "nope",
            "cancel",
            "don't"
        ]

        for word in yes_words:

            if word in answer:
                return True

        for word in no_words:

            if word in answer:
                return False

        self.assistant.say(
            "I did not understand. Please answer yes or no."
        )

        return self.confirm(text)