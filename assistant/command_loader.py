from pathlib import Path
import importlib


class CommandLoader:


    def __init__(self):

        self.commands = []



    def load(self):

        folder = Path("commands")


        for file in folder.glob("*.py"):

            if file.name.startswith("_"):
                continue


            module_name = (
                f"commands.{file.stem}"
            )


            module = importlib.import_module(
                module_name
            )


            if hasattr(module, "register"):

                self.commands.append(
                    module.register()
                )


        return self.commands