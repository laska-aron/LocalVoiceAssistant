from dataclasses import dataclass


@dataclass
class Command:

    action: str

    target: str | None = None

    data: dict | None = None



class CommandParser:


    def parse(self, text: str):

        text = text.lower().strip()


        if text.startswith("open "):

            return Command(
                action="open",
                target=text[5:]
            )


        if text == "play music":

            return Command(
                action="play_music"
            )


        return None