import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
import scipy as sc

#---------------- TASK 1 -----------------


def gen_x_y(N, o=2.0, m=10.0):
    x_arr = []
    for i in range(0, N):
        x = random.uniform(0, 20)
        x_arr.append(x)
    x_arr.sort()
    return x_arr

x_arr = gen_x_y(10**3)
#x_arr = np.linspace(0, 20, 1000)
y_arr = norm.pdf(x_arr, 10, 2)
plt.plot(x_arr, y_arr, linewidth=3)
plt.show()
x_rev = []
for x in x_arr:
    x_rev.append(norm.ppf(x, 10, 2))
print(x_rev)
plt.plot(x_rev, x_arr, linewidth=3)
plt.show()
