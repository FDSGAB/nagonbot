import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

class Model():
    words = None
    classes = None
    model = None

    def __init__(self) -> None:
        self.words = pickle.load(open('./src/nagonbot/bin/data/model/words.pkl', 'rb'))
        self.classes = pickle.load(open('./src/nagonbot/bin/data/model/classes.pkl', 'rb'))
        self.model = load_model('./src/nagonbot/bin/data/model/nagonmodel.h5')