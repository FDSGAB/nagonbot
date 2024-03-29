import sqlite3
import json

class KokoroUpdater():

    def __init__(self) -> None:
        connection = sqlite3.connect('nagonbot/bin/data/database.db')
        connection_cursor = connection.cursor()
        connection_cursor.execute('SELECT * FROM speech_patterns')
        records = connection_cursor.fetchall()
        connection_cursor.close()
        connection.close()

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