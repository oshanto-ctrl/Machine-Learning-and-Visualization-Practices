inputs = [1.2, 5.1, 2.1] # 3 neurons of input (unique) 
weights = [3.1, 2.1, 8.7] # 3 weights for 3 inputs
bias = 3 # every qunique neuron has unique bias

output = inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias
print(output)