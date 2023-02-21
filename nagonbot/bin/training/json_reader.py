import fugashi
import json
from importlib import resources


class Json_Reader():

    tagger = None
    kokoro = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()
        try:
            self.kokoro = json.loads(open("nagonbot/bin/data/kokoro.json", encoding="utf8").read())
        except:
            self.kokoro = json.loads(open("kokoro.json", encoding="utf8").read())
        #self.kokoro = json.load(file)

        #IMPORT LIB
        #self.kokoro = json.load(resources.open_text('nagonbot.bin.data', 'kokoro.json', encoding="utf-8"))

            
        #ORIGINAL
        #self.kokoro = json.loads(open("nagonbot/bin/data/kokoro.json", encoding="utf8").read())

if __name__ == '__main__':
    file = Json_Reader()
    print(file.kokoro)