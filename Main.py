import random
import matplotlib.pyplot as plt
from DataStatistics import File as fsys
from DataStatistics import DataStatistics as s
from Utility import Utility as util
import numpy as np
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":

    (x_dataset, y_dataset) = fsys.File('data.csv').get_csv_data()

    x_stat = s.DataStatistics(x_dataset)
    y_stat = s.DataStatistics(y_dataset)

    # Regression line using sklearn
    data = pd.read_csv('data.csv')  # load data set
    X = data.iloc[:, 1].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = data.iloc[:, 2].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions

    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()

    # plot x data
    x_stat.plot_data("X array")
    y_stat.plot_data("Y array")

    # Empirical Cumulative Distribution Function
    x, y = x_stat.ecdf()
    # Plot the ECDF as dots
    plt.plot(x, y * 100, linestyle='dotted', lw=2)
    plt.show()

    ### ISSUE TO SOLVE
    # Covariance and regression line
    # x_cov = x_stat.covariance(y_stat)
    # b = x_cov / y_stat.variance()
    # a = y_stat.mean() - b * x_stat.mean()

    # plt.scatter(x_dataset, y_dataset)
    # plt.title("Regression line and x, y correlation")
    # util.create_line([0, a], [1, b + a])
    # plt.show()
