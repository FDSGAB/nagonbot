import fugashi
import json


class Json_Reader():

    tagger = None
    kokoro = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()
        self.kokoro = json.loads(open("./src/nagonbot/bin/data/kokoro.json", encoding="utf8").read())