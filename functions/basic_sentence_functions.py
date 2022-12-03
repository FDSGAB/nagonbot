import numpy 
from functions import *


class Sentence():

    def clean_up_sentece(self, tagger,sentence):
        sentence_words = [word.surface for word in tagger(sentence)]
        return sentence_words

    def bag_of_words(self, sentence, words, tagger):
        sentence_words = self.clean_up_sentece(tagger, sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return numpy.array(bag)


    #Função que tenta acertar a classe da mensagem enviada
    def predict_class(self, sentence, model, classes, tagger, words):
        bow = self.bag_of_words(sentence, words,tagger)
        res = model.predict(numpy.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i, r in enumerate(res) if r > 0.1]      

        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'koko': classes[r[0]], 'probability': str(r[1])})
        return return_list

    #Com base na classe da mensagem prevista, essa função retorna uma resposta adequada
    def get_response(self,koe,kokoro_list, kokoro_json):
        tag = kokoro_list[0]['koko']               
        list_of_kokoro = kokoro_json['kokoro']
        for i in list_of_kokoro:
            if i['tag'] == tag:
                return selector.select(tag,koe,i)