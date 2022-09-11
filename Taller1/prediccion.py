import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

def predict(modelData, personData):
    training_data = np.array([[0, 0, 11/33, 1], [1, 1, 1, 0], [1, 0, 1, 0], [0.5, 0, 0.5, 1] ,[0.5, 0, 0.5, 0], [0, 0, 3/33, 0], [15/23, 1, 26/33, 1], [4/23, 0, 15/33, 0]], "float32")
    target_data = np.array([  [1],              [0],          [0],          [1],              [0.95],           [0.85],          [1],                  [0.9]], "float32")

    n_entrada = len(training_data[0])
    n_salida = 1
    n_nodos = 16

    model = Sequential()
    model.add(Dense(n_nodos, input_dim=n_entrada, activation='relu'))  # entradad (2)
    model.add(Dense(n_salida, activation='sigmoid'))  # salida (1)

    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['binary_accuracy'])

    model.fit(training_data, target_data, epochs=1000, verbose=False)  # descripción del entrenamiento

    # ========================================
    # evaluamos el modelo
    scores = model.evaluate(training_data, target_data, verbose=False)

    print(f'Metrica del modelo: {model.metrics_names[1]}, con un valor de: {scores[1] * 100}')

    real_data = np.array(modelData, "float32")

    resultado = model.predict(real_data, verbose=0)
    model.summary()

    for i in range(len(modelData)):
        print(f' para la entrada: {real_data[i]} -> {resultado[i]}')
