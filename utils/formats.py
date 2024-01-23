import re
from unidecode import unidecode

def latinCharRemove(text):
    text = unidecode(text)  # Remove latin characters

    return text

def removeSpace(text):
    if re.search(" ", text) is not None:
            text = text.replace(" ", "")

    return text

def formatText(text):

    
    # To weather
    if re.search("!", text) is not None:
        text = text.replace("! ", "")
        text = text.replace("!", "")

    # To org key
    if re.search("ok-", text) is not None or re.search("Ok-", text) is not None or re.search("OK-", text) is not None:
        
        text = removeSpace(text)
        text = text.replace("ok-", "")
    
    # To weather
    if re.search("wk-", text) is not None or re.search("Wk-", text) is not None or re.search("WK-", text) is not None:
        
        text = removeSpace(text)
        text = text.replace("wk-", "")

    # To chatOpenAi
    if re.search("#", text) is not None:
        text = text.replace(
            "# ", ""
        )  # elimina el signo de exclamación
        text = text.replace("#", "")

    print(text)
    return text