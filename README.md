# Informations

**If you want to reset the conversation, login to character.ai and reset it like a normal character.ai conversation.**

# Credits

Credits for the RVC fork goes to Mangio621, and the original project credits can be found on their github. I did not make this part of the code, they did.
The .pth model was made by Sakushi.

# Usage

The first thing to do, is to download just the 'installer.ps1' that is at the root of this github, and after that run it. The only python version **I know** works for this entire project is **3.9.8**. It will download all the necessary files from this repo and my other RVC fork repo.

After that, you'll need an character.ai key, which is very easy to get. Follow these steps: 
1. Log in on character.ai
2. Go to `Network` in your browser's DevTools (F12) and refresh page
3. Search for `/dj-rest-auth/auth0/`
4. Copy the `key` value
5. Create a `api_token.py` file, and just create a variable named `TOKEN`, with the `key` value we previously got attached to it.

## Requirements

The basic requirements are already installed by the powershell script. You also need to have ffmpeg installed (the full-blown cli tool), that can be found on the internet manually, or can be downloaded trough Chocolatey.
I don't know if this install will use the cuda gpus with torch. If not, do these two commands:
- `python -m pip uninstall torch torchvision, torchaudio`
- `python -m pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`
