from telethon.sync import TelegramClient
from datetime import datetime, timedelta, timezone

API_ID = "YOUR API_ID"
API_HASH = 'YOUR HASH_API'
session_name = 'session name (any)'

client = TelegramClient(session_name, API_ID, API_HASH)

#return 10 last dialogs (or more)
def get_dialogs(limit=10):
    dialogs = client.get_dialogs(limit=limit)
    return dialogs


#returns a list of up to 100 messages in the dialog,
#or stops when it reaches a message older than 30 days
#limit and days can be changed
def get_messages(dialog, days_back=30, limit=100):

    #last possibly day
    since_date = datetime.now(timezone.utc) - timedelta(days=days_back)

    messages = []

    #chek every message's in dialog
    for message in client.iter_messages(dialog, limit=limit, reverse=False):
        #if older than 30 days -> break
        if message.date < since_date:
            break
        #if it's a picture or voice message -> skip
        if not message.text:
            continue

        #every message save in dict format
        messages.append({
            "date": message.date.isoformat(),
            "sender_id": message.sender_id,
            "text": message.text
        })

    return messages