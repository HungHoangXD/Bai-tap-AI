import numpy as np
import matplotlib.pyplot as plt
from polyreg import PolynomialRegression

if __name__ == "__main__":
    '''
        Main function to test polynomial regression
    '''

    # load the data
    filePath = "data/polydata.dat"
    allData = np.loadtxt(filePath, delimiter=',')

    X = allData[:, 0]
    y = allData[:, 1]

    # regression with degree = d
    d = 8
    model = PolynomialRegression(degree=d, regLambda=0)
    model.fit(X, y)

    # output predictions
    xpoints = np.linspace(np.max(X), np.min(X), 100)
    ypoints = model.predict(xpoints)

    # plot curve
    plt.figure()
    plt.plot(X, y, 'rx', label='Data points')
    plt.plot(xpoints, ypoints, 'b-', label=f'PolyRegression with d = {d}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'PolyRegression with d = {d}')
    plt.legend()
    plt.show()
