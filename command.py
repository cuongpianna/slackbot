class Command(object):
    def __init__(self):
        self.commands = {
            "jump": self.jump,
            "help": self.help
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Lệnh không đúng rồi! " + command + ". " + self.help()

        return response

    def jump(self):
        return "test jump"

    def help(self):
        response = "Boss hỗ trợ các lệnh này nè\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response