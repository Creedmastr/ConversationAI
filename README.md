# Credits

Credits for the RVC fork goes to Mangio621, and the original project credits can be found on their github. I did not make this part of the code, they did.
The .pth model was made by Sakushi.

# Usage

To use, you'll need to install requirements with `pip install -r requirements.txt`. The **only version** that I know works is 3.9.
I don't know if this install will use the gpu with torch. If not, do these two commands:
- `python -m pip uninstall torch torchvision, torchaudio`
- `python -m pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`