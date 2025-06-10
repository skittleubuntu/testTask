from tg_client import client, get_dialogs, get_messages
from loging import log_result

def main():
    #start telethon client
    client.start()
    dialogs = get_dialogs()
    for dialog in dialogs:
        #analyze every dialog
        messages = get_messages(dialog)
        #TODO AI analyze
        response = "AI ANALYZE"
        log_result(dialog.id, response )

        print(messages)

if __name__ == "__main__":
    main()
