def register():

    return {

        "triggers": [
            r"test confirmation"
        ],

        "execute": execute
    }



def execute(api, match):

    result = api.confirm(
        "Do you want me to continue?"
    )


    if result:

        api.say(
            "You confirmed."
        )


    else:

        api.say(
            "You cancelled."
        )