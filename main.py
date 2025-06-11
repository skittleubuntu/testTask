from tg_client import client, get_dialogs, get_messages
from loging import log_result
from ai_analyzer import analyze_conversation

def main():
    #start telethon client
    client.start()
    dialogs = get_dialogs()
    for dialog in dialogs:
        #analyze every dialog
        messages = get_messages(dialog)
        print(messages[0])
        response = analyze_conversation(messages)
        log_result(dialog.id, response)



if __name__ == "__main__":
    main()
