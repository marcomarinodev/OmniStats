# Empirical-Cumulative-Distribution-Function
## Overview
This code is written for Statistics and Probability Course, and for now it shows:
1) Mean
2) Standard Deviation and Variance
3) Empirical Cumulative Distribution Function (ECDF)

#
![equation](https://latex.codecogs.com/gif.latex?n%3Ddatasize.)
### Mean
![equation](https://latex.codecogs.com/gif.latex?x_%7BM%7D%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_%7Bi%7D%7D%7Bn%7D)
### Variance
![equation](https://latex.codecogs.com/gif.latex?var%28x%29%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28x_%7Bi%7D-x_%7BM%7D%29%5E2%7D%7Bn-1%7D)
### Standard Deviation
![equation](https://latex.codecogs.com/gif.latex?%5Csigma%28x%29%3D%5Csqrt%7Bvar%28x%29%7D%3D%5Csqrt%7B%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28x_%7Bi%7D-x_%7BM%7D%29%5E2%7D%7Bn-1%7D%7D)
### Empirical Cumulative Distribution Function
![equation](https://latex.codecogs.com/gif.latex?F_%7Be%7D%28t%29%3D%5Cfrac%7B%5C%23%5C%7Bx_%7Bi%7D%7Cx_%7Bi%7D%5Cleq%20t%5C%7D%7D%7Bn%7D)
## ToDo:
- Regression Line Representation
- Covariance
- Load data from file (possibly add File class to handle that)
- Median and quartiles
## Improvements:
- Show both the plots at once, without having to close the first one to show the second one
- Maybe think about creating a more generic class to handle things like the covariance, that involves more than one dataset. This is just an organization choice though


