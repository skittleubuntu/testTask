import google.generativeai as genai
import config

API = "API"
genai.configure(api_key=API)


model = genai.GenerativeModel("models/gemini-1.5-flash")

def cut_messages(messages, limit=100):
    result = ""
    for i in range(min(limit, len(messages))):
        result += f"date: {messages[i]["date"]} ,{messages[i]['senderID']} - {messages[i]['text']}\n"
    return result


def analyze_conversation(messages):
    dialog_text = cut_messages(messages)
    prompt = f"""
проаналізуй наступну переписку

напиши чи є моменти коли менеджер дав обіцянку виконати щось в день написання, але забув і зробив це на наступний день(тобто не відповів по сенсу до кінця дня. ЦЕ ВАЖЛИВО)
скажи чи є якісь порушення зі сторони менеджера? грубі відповіді, невиконані обіцянки і тд, 
проаналізуй роботу менеджера та створи доклад, оціни роботу менеджра по
його кількостям відповіді за день, швидкість відповіді, ініційовані повідомлення і так далі
відповідай стисло як діагностичний звіт звіт яки буде в форматі 1) чи є порушення в тому що менеджер не відповів протягом дня 
2) його повний аналіз:


{dialog_text}
    """
    response = model.generate_content(prompt)
    return response.text