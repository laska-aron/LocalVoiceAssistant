import subprocess


def register():

    return {

        "triggers": [
            r"open (.+)"
        ],

        "execute": execute

    }



def execute(api, match):

    program = match.group(1)

    api.say(
        f"Opening {program}"
    )


    if program == "chrome":

        subprocess.Popen(
            "start chrome",
            shell=True
        )


    elif program == "calculator":

        subprocess.Popen(
            "calc"
        )


    elif program == "notepad":

        subprocess.Popen(
            "notepad"
        )


    else:

        api.say(
            f"I don't know how to open {program}"
        )