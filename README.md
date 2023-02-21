# nagonbot (1.0.0)
Japanese Chatbot.

## Summary
- [Project Description](#project-description)
- [Project Current Status](#project-current-status)
- [Setup](#setup)
- [Required Libraries](#required-libraries)
- [Project Packages](#project-packages)
- [References](#references)


## Project Description

nagonbot is a simple chatbot that "speaks" japanese. The name is a reference to a Heian period japanese writer.

## Project Current Status
🤖 Version 1.0.0

✅ The bot is fully functional!

✅ You can now install it with PIP! (although some issues regarding the installation have been brought up (┬┬﹏┬┬))

❌ The [required packages](#required-libraries) do not install automatically with the bot's installation (needs to be done manually).

❌ Some functions like BGM are not available in the release.

🛠 I'm always working on the bot to make it even better (adding functions, bettering the model, updating the package)

## Setup
I recommend using a vitual environment (venv) for this project, since it's libraries are not fully optimized.
Steps:

1. Create a virtual environment in a test folder.
```
py -m venv ./myvenv
```

2. Activate the virtual environment.
```
.\myvenv\Scripts\activate
```

3. Install the bot inside the virtual environment as a package for simpler usage (the package is not functional yet).
```
pip install nagonbot
```

4. Run the program inside the virtual enviroment.
```python
from nagonbot.bot import Main

Main()
```

5. Exit the virtual environment when done.
```
deactivate
```

## Required Libraries
> __Note__
Please, while the package does not install all the packages automattically, install the following libraries (inside a virtual environment).

For more information on the libraries, please refer to the [Required Libraries Wiki Page](https://github.com/FDSGAB/nagonbot/wiki/Required-Libraries)

Install:
```
pip install tensorflow
pip install pygame
pip install keras
pip install numpy
pip install playsound==1.2.2
pip install fugashi
pip install beautifulsoup4
pip install gTTS
pip install unidic-lite
pip install mecab-python3
pip install selenium
pip install webdriver_manager
```


## Project Packages

### Official Packages
You can find this project's official packages [here](https://pypi.org/project/nagonbot/1.0.0/) on the PyPi site.


### Test Packages
For information about test packages, please refer to the [Project Test Packages Wiki Page](https://github.com/FDSGAB/nagonbot/wiki/Project-Test-Packages#project-test-packages).

## References

Tensor Flow model was inspired from [Neural Nine](https://github.com/NeuralNine)'s [video](https://www.youtube.com/watch?v=1lwddP0KUEg) on how to make a chatbot.
