# nagonbot
Japanese Chatbot.

## Summary
- [Project Description](#project-description)
- [Project Current Status](#project-current-status)
- [Setup](#setup)
- [Required Libraries](#required-libraries)
- [Project Test Package](#project-test-package)
- [References](#references)


## Project Description

nagonbot is a simple chatbot that "speaks" japanese. The name is a reference to a Heian period japanese writer.

## Project Current Status
✅The bot is fully functional, but I'll still make some improvements to make it even better.

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
Please, while the package does not install all the packages automatticallly, install the following libraries (inside a virtual environment).


### Keras
Install:
```
pip install keras
```
github page: https://github.com/keras-team/keras

### Numpy
Install:
```
pip install numpy
```
github page: https://github.com/numpy/numpy

### playsound (probably will be out)
Install (version 1.2.2 certainly works with nagonbot):
```
pip install playsound=1.2.2
```
github page: https://github.com/TaylorSMarks/playsound

### fugashi
Install:
```
pip install fugashi
```
github page: https://github.com/polm/fugashi

### bs4
```
pip install bs4
```
Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### gtts
```
pip install gTTS
```
github page: https://github.com/pndurette/gTTS

### unidic-lite
```
pip install unidic-lite
```
github page: https://github.com/polm/unidic-lite

### mecab-python3
```
pip install mecab-python3
```
github page: https://github.com/SamuraiT/mecab-python3

### selenium
```
pip install selenium
```
github page: https://github.com/SeleniumHQ/selenium

### webdriver_manager
```
pip install webdriver_manager
```
github page: https://github.com/SergeyPirogov/webdriver_manager

## Project Test Package
> __Warning__
Not working yet!!!

Since it's the package is not working, it's tentatives are being uploaded in the test server of PyPi. It has a lot of versions, but none of them work properly:
https://test.pypi.org/project/nagonbot/

## References

Tensor Flow model was inspired from [Neural Nine](https://github.com/NeuralNine)'s [video](https://www.youtube.com/watch?v=1lwddP0KUEg) on how to make a chatbot.
