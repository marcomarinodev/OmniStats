import numpy as np
import matplotlib.pyplot as plt


class Statistics:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset_size = len(dataset)

    def get_dataset(self):
        return self._dataset

    def mean(self):
        m = 0
        for i in self._dataset:
            m += i
        
        return m / len(self._dataset) 

    def variance(self):
        current_sum = 0
        mean = np.mean(self._dataset)

        for x in self._dataset:
            current_sum += (x - mean) ** 2

        return current_sum / (len(self._dataset) - 1)

    def standard_deviation(self):
        return np.sqrt(self.variance())

    def cdf(self):
        x = np.sort(self._dataset)
        n = x.size
        y = np.arange(1, n + 1) / n
        plt.scatter(x=x, y=y)
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
        plt.title("ECDF")
        plt.show()

    def plot_data(self, name):
        plt.hist(self._dataset)
        plt.title(name + " | Mean: {:.2f}; Standard Deviation: {:.5f}; Variance: {:.5f}".format(
            self.mean(), self.standard_deviation(), self.variance()))
        plt.show()
