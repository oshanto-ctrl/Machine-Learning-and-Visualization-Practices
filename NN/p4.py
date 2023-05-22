import numpy as np

# random numbers 
np.random.seed(0)

# X is the original input dataset
X = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
]



class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) # random neuron weights depending on num of inputs and num of neurons
        self.biases = np.zeros((1, n_neurons)) # biases as 0 with tuple of shape (1 dim to n_neuron parameters)
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# print(np.random.randn(4, 3))
# input size = 4, neuron = 5 (as we want)
layer1 = Layer_Dense(4, 5)

layer2 = Layer_Dense(5,2) # out of layer1 is input of layer2
#output of layer1 5 (neuron num) is input (n_input of layer2)

layer1.forward(X) # layer.output value
# print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)





"""
# Try 1
inputs = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
]


weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],

]

biases = [2, 3, 0.5]


weights2 = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13]
]

biases2 = [-1, 2, -0.5]



layer1_outputs = np.dot(inputs, np.array(weights).T) + biases

# layer1_output becomes layer2's inputs
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

print(layer1_outputs)
print(layer2_outputs)
"""









