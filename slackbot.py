# from slackclient import SlackClient
# import time
#
# slack_client = SlackClient('xoxb-337490698901-418208251142-im2V008fJMZhyGmkeJoduIdE')
#
# api_call = slack_client.api_call('users.list')
# if api_call.get('ok'):
#     users = api_call.get('members')
#     for user in users:
#         print(user.get('name'))

import bot

bot.Bot()

