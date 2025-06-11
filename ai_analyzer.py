import google.generativeai as genai
import config

API = "API"
genai.configure(api_key=API)


model = genai.GenerativeModel("models/gemini-1.5-flash")

def cut_messages(messages, limit=100):
    result = ""
    for i in range(min(limit, len(messages))):
        result += f"{messages[i]['senderID']} - {messages[i]['text']}\n"
    return result


def analyze_conversation(messages):
    dialog_text = cut_messages(messages)
    prompt = f"""
проаналізуй наступну переписку
скажи чи є якісь порушення зі сторони менеджера? грубі відповіді, невиконані обіцянки і тд, проаналізуй роботу менеджера та створи доклад
відповідай стисло як діагностичний звіт:

{dialog_text}
    """
    response = model.generate_content(prompt)
    return response.text