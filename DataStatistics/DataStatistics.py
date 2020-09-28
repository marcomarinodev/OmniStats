import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

class DataStatistics:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset_length = len(dataset)

    def get_dataset(self):
        return self._dataset

    def mean(self):
        return np.mean(self._dataset)

    def covariance(self, other_dataset):
        sum = 0
        y_data = other_dataset.get_dataset()

        x_mean = np.mean(self._dataset)
        y_mean = np.mean(y_data)

        if self._dataset_length == len(y_data):
            for i in range(0, self._dataset_length):
                sum += (self._dataset[i] - x_mean) * (y_data[i] - y_mean)
            sum /= (self._dataset_length - 1)
        return sum

    def variance(self):
        sum = 0
        mean = np.mean(self._dataset)

        for x in self._dataset:
            sum += (x - mean) ** 2

        return sum / (len(self._dataset) - 1)

    def standard_deviation(self):
        return np.sqrt(self.variance())

    def ecdf(self):
        return dcst.ecdf(self._dataset)

    def plot_data(self, name):
        plt.hist(self._dataset)
        plt.title(name + " | Mean: {:.2f}; Standard Deviation: {:.5f}; Variance: {:.5f}".format(
            self.mean(), self.standard_deviation(), self.variance()))
        plt.show()
