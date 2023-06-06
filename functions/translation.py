from googletrans import Translator

def translate(text, src, dest):
    print("INFO: Translating")
    translator = Translator()

    # Translate the text from English to Japanese
    translated_text = translator.translate(text, src=src, dest=dest).text

    return translated_text
