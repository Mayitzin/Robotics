# -*- coding: utf-8 -*-
"""
Example of Linear Regression using Theano as explained by Alec Radford of indico

@author: Alec Radford
"""

# Namespaces
import theano
from theano import tensor as T
import numpy as np
# Module to plot
import matplotlib.pyplot as plt

# Training Data generation
theta = 2.0
variance = 0.33
trX = np.linspace(-1, 1, 101)
trY = theta*trX + np.random.randn(*trX.shape)*variance

# Symbolic variable initialization
X = T.scalar()
Y = T.scalar()

# Model
def model(X, w):
    return X * w

# Model Parameter initialization
w = theano.shared(np.asarray(0., dtype=theano.config.floatX))
y = model(X, w)

# Metric to be optimized by model
cost = T.mean(T.sqr(y - Y))
# Learning signal for parameter(s)
gradient = T.grad(cost=cost, wrt=w)
# Step size to change parameters
updates = [[w, w - gradient * 0.01]]

# Compile to a Python function
train = theano.function(inputs=[X, Y], outputs=cost, updates=updates, allow_input_downcast=True)

# Iterate through data 100 times and train model
weights = []
errors = []
for i in range(100):
    for x, y in zip(trX, trY):
        train(x, y)
    weights.append(w.get_value())
    errors.append((w.get_value()-theta)**2)
        
w1 = w.get_value()
print w1 #something around 2

# Create a line
line = trX*w1

# Plotting results
plt.subplot(2,1,1)
plt.plot(trX, theta*trX, 'k--', trX, trY, 'b.', trX, line, 'r-')
plt.title('Sampled data')
# Plot Errors in Logarithmic graph
plt.subplot(2,1,2)
plt.semilogy(range(100), errors, 'r-')
plt.xlabel('Iterations')
plt.ylabel('Squared Error')
plt.grid(True)
# Render the Plot Figures
plt.show()