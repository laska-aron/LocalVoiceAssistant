import os


class SystemCommands:


    def open_program(self, name):

        programs = {

            "calculator": "calc.exe",

            "notepad": "notepad.exe"

        }


        if name not in programs:

            print(
                "Unknown program:",
                name
            )

            return


        os.startfile(
            programs[name]
        )



    def shutdown(self):

        os.system(
            "shutdown /s /t 5"
        )