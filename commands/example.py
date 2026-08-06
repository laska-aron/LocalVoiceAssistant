def register():

    return {

        "triggers": [
            r"hello assistant",
            r"say hello"
        ],

        "execute": execute
    }



def execute(api, match):

    api.say(
        "Hello. Regex command framework is working."
    )