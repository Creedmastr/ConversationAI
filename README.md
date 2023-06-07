# Informations

**If you want to reset the conversation, login to character.ai and reset it like a normal character.ai conversation.**

# Credits

Credits for the RVC fork goes to Mangio621, and the original project credits can be found on their github. I did not make this part of the code, they did.
The .pth model was made by Sakushi.

# Usage

First of all, you'll need an character.ai key, which is very to get. Follow these steps: 
1. Log in on character.ai
2. Go to `Network` in your browser's DevTools (F12) and refresh page
3. Search for `/dj-rest-auth/auth0/`
4. Copy the `key` value
5. Create a `api_token.py` file, and just create a variable named `TOKEN`, with the `key` value we previously got attached to it.

To use, you'll need to install requirements with `pip install -r requirements.txt`. The **only version** that I know works is 3.9. You also need to have ffmpeg installed (the full-blown cli tool)
I don't know if this install will use the gpu with torch. If not, do these two commands:
- `python -m pip uninstall torch torchvision, torchaudio`
- `python -m pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`