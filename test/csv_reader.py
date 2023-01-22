import csv
import json
from pathlib import Path

data_folder = Path("./test/")
file_to_open = data_folder / "speech_patterns.csv"

rows = []
fields = []

with open(file_to_open, mode = 'r', encoding = "utf8") as csv_file:

    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)

    for row in csv_reader:
        rows.append(row)

tag_list = []

for row in rows:
    tag_list.append(row[2])

unique_tags = set(tag_list)


list_for_json = []

for subject in unique_tags:
    pattern_list = []
    response_list = []
    for row in rows:
        if row[2] == subject:
            if row[3] == 'pattern':
                pattern_list.append(row[4])
            if row[3] == 'response':
                response_list.append(row[4])
    json_entry = {"tag": subject, "patterns" : pattern_list, "responses" :response_list}
    list_for_json.append(json_entry)

json_dict = {"kokoro" : list_for_json}

with open("kokoro_test.json", mode = "w", encoding = "utf8") as outfile:
    json.dump(json_dict, outfile, ensure_ascii=False, indent=2)

print(json_dict)

