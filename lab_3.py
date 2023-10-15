import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
import scipy as sc

#---------------- TASK 1 --------------------
def rasp_plot(o=2.0, m=10.0):
    x_arr = []
    y_arr = []
    for i in range(0, 1000):
        x = random.uniform(0, 20)
        x_arr.append(x)
    x_arr.sort()
    for x in x_arr:
        y = (1 / (o * (2 * math.pi)**(1/2))) * math.e**((-(x-m)**2) / 2 * o ** 2)
        y_arr.append(y)
    return x_arr, y_arr


fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
x_arr, y_arr = rasp_plot(2, 10)
axs[0][0].plot(x_arr, y_arr, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=5)
axs[0][0].set_title("o=2 m=10")
x_arr, y_arr = rasp_plot(1, 10)
axs[0][1].plot(x_arr, y_arr, 'o-r', alpha=0.7, label="sec", lw=5, mec='b', mew=2, ms=5)
axs[0][1].set_title("o=1 m=10")
x_arr, y_arr = rasp_plot(0.5, 10)
axs[1][0].plot(x_arr, y_arr, 'o-r', alpha=0.7, label="third", lw=5, mec='b', mew=2, ms=5)
axs[1][0].set_title("o=0.5 m=10")
x_arr, y_arr = rasp_plot(1, 12)
axs[1][1].plot(x_arr, y_arr, 'o-r', alpha=0.7, label="fourth", lw=5, mec='b', mew=2, ms=5)
axs[1][1].set_title("o=1 m=12")
plt.grid(True)
plt.show()
#------------------ END ---------------------
#------------------ TASK 2 ------------------
def norm_zak_rasp(x, o=2.0, m=10.0):
    return (1 / (o * (2 * math.pi)**(1/2))) * math.e**((-(x-m)**2) / 2 * o ** 2)

def gen_x_y(N, o=2.0, m=10.0):
    N = 10**2
    x_arr = []
    y_arr = []
    for i in range(0, N):
        x = random.uniform(0, 20)
        x_arr.append(x)
    x_arr.sort()
    for x in x_arr:
        y_arr.append(norm_zak_rasp(x))
    return x_arr, y_arr

x_arr_e2, y_arr_e2 = gen_x_y(10**2)

plt.figure(figsize=(12, 7))
plt.plot(x_arr_e2, y_arr_e2, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=5)
plt.title("o=2 m=10 N=10^2")
plt.grid(True)
plt.show()
#------------------ TASK 3 ------------------
def reverse_fnc(x_arr):
    o=2
    m=10
    func = lambda t: math.e**((-(t-m)**2)/2*(o**2))
    rev_y = []
    for x in x_arr:
        tmp = sc.integrate.quad(func, -math.inf, x)
        print(tmp)
        rev_y.append((1 / (o * (2 * math.pi)**(1/2)))*tmp[1])
    rev_y.sort()
    return rev_y

y_rev = reverse_fnc(x_arr_e2)

plt.figure(figsize=(12, 7))
plt.plot(x_arr_e2, y_rev, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=5)
plt.title("o=2 m=10 N=10^2")
plt.grid(True)
plt.show()
