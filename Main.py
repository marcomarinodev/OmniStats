import random
import matplotlib.pyplot as plt
from Statistica import Statistica as s

if __name__ == "__main__":
    size = 13
    dataset = [random.randrange(1, 101) for _ in range(size)]

    stat = s.Statistica(dataset)
    print(stat.get_dataset())

    # plot data
    plt.hist(stat.get_dataset())
    plt.title("Mean: {:.2f}; Standard Deviation: {:.5f}; Variance: {:.5f}".format(
        stat.mean(), stat.standard_deviation(), stat.variance()))
    plt.show()

    # Empirical Cumulative Distribution Function
    x, y = stat.ecdf()
    # Plot the ECDF as dots
    plt.plot(x, y * 100, linestyle='dotted', lw=2)
    plt.show()
