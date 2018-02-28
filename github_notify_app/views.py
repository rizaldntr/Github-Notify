from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import json

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        push_message = ""
        push_message += "====================================\n"
        push_message += "Author: " + body['commit']['author']['name'] + "\n"
        push_message += "Branch: " + body['object_attributes']['ref'] + "\n"
        push_message += "Status: " + body['object_attributes']['status'] + "\n"
        push_message += "Commit Message: " + body['commit']['message'] + "\n"
        push_message += "Commit Url: " + body['commit']['url'] + "\n"
        push_message += "Details\n"

        for build in body['builds'] :
            push_message += "    Name: " + build['name'] + "\n"
            push_message += "    Status: " + build['status'] + "\n"
            push_message += "=============" + "\n"

        push_message += "===================================="

        line_bot_api.push_message("Ce19e93427b803f272445591d66546738", TextSendMessage(text=push_message))

        # #             line_bot_api.reply_message(
        # #                 event.reply_token,
        # #                 TextSendMessage(text=event.message.text)
        # #             )
        #

        # Ce19e93427b803f272445591d66546738
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
