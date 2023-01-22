import csv
from pathlib import Path

data_folder = Path("./test/")
file_to_open = data_folder / "speech_patterns.csv"

rows = []
fields = []


#csv_file = open(file_name, 'r')

with open(file_to_open, mode = 'r', encoding="utf8") as csv_file:

    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)

    for row in csv_reader:
        rows.append(row)

    print("Total rows number: %d"%(csv_reader.line_num))

print('Field names are:' + ', '.join(field for field in fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')

