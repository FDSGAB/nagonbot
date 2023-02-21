"""



-----------------------Arquivo de treinamento----------------------------

    Esse arquivo é responsável por treinar o modelo do chat-bot. Primeiramente,
abre-se um arquivo JSON com os padrões de pergunta e resposta do bot em japonês.
Em seguida, eles são lidos e armazenados em listas e salvos em .pkl..........



"""




#Bibliotecas para manipulação de arquivos
#from src.nagonbot.bin.database import sql_to_json
import json
import pickle

#Bibliotecas matemáticas
import numpy 
import random

#Biblioteca para separar palavras de frases em japonês
import fugashi

#Bibliotecas de Machine Learning / Deep Learning
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from nagonbot.bin.training.json_reader import Json_Reader




"""

----------------------Coleta dos padrões de pergunta e resposta do arquivo JSON-------------------------------


"""

class ModelTraining():

    outside_run = False

    def __init__(self) -> None:
        

        json_file = Json_Reader()

        #Cria as listas de controle 
        words = []                                               #Palavras que serão utilizadas
        classes = []                                             #Classes que serão utilizadas
        documents = []                                           #Combinações 'pertences'
        ignore_letters = ['。', '、', '！', '？', '「', '」','～']     #Caracteres que serão ignorados



        for koko in json_file.kokoro['kokoro']:                   
            for pattern in koko['patterns']:
                word_list = [word.surface for word in json_file.tagger(pattern)]
                words.extend(word_list)
                documents.append((word_list, koko['tag']))
                if koko['tag'] not in classes:
                    classes.append(koko['tag'])

        #print("\n\n DOCUMENTS:\n",documents) só printa o documento de lista de palavras




        """


        --------------------Salva as palavras e classes dentro de um .pkl---------------------


        """

        classes = sorted(set(classes))                                      #remove entradas duplicadas

        words = [word for word in words if word not in ignore_letters]      #retira os caracteres ignorados
        words = sorted(set(words))                                          #remove entradas duplicadas

        #print("\n\n Words:\n",words)
        try:
            pickle.dump(words, open('nagonbot/bin/data/model/words.pkl', 'wb'))
            pickle.dump(classes, open('nagonbot/bin/data/model/classes.pkl', 'wb'))
        except:
            pickle.dump(words, open('words.pkl', 'wb'))
            pickle.dump(classes, open('classes.pkl', 'wb'))
            self.outside_run = True


        #print("\n\n Classes:\n",classes)

        """


        -------------------TREINAMENTO (PARTE DE DEEP LEARNING)----------------------------


        """

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



        """


        ------------------------Construindo o módulo da rede neural (NEURAL NETWORK THEORY)--------------------------


        """

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