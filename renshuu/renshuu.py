import os
import random
import json
import pickle
import numpy 

import nltk 
from nltk.corpus import knbc                #Japanese language import
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from pathlib import Path

#Aqui eu utilizei essas funções path para pegar o endereço do JSON poder usar na open()
data_folder = Path("D:/REP_programas_Python/NagonBot.py/kokoro JSON/")
file_to_open = data_folder / "kokoro.json"


#Abre o arquivo JSON, o enconding="utf8" é necessário por conta dos caracteres japoneses
kokoro = json.loads(open(file_to_open, encoding="utf8").read()) #Recebe o arquivo em JSON como, essencialmente, um dicionário em Python


#Cria as listas de controle 
words = []              #Palavras que serão utilizadas, PROBLEMA: SOMENTE AS LETRAS SAO COLETADAS
classes = []            #Classes que serão utilizadas
documents = []          #Combinações 'pertences'
ignore_letters = ['。', '、', '！', '？', '「', '」']   #Caracteres que serão ignorados



for koko in kokoro['kokoro']:                   
    for pattern in koko['patterns']:
        #word_list = nltk.word_tokenize(pattern, language='japanese')    #ERRO AQUIII
        #word_list = knbc.words(pattern)                                 #tokenize e knbc n funcionam, procurar mais sobre depois :/
        word_list = pattern
        words.extend(word_list)                                          #Troucou .append() por .extend()  (necessário?)
        documents.append((word_list, koko['tag']))
        if koko['tag'] not in classes:
            classes.append(koko['tag'])

#print(documents)                    #Fim da primeira parte!!!

classes = sorted(set(classes))        #remove entradas duplicadas

words = sorted(set(words))           #Não sei se vale a pena no caso comentei por enquanto, SÒ SAO AS LETRAS N FUNCIONA

#print(words)

pickle.dump(documents, open('documents.pkl', 'wb'))
pickle.dump(documents, open('classes.pkl', 'wb'))


#PARTE DE DEEP LEARNING

training = []
output_empty = [0] * len(classes)

#AD LIB como o words não funciona no momento, estou tentando substituir com o documents e ver se uso as frases
for document in documents:
    bag = []
    sentence_patterns = document[0]
    bag.append(1) if document[0] in sentence_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = numpy.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])


"""
Construindo o módulo da rede neural (NEURAL NETWORK THEORY):
"""

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(numpy.array(train_x), numpy.array(train_y), epochs=200, batch_size = 5, verbose = 1)
model.save('nagon_model.model')
print("Done")