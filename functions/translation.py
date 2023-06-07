from deep_translator import GoogleTranslator

def translate(text, src, dest):
    print("INFO: Translating")
    translated_text = GoogleTranslator(source=src, target=dest).translate(text)
    return translated_text
