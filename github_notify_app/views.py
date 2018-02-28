from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        body = request.body

        print ("====================================")
        print ("Author: " + body['commit']['author']['name'])
        print ("Branch: " + body['object_attributes']['ref'])
        print ("Status: " + body['object_attributes']['status'])
        print ("Commit Message: " + body['commit']['message'])
        print ("Commit Url: " + body['commit']['url'])
        print ("Details")

        for build in body['builds'] :
            print ("    Name: " + build['name'])
            print ("    Name: " + build['status'])


        # # for event in events:
        # #     print (event)
        # #     if isinstance(event, MessageEvent):
        # #         if isinstance(event.message, TextMessage):
        # #             line_bot_api.reply_message(
        # #                 event.reply_token,
        # #                 TextSendMessage(text=event.message.text)
        # #             )
        #

        # Ce19e93427b803f272445591d66546738
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
