import re
def process(text):
    final_text = re.sub("[^a-zA-Z]",' ',text)
    final_text = final_text.lower()
    return final_text