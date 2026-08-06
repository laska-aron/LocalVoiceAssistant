from assistant.command_loader import CommandLoader


loader = CommandLoader()

commands = loader.load()


for command in commands:

    print(
        command["triggers"]
    )