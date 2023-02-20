# nagonbot


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
### Keras
### Numpy
### playsound (probably will be out)
### fugashi
### bs4
### gtts
### unidic-lite
### mecab-python3
### selenium
### webdriver_manager

## Project Test package (not working yet)
https://test.pypi.org/project/nagonbot/

## References

Tensor Flow model was inspired from this video by [Neural Nine] (https://www.youtube.com/watch?v=1lwddP0KUEg)
