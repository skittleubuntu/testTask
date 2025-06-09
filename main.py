from tg_client import client, get_dialogs, get_messages

def main():
    #start telethon client
    client.start()
    dialogs = get_dialogs()
    for dialog in dialogs:
        #analyze every dialog
        messages = get_messages(dialog)
        print(messages)

if __name__ == "__main__":
    main()
