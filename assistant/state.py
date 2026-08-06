from enum import Enum


class AssistantState(Enum):

    WAITING_WAKEWORD = 1
    SPEAKING = 2
    LISTENING_COMMAND = 3
    LISTENING_QUESTION = 4
    EXECUTING_COMMAND = 5