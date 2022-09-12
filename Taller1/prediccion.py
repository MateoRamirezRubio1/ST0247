import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import pandas as pd

def predict(modelData, dfPersonData : pd):
    training_data = np.array([[0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0.33, 1] , [0.13, 0, 0.39, 0], [0.39, 0.6, 0.6060, 0], [0.47, 0.8, 0.666, 0], [0.65, 0, 0.7878, 0], [0, 0, 0.1818, 0], [0.13, 0, 0.39, 0], [0, 0, 0.3030, 0], [0.5, 0.5, 0.5, 1], [0.5, 0, 0.5, 1], [0.695, 0.2, 0.81, 0], [0.85, 0.70, 0.90, 1], [0.173, 0, 0.4545, 0]], "float32")
    target_data = np.array([  [1],          [1],          [0.01],       [1],              [0.9],              [0.37],                 [0.15],                [0.07],               [0.95],            [0.93],             [0.98],            [1],                [1],              [0.05],                [1],                   [0.75]], "float32")

    n_entrada = len(training_data[0])
    n_salida = 1
    n_nodos = 16

    model = Sequential()
    model.add(Dense(n_nodos, input_dim=n_entrada, activation='relu'))  # 4 entradas
    model.add(Dense(n_salida, activation='sigmoid'))  # 1 salida

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])

    model.fit(training_data, target_data, epochs=1000, verbose=False)  # Descripción del entrenamiento

    # Evaluar el modelo
    scores = model.evaluate(training_data, target_data, verbose=False)

    real_data = np.array(modelData, "float32")

    resultado = model.predict(real_data, verbose=False)
    model.summary()

    # Agregar resultados del modelo a una nueva columna del dataframe
    dfPersonData['Probabilidad Graduarse'] = 'null'
    for i in range(len(modelData)):
        dfPersonData.iloc[i, 7] = round(resultado[i][0]*100)

    return dfPersonData
