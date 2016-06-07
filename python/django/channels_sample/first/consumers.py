from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


def ws_add(message):
    Group("chat").add(message.reply_channel)

def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

def ws_message(message):
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })