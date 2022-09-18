from functions import *
import random


class selector:

    def __init__(self):
        pass

    def select(tag,koe,i):
        if tag in ["時間" , "日付" , "曜日"]:
                return get_time(tag)
        if tag == "辞書":
            return get_word_dic(koe)
        if tag == "天気":
            koe.voice_answer("少々お待ちください。\n")
            return  get_weather() + "\n" + random.choice(i['responses'])
        if tag == "何歳":
            return age()
        return random.choice(i['responses'])
        

    def __repr__(self) -> str:
        return "Class that returns the most approppriate function or response to the identified label."