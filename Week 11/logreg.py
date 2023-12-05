import numpy as np
from numpy import linalg as LA


class LogisticRegression:

    def __init__(self, alpha=0.01, regLambda=0.01, epsilon=0.0001, maxNumIters=10000):
        '''
        Constructor
        '''
        self.alpha = alpha
        self.regLambda = regLambda
        self.epsilon = epsilon
        self.maxNumIters = maxNumIters

    def computeCost(self, theta, X, y, regLambda):
        '''
        Computes the objective function
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
            regLambda is the scalar regularization constant
        Returns:
            a scalar value of the cost  ** make certain you're not returning a 1 x 1 matrix! **
        '''
        cost = -y.T @ np.log(self.sigmoid(X @ theta)) - (1 - y).T @ np.log(1 - self.sigmoid(X @ theta)) + 0.5 * regLambda * LA.norm(theta, 2)
        return cost.item(0)

    def computeGradient(self, theta, X, y, regLambda):
        '''
        Computes the gradient of the objective function
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
            regLambda is the scalar regularization constant
        Returns:
            the gradient, an d-dimensional vector
        '''
        n, d = X.shape
        gradient = np.zeros((d, 1))
        gradient[0] = np.sum(self.sigmoid(X @ theta) - y)

        for i in range(1, d):
            gradient[i] = np.sum(X[:, i].T @ (self.sigmoid(X @ theta) - y) + regLambda * theta[i])

        return gradient

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
        '''
        n, d = X.shape
        X = np.c_[np.ones((n, 1)), X]
        n, d = X.shape
        theta = np.zeros((d, 1))

        for i in range(self.maxNumIters):
            oldtheta = theta
            theta = theta - self.alpha * self.computeGradient(theta, X, y, self.regLambda)
            print('Gradient:', self.computeGradient(theta, X, y, self.regLambda))
            print('theta', theta)
            print('Cost:', self.computeCost(theta, X, y, self.regLambda))
            print('Changing:', LA.norm(theta - oldtheta))
            if LA.norm(theta - oldtheta) <= self.epsilon:
                self.theta = theta
                break

        self.theta = theta

    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy matrix
        Returns:
            an n-dimensional numpy vector of the predictions
        '''
        n, d = X.shape
        X = np.c_[np.ones((n, 1)), X]
        Y = np.array(self.sigmoid(X @ self.theta))
        Y[Y > 0.5] = 1
        Y[Y <= 0.5] = 0

        return Y

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
