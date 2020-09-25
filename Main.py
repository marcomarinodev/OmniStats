import random
import matplotlib.pyplot as plt
from Statistica import Statistica as s
from Utility import Utility as util

if __name__ == "__main__":
    size = 20
    x_dataset = [random.randrange(1, 101) for _ in range(size)]
    y_dataset = [random.randrange(1, 101) for _ in range(size)]

    x_stat = s.Statistica(x_dataset)
    y_stat = s.Statistica(y_dataset)

    print(x_stat.get_dataset())

    # plot x data
    x_stat.plot_data("X array")
    y_stat.plot_data("Y array")

    # Empirical Cumulative Distribution Function
    x, y = x_stat.ecdf()
    # Plot the ECDF as dots
    plt.plot(x, y * 100, linestyle='dotted', lw=2)
    plt.show()

    # Covariance and regression line
    x_cov = x_stat.covariance(y_stat)
    b = x_cov / y_stat.variance()
    a = y_stat.mean() - b * x_stat.mean()

    plt.scatter(x_dataset, y_dataset)
    plt.title("Regression line and x, y correlation")
    util.create_line([0, a], [1, b + a])
    plt.show()
