def register():

    return {

        "triggers": [
            r"ask me something"
        ],

        "execute": execute
    }



def execute(api, match):

    answer = api.question(
        "What is your favorite color?"
    )


    api.say(
        f"You said {answer}"
    )