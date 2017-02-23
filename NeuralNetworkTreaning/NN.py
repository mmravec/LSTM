import numpy
import matplotlib.pyplot as plt
import pandas
import math
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

numpy.random.seed(7)

dataframe = pandas.read_csv(os.path.dirname(__file__))
print(dataframe)