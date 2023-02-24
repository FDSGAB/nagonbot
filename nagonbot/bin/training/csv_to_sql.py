import sqlite3
import csv

connection = sqlite3.connect('nagonbot/bin/data/database.db')

connection_cursor = connection.cursor()

fields = []

with open('nagonbot/bin/data/SpeechPatterns.csv', mode = 'r', encoding = "utf8") as csv_file:

    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)

    try:
        connection_cursor.execute('DROP TABLE speech_patterns;')
        print("OLD TABLE DELETED")
    except:
        pass
    connection_cursor.execute('CREATE TABLE speech_patterns (\
                                entry INT,\
                                json_object TEXT,\
                                tag TEXT NOT NULL,\
                                type TEXT NOT NULL,\
                                value TEXT NOT NULL,\
                                PRIMARY KEY("entry")\
                                );')


    print("Saving", end="")
    for row in csv_reader:
        connection_cursor.execute('INSERT INTO speech_patterns VALUES (?,?,?,?,?);', row)
        print(".", end="")
    print("")

connection_cursor.execute('SELECT * FROM speech_patterns')
records = connection_cursor.fetchall()

for row in records:
    print(row)


connection.commit()
connection_cursor.close()
connection.close()


