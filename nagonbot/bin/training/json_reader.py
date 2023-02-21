import fugashi
import json
from importlib import resources


class Json_Reader():

    tagger = None
    kokoro = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()
        self.kokoro = json.load(resources.open_text('nagonbot.bin.data', 'kokoro.json', encoding="utf-8"))
        #self.kokoro = json.load(file)

        #ORIGINAL
        #self.kokoro = json.loads(open("nagonbot/bin/data/kokoro.json", encoding="utf8").read())

if __name__ == '__main__':
    file = Json_Reader()
    print(file.kokoro)