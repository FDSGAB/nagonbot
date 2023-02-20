import pickle
from keras.models import load_model
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

class Model():
    words = None
    classes = None
    model = None

    def __init__(self) -> None:
        self.words = pickle.load(open('./nagonbot/bin/data/model/words.pkl', 'rb'))
        self.classes = pickle.load(open('./nagonbot/bin/data/model/classes.pkl', 'rb'))
        self.model = load_model('./nagonbot/bin/data/model/nagonmodel.h5')