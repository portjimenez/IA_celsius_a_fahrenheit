# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sz8XYTLeh3DTQi4yu0C4CxYRmM45C_nz
"""

import tensorflow as tf
import numpy as np

celsius = np.array([-50,50,30,10,-80,90,60,100,-30,0], dtype=float)
fahrenheit = np.array([-58,122,86,50,-112,194,140,212,-22,32], dtype=float)

neuronaCapa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([neuronaCapa])

modelo.compile(
    optimizer= tf.keras.optimizers.Adam(0.3),
    loss='mean_squared_error'
)

print("Entramiento iniciado")
historial = modelo.fit(celsius, fahrenheit, epochs=200)
print("Fin del entrenamiento")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])

centi = 0
print("Prueba realizada")
print("Ingrese los grados centigrados")
dato = input()
centi = float(dato)
resultado = modelo.predict([centi])
print("el resultado es "+str(resultado))