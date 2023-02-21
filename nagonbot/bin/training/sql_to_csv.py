import sqlite3

class CsvCreator():
    
    first_line = True

    def __init__(self) -> None:
        connection = sqlite3.connect('nagonbot/bin/data/database.db')
        connection_cursor = connection.cursor()
        connection_cursor.execute('SELECT * FROM speech_patterns')
        records = connection_cursor.fetchall()
        connection_cursor.close()
        connection.close()


        csv_file = open('nagonbot/bin/data/SpeechPatterns.csv', "w", encoding='utf-8')
        for line in records:
            if self.first_line:
                self.first_line = False
            else:
                csv_file.write("\n")
            line = str(line[0]), line[1], line[2], line[3]
            line = ",".join(line)
            csv_file.write(line)
        csv_file.close
        
        



if __name__ == '__main__':
    CsvCreator()