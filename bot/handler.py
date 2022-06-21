from telegram.ext import CommandHandler


class BotCommandHandler:
    def __init__(self):
        self.handler_list = []

    def __call__(self, command):
        def _(func):
            self.handler_list.append(CommandHandler(command, func))
            return func

        return _


cmd_route = BotCommandHandler()
