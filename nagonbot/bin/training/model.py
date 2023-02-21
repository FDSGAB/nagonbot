import pickle
from keras.models import load_model
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from importlib import resources

class Model():
    words = None
    classes = None
    model = None

    def __init__(self) -> None:
        """ words_pickle = resources.open_binary('nagonbot.bin.data.model', 'words.pkl').read()
        self.words = pickle.load(open(file = words_pickle, mode ='rb'))
        classes_pickle = resources.open_binary('nagonbot.bin.data.model', 'classes.pkl').read()
        self.classes = pickle.load(open(classes_pickle, 'rb'))
        model_file = resources.open_binary('nagonbot.bin.data.model', 'nagonmodel.h5').read()
        self.model = load_model(model_file) """

        #ORIGINAL
        self.words = pickle.load(open('./nagonbot/bin/data/model/words.pkl', 'rb'))
        self.classes = pickle.load(open('./nagonbot/bin/data/model/classes.pkl', 'rb'))
        self.model = load_model('./nagonbot/bin/data/model/nagonmodel.h5')