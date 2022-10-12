"""
Example for pickle
"""
import pickle


class Model:

    def __init__(self, text):
        self.text = text

    def predict(self):
        print(self.text)


# save the model
m = Model("this is a random forest")
pickle.dump(m, open('model.pkl', 'wb'))

# load the model
new_model = pickle.load(open('model.pkl', 'rb'))
new_model.predict()

