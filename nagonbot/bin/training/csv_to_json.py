import json
from importlib import resources

class KokoroUpdaterC():

    def __init__(self) -> None:
        csv_file = resources.open_text('nagonbot.bin.data', "SpeechPatterns.csv", encoding='utf-8').read()
        lines = csv_file.split("\n")
        records = list()
        for line in lines:
            line = line.split(',')
            line[0] = int(line[0])
            records.append(line)

        tag_list = []

        for row in records:
            tag_list.append(row[1])

        unique_tags = set(tag_list)

        list_for_json = []

        for subject in unique_tags:
            pattern_list = []
            response_list = []
            for row in records:
                if row[1] == subject:
                    if row[2] == 'pattern':
                        pattern_list.append(row[3])
                    if row[2] == 'response':
                        response_list.append(row[3])
            json_entry = {"tag": subject, "patterns" : pattern_list, "responses" :response_list}
            list_for_json.append(json_entry)

        json_dict = {"kokoro" : list_for_json}

        try:
            with open("nagonbot/bin/data/kokoro.json", mode = "w", encoding = "utf8") as outfile:
                json.dump(json_dict, outfile, ensure_ascii=False, indent=2)
        except:
            with open("kokoro.json", mode = "w", encoding = "utf8") as outfile:
                json.dump(json_dict, outfile, ensure_ascii=False, indent=2)

        print("心が更新いたしました！！")


if __name__ == '__main__':
    KokoroUpdaterC()