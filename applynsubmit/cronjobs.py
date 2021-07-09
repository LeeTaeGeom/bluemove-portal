####
#### Django
####
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bluemoveportal.settings")
django.setup()

from django.conf import settings


# models
from .models import Applymembership
from .models import ApplymembershipNoti

# Slack
from slack_sdk import WebClient

# multiple functions
import datetime

# secrets
slack_bot_token = getattr(settings, "SLACK_BOT_TOKEN", "SLACK_BOT_TOKEN")

# Bluemove data
management_all_channel_id = "CV3THBHJB"


####
#### cron jobs
####
apps_notified = Applymembership.objects.filter(notified=True)
notis_sent = ApplymembershipNoti.objects.filter(sent=True)
for app in apps_notified:
    if app.will_be_deleted_at < datetime.datetime.now():
        app.delete()
        app.applicant.delete()
for noti in notis_sent:
    if noti.will_be_deleted_at < datetime.datetime.now():
        client = WebClient(token=slack_bot_token)
        try:
            client.conversations_join(channel=management_all_channel_id)
        except:
            pass
        client.chat_postMessage(
            channel=management_all_channel_id,
            link_names=True,
            as_user=True,
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"✂️ '{noti.wanted_title}' 데이터 자동 삭제됨",
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"'{noti.wanted_title}' 관련 모든 데이터가 자동 삭제되었습니다.",
                    },
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*공고 ID:*\n" + noti.wanted_id,
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*삭제일시:*\n"
                            + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        },
                    ],
                },
            ],
            text=f"✂️ '{noti.wanted_title}' 데이터 자동 삭제됨",
        )
        noti.delete()