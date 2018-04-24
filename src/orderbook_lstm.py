from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM

class OrderBookLSTM:
    '''
    Inputs:
        - timesteps: number of time sequence inputs
        - layer_neurons: number of neurons in each LSTM layer
        - input_shape: shape of input
        - output_shape: shape of output (e.g. num classes)
        - num_hidden_layers: number of 'vertical' hidden LSTM layers
        - dropout: dropout rate
    '''
    def __init__(self, timesteps, layer_neurons, input_shape, output_shape, num_hidden_layers, dropout = None):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.timesteps = timesteps
        self.layer_neurons = layer_neurons
        self.dropout = dropout
        self.num_hidden_layers = num_hidden_layers
        self.model = self.createLSTM()

    def createLSTM(self):
        print('Building model...')
        model = Sequential()
        model.add(LSTM(self.layer_neurons, input_shape=self.input_shape, return_sequences=True))
        for i in range(self.num_hidden_layers):
            if i == self.num_hidden_layers-1:
                model.add(LSTM(self.layer_neurons, return_sequences=False))
            else:
                model.add(LSTM(self.layer_neurons, return_sequences=True))

        if self.dropout is not None:
            model.add(Dropout(self.dropout))

        model.add(Dense(self.output_shape, activation='softmax'))

        print('Compiling model...')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])

        return model

    def get_model(self):
        return self.model
