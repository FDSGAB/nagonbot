import pickle
import numpy 
import random
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from nagonbot.bin.training.json_reader import Json_Reader

class ModelTraining():

    outside_run = False

    def __init__(self) -> None:
        

        json_file = Json_Reader()

        words = []
        classes = []
        documents = []
        ignore_letters = ['。', '、', '！', '？', '「', '」','～']



        for koko in json_file.kokoro['kokoro']:                   
            for pattern in koko['patterns']:
                word_list = [word.surface for word in json_file.tagger(pattern)]
                words.extend(word_list)
                documents.append((word_list, koko['tag']))
                if koko['tag'] not in classes:
                    classes.append(koko['tag'])

        #print("\n\n DOCUMENTS:\n",documents)

        classes = sorted(set(classes))

        words = [word for word in words if word not in ignore_letters]
        words = sorted(set(words))

        #print("\n\n Words:\n",words)
        try:
            pickle.dump(words, open('nagonbot/bin/data/model/words.pkl', 'wb'))
            pickle.dump(classes, open('nagonbot/bin/data/model/classes.pkl', 'wb'))
        except:
            pickle.dump(words, open('words.pkl', 'wb'))
            pickle.dump(classes, open('classes.pkl', 'wb'))
            self.outside_run = True


        #print("\n\n Classes:\n",classes)

        training = []
        output_empty = [0] * len(classes)

        for document in documents:
            bag = []
            word_patterns = document[0]
            for word in words:
                bag.append(1) if word in word_patterns else bag.append(0)
            

            output_row = list(output_empty)
            output_row[classes.index(document[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = numpy.array(training)

        train_x = list(training[:, 0])
        train_y = list(training[:, 1])

        model = Sequential()
        model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation = 'relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]), activation='softmax'))


        #sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        sgd = SGD(lr=0.01, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

        hist = model.fit(numpy.array(train_x), numpy.array(train_y), epochs=200, batch_size = 5, verbose = 1)
        if not self.outside_run:
            model.save('nagonbot/bin/data/model/nagonmodel.h5', hist)
        else:
            model.save('nagonmodel.h5', hist)
        print("出来ました！")