import numpy as np
from numpy.linalg import *

# Matplotlib provides MATLAB-like plotting tools in Python
import matplotlib.pyplot as plt

# Our linear regression class
from linreg import LinearRegression

# All the modules needed for 3D surface plots
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# ------------------------------------------------------------------------------------------------
# Plotting tools already written for you.
# Feel free to edit and experiment.

def plotData1D(X, y, to_block=True):
    '''
        This function is to plot y vs X where the number of predictors of X is 1.
        Input
        X - n*1 matrix or vector of length n
        y - n*1 matrix or vector of length n
        to_block - boolean flag which, when set, stops the program execution until the
            plot is closed
    '''
    plt.figure(1)
    plt.clf()
    plt.title("Univariate Data")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.plot(X, y, 'rx', label='Training Data')
    plt.show(block=to_block)

def plotRegLine1D(lr_model, X, y):
    '''
        Plots the y vs X and also the regressed line according to the theta computed.
        Input
        X - n*2 matrix or vector of length n (the second dimension is a column of ones for the bias term)
        y - n*1 matrix or vector of length n
        lr_model - linear regression trained model
    '''
    plotData1D(X[:, 1], y, to_block=False)
    plt.plot(X[:, 1], X @ lr_model.theta, 'b-', label='Regression Line')
    plt.legend(loc='lower right')
    plt.show()

def visualizeObjective(lr_model, t1_vals, t2_vals, X, y):
    '''
        The function does the surface plot of the objective for a
        univariate regression problem with a bias term, so over 2 parameters.
        Search over the space of theta1, theta2.

        It also plots the gradient descent steps as blue points on the surface plot.
        Finally it plots a contour plot of the same

        lr_model - object of class LinReg (already trained)
        t1_vals, t2_vals - values over which the objective function should be plotted
                        List of numbers
        X - n*2 matrix or vector of length n (the second dimension is a column of ones for the bias term)
        y - n*1 matrix or vector of length n
    '''
    T1, T2 = np.meshgrid(t1_vals, t2_vals)
    n, p = T1.shape

    # Compute the objective function over the space
    Z = np.zeros(T1.shape)
    for i in range(n):
        for j in range(p):
            Z[i, j] = lr_model.computeCost(X, y, np.array([T1[i, j], T2[i, j]]).reshape(-1, 1))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(T1, T2, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.plot(lr_model.theta[0], lr_model.theta[1], 'rx')
    plt.title('Surface plot of the cost function')
    plt.xlabel('Theta0')
    plt.ylabel('Theta1')
    plt.show()

    # Contour plot
    plt.figure()
    plt.clf()
    CS = plt.contour(T1, T2, Z)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Contours of cost function')
    plt.xlabel("Theta0")
    plt.ylabel("Theta1")

    plt.plot(lr_model.theta[0], lr_model.theta[1], 'rx')
    plt.show()

# ------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    '''
        Main function to test univariate linear regression
    '''

    # load the data
    filePath = "data/univariateData.dat"
    allData = np.loadtxt(filePath, delimiter=',')

    X = allData[:, :-1]
    y = allData[:, -1].reshape(-1, 1)

    n, d = X.shape

    # Add a column of ones for the bias term
    X = np.c_[np.ones((n, 1)), X]

    # Initialize the model
    init_theta = np.ones((d + 1, 1)) * 10
    n_iter = 1500
    alpha = 0.01

    # Instantiate objects
    lr_model = LinearRegression(init_theta=init_theta, alpha=alpha, n_iter=n_iter)
    plotData1D(X[:, 1], y)
    lr_model.fit(X, y)
    plotRegLine1D(lr_model, X, y)

    # Visualize the objective function convex shape
    theta1_vals = np.linspace(-10, 10, 100)
    theta2_vals = np.linspace(-10, 10, 100)
    visualizeObjective(lr_model, theta1_vals, theta2_vals, X, y)

    # Compute the closed form solution in one line of code
    theta_closed_form = np.linalg.pinv(X.T @ X) @ X.T @ y
    print("theta_closed_form: ", theta_closed_form)
