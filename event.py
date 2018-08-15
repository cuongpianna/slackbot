import re
import command

class Event:
    def __init__(self,bot):
        self.bot = bot
        self.command = command.Command()

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for e in events:
                self.parse_event(e)

    def parse_event(self,event):
        # if event and 'text' in event:
        #     print(re.match(r'^<@UCA647D46>','<@UCA647D46> sass'))
        if event and 'text' in event and self.bot.bot_id in event['text'] and re.match(r'^<@UCA647D46>',event['text']) is not None:
            self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])
        elif event and 'type' in event and event['type'] == 'message':
            self.bot.slack_client.rtm_send_message(
                event['channel'], 'Hihiihi'
            )

    def handle_event(self, user, command, channel):
        if command and channel:
            print("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handle_command(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    def reply(self,event):
        if event and 'type' in event and event['type'] == 'message':
            self.bot.slack_client.rtm_send_message(
                event['channel'],'sss'
            )
    def test(self,event):
        if event and 'text' in event:
            print(event)

