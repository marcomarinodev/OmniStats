import numpy as np
import dc_stat_think as dcst

class Statistica:
    def __init__(self, dataset):
        self._dataset = dataset

    def get_dataset(self):
        return self._dataset

    def mean(self):
        return np.mean(self._dataset)

    def variance(self):
        sum = 0
        mean = np.mean(self._dataset)

        for x in self._dataset:
            sum += (x - mean) ** 2

        return sum / len(self._dataset) - 1

    def standard_deviation(self):
        return np.sqrt(self.variance())

    def ecdf(self):
        return dcst.ecdf(self._dataset)
