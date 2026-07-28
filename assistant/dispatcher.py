from commands.system import SystemCommands


class Dispatcher:


    def __init__(self):

        self.system = SystemCommands()



    def execute(self, command):

        if command.action == "open":

            return {
                "type": "execute",
                "text": f"Opening {command.target}."
            }


        if command.action == "play_music":

            if not command.data:

                return {
                    "type": "question",
                    "text": "Which music app should I use?",
                    "action": "play_music"
                }


            return {
                "type": "execute"
            }


        return {
            "type": "error",
            "text": "Unknown command."
        }