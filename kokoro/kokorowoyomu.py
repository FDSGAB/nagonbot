import fugashi
import json
from pathlib import Path


class Json_Reader():

    tagger = None
    kokoro = None

    def __init__(self) -> None:
        data_folder = Path("D:/REP_programas_Python/nagonbot/kokoro/")
        file_to_open = data_folder / "kokoro.json"
        self.tagger = fugashi.Tagger()
        self.kokoro = json.loads(open(file_to_open, encoding="utf8").read()) 