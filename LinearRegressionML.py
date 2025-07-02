import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes as ax
from matplotlib.animation import FuncAnimation

url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240320114716/data_for_lr.csv'
data = pd.read_csv(url)
data

data = data.dropna()

train_input = np.array(data.x[0:500]).reshape(500,1)
train_output = np.array(data.y[0:500]).reshape(500,1)

test_input = np.array(data.x[500:700]).reshape(199,1)
test_output = np.array(data.y[500:700]).reshape(199,1)

#Building Linear Regression Model

class LinearRegression:
    def __init__(self):
        self.parameters = {}

    #Forward Propagation
    def forward_propagation(self, train_input):
        m = self.parameters{'m'}
        c = self.parameters{'c'}
        predictions = np.multiply(m, train_input) + c
        return predictions
    
    def cost_function(self, train_output, predictions):
        cost = np.mean((train_output - predictions) ** 2)
        return cost
    
    #Backpropagation
    def back_propagation(self, train_input, train_output, predictions):
        derivates = {}
        df = 
        dm = 2 * np.mean(predictions) + train_input

    