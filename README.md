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

### Mehod #1 - dowloading the source code (✅ Works!!)
#### Steps:
1. Click the "<> Code" green button on [nagonbot's GitHub repository](https://github.com/FDSGAB/nagonbot).
2. Click the "Download ZIP" option.
3. Extract the project's code to a location of your liking.
4. Open the extracted project folder in an IDE of your liking.
5. Create a virtual environment inside the project folder.
```
py -m venv ./myvenv
```
6. Activate the virtual environment created in the last step.
```
.\myvenv\Scripts\activate
```
7. Install the [necessary libraries](#required-libraries).
```
python -m pip install -r requirements.txt
```
8. Run the test_nagonbot.py file
9. Exit the virtual environment when done.
```
deactivate
```



### Method #2 - pip install (❌ Still doesn't work)
#### Steps:

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
> __Note__\
Please, while the package does not install all the packages automattically, install the following libraries (inside a virtual environment).

For more information on the libraries, please refer to the [Required Libraries Wiki Page](https://github.com/FDSGAB/nagonbot/wiki/Required-Libraries)

### Install:

```
python -m pip install -r requirements.txt
```
or

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

### Uninstalling all pip libraries from your virtual environment:
> __Warning__\
***DO NOT RUN THESE COMMANDS IF YOU'RE NOT IN A VIRTUAL ENVIRONMENT OR ELSE, IT WILL DELETE ALL THE LIBRARIES YOU'VE PIP INSTALLED IN YOUR BASE PYTHON!!!***

Creates a .txt file with all current libraries installed with pip
```bash
pip freeze > pip_libs.txt
```

Deletes all the libraries listed inside the pip_libs.txt previously created asking wheter or not to delete each library
```bash
pip uninstall -r pip_libs.txt
```

Deletes all the libraries at once listed inside the pip_libs.txt previously created without asking what to do with each library
```bash
pip uninstall -r pip_libs.txt -y
```


## Project Packages

### Official Packages
You can find this project's official packages [here](https://pypi.org/project/nagonbot/1.0.0/) on the PyPi site.


### Test Packages
For information about test packages, please refer to the [Project Test Packages Wiki Page](https://github.com/FDSGAB/nagonbot/wiki/Project-Test-Packages#project-test-packages).

## References

Tensor Flow model was inspired from [Neural Nine](https://github.com/NeuralNine)'s [video](https://www.youtube.com/watch?v=1lwddP0KUEg) on how to make a chatbot.
