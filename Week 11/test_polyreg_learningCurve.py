import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from polyreg import PolynomialRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import LeaveOneOut

from polyreg import learningCurve

# ----------------------------------------------------
# Plotting tools

def plotLearningCurve(errorTrain, errorTest, regLambda, degree):
    '''
        plot computed learning curve
    '''
    minX = 3
    maxY = max(errorTest[minX+1:])

    xs = np.arange(len(errorTrain))
    plt.plot(xs, errorTrain, 'r-o')
    plt.plot(xs, errorTest, 'b-o')
    plt.plot(xs, np.ones(len(xs)), 'k--')
    plt.legend(['Training Error', 'Testing Error'], loc='best')
    plt.title(f'Learning Curve (d={degree}, lambda={regLambda})')
    plt.xlabel('Training samples')
    plt.ylabel('Error')
    plt.yscale('log')
    plt.ylim((0, maxY))
    plt.xlim((minX, 10))

# ----------------------------------------------------

def generateLearningCurve(X, y, degree, regLambda, subplot_index):
    '''
        computing learning curve via leave one out CV
    '''

    n = len(X)

    errorTrains = np.zeros((n, n-1))
    errorTests = np.zeros((n, n-1))

    loo = LeaveOneOut()
    itrial = 0
    for train_index, test_index in loo.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        (errTrain, errTest) = learningCurve(X_train, y_train, X_test, y_test, regLambda, degree)

        errorTrains[itrial, :] = errTrain
        errorTests[itrial, :] = errTest
        itrial = itrial + 1

    errorTrain = errorTrains.mean(axis=0)
    errorTest = errorTests.mean(axis=0)

    plt.subplot(2, 3, subplot_index)
    plotLearningCurve(errorTrain, errorTest, regLambda, degree)

# ----------------------------------------------------

if __name__ == "__main__":
    '''
        Main function to test polynomial regression
    '''

    # load the data
    filePath = "data/polydata.dat"
    allData = np.loadtxt(filePath, delimiter=',')

    X = allData[:, 0]
    y = allData[:, 1]

    # generate Learning curves for different params
    plt.figure(figsize=(15, 10))
    generateLearningCurve(X, y, 1, 0, 1)
    generateLearningCurve(X, y, 4, 0, 2)
    generateLearningCurve(X, y, 8, 0, 3)
    generateLearningCurve(X, y, 8, 0.1, 4)
    generateLearningCurve(X, y, 8, 1, 5)
    generateLearningCurve(X, y, 8, 100, 6)

    plt.tight_layout()
    plt.show()
