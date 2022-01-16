from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.activations import relu


def checking_with_perceptron(video, model):
    if model.predict(video):
        return True
    return False


def creating_model():
    activation = relu(.2)
    model = Sequential(
        layers=[
            Dense(144*3, activation=activation),
            Dropout(.3)
        ]
    )
    return model


def train_model(X, y):
    model = creating_model()
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(X, y, epochs=200, validation_split=.2)
    return model

