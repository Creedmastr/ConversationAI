from api_token import TOKEN
from characterai import pyCAI
import os

def get_answer(id, text): 
    client = pyCAI(TOKEN)

    print("INFO: Asking character")

    data = client.chat.send_message(id, text, wait=True)

    return data

def answer_formating(answer):
    return f"{answer['src_char']['participant']['name']}: {answer['replies'][0]['text']}"