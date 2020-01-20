# -*- coding: utf-8 -*-
"""
Linear regression example using gradient descent. The purpose of this
script is to give an idea of how nested functions can be used.

-- Sean Morrison, 2018
"""

# we'll use numpy here since it makes sense to do so. Also a good time to
# introduce it, since we'll be using it for the quadrotor simulation.
import numpy as np
import matplotlib.pyplot as plt

# We have a bunch of datapoints y_hat that follows a linear pattern.
# we want to find a set of theta values Y=theta_0*X+theta_1 that match the
# line Y=A*X+B that generated the data.
def optimize_f(theta, x, y_targ):
    # outer optimization function
    
    def cost(pred, targ):
        # mean squared-error cost function
        loss = -0.5*(pred-targ)**2
        grad = targ-pred
        return np.mean(loss), grad
    
    # We can either optimize for a fixed number of iterations and take the 
    # result, or optimize until the gradient goes to zero (local minima). 
    # We do the latter here since it makes more sense. Since we don't know
    # how long the optimization process will take, we use a while loop.
    iteration = 1
    while True:
        y_pred = theta.dot(x_act)
        loss, grad = cost(y_pred, y_targ)
        print("--- Iteration: {}, Loss: {:.5f} ---".format(iteration, loss))
        theta += alpha*x_act.dot(grad)
        if np.mean(grad) < thresh:
            break
        iteration += 1
        
thresh = 1e-10                                      # termination threshold
alpha = 1e-3                                        # learning rate
x = np.linspace(-1, 1, 100)                         # x range
x_act = np.vstack([x, np.ones(x.shape)])            # add 1s vector for Y=THETA*X
A = np.random.randn()*10                            # generate random slope
B = np.random.randn()*10                            # generate random intercept
y = A*x+B+0.8*np.random.randn(100)                  # add noise to the function
theta = np.random.randn(2)                          # generate two random THETA vals
theta_start = theta.copy()                          # save initial THETA vals
optimize_f(theta, x, y)                             # call optimization fn
print("A: {}".format(A))
print("B: {}".format(B))
print("Theta init: {}".format(theta_start))
print("Optimized Theta: {}".format(theta))
fig = plt.figure()                                  # create a figure
plt.scatter(x,y)                                    # scatter plot of data
plt.plot(x, theta.dot(x_act), "-r")                 # plot the line given by THETA
fig.show()                                          # show plot