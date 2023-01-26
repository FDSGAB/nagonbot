from pathlib import Path

class FileChecker():

    json_file = Path('./kokoro/kokoro.json')
    database = Path('./database/database.db')
    training_program = Path('./training/training.py')
    main_program = Path('main.py')
    model = Path('./model/nagonmodel.h5')
    words_pickle = Path('./model/words.pkl')
    classes_pickle = Path('./model/classes.pkl')

    def check_json(self) -> bool:
        return self.json_file.is_file()

    def check_database(self) -> bool:
        return self.database.is_file()

    def check_training(self) -> bool:
        return self.training_program.is_file()

    def check_main(self) -> bool:
        return self.main_program.is_file()
    
    def check_model(self) -> bool:
        return self.model.is_file()
    
    def check_words_pickle(self) -> bool:
        return self.words_pickle.is_file()

    def check_classes_pickle(self) -> bool:
        return self.classes_pickle.is_file()

if __name__ == "__main__":
    print('')
    checker = FileChecker()
    check_list = [int(checker.check_json()), int(checker.check_database()), int(checker.check_training()), int(checker.check_main()), int(checker.check_model()), int(checker.check_words_pickle()), int(checker.check_classes_pickle())]
    print('Json file: ', 'Exists' if checker.check_json() else 'Not found!!!')
    print('Database file: ', 'Exists' if checker.check_database() else 'Not found!!!')
    print('Training file: ', 'Exists' if checker.check_training() else 'Not found!!!')
    print('Main file: ', 'Exists' if checker.check_main() else 'Not found!!!')
    print('Model file: ', 'Exists' if checker.check_model() else 'Not found!!!')
    print('Words.pkl file: ', 'Exists' if checker.check_words_pickle() else 'Not found!!!')
    print('Classes.pkl file: ', 'Exists' if checker.check_classes_pickle() else 'Not found!!!')