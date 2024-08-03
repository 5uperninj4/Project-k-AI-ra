import re
def parse(text):
    #text = re.sub(r"\n", " ", text)
    text = re.sub(r" â€™ ", "'", text)
    text = re.sub(r'[A-Z]', lambda match: match.group().lower(), text)
    return text

with open ('C:/Users/logan/Documents/Coding/Python/KAIra/3.0/Main/dialogues_text.txt', 'r', errors='ignore') as f:
    text = f.read()
    text = parse(text)
    with open ('C:/Users/logan/Documents/Coding/Python/KAIra/3.0/Main/dialogues.txt', 'w', errors='ignore') as f:
        f.write(text)