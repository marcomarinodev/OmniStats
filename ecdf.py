import numpy as np
import matplotlib.pyplot as plt
import random
import dc_stat_think as dcst

def variance(data, mean):
	summation = 0
	for x in data:
		summation = summation + (x-mean)**2
	
	return summation/(len(data)-1)

def main():
	randomData = []
	size = 13
	
	for i in range(0, size):
		n = random.randint(1,10)
		randomData.append(n)
	
	_variance = variance(randomData, np.mean(randomData))
	_mean = np.mean(randomData)
	_sdeviation = np.sqrt(_variance)
	
	print(randomData)
	plt.hist(randomData, bins=10)
	plt.title("Mean: %.3f; Standard Deviation: %.5f; Variance: %.5f" % (_mean, _sdeviation, _variance))
	plt.show()
	
	# Empirical Cumulative Distribution Function
	# Generate x and y values for ECDF: x, y
	x, y = dcst.ecdf(randomData)
	# Plot the ECDF as dots
	_ = plt.plot(x, y*100, linestyle='dotted', lw=2)
	plt.show()

if __name__ == "__main__":
	main()

