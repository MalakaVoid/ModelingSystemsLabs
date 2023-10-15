import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math


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
        y_arr.append(norm_zak_rasp(y, o, m))
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

def gen_x_y(o=2.0, m=10.0):
    N = 10**3
    x_arr = []
    y_arr = []
    for i in range(0, N):
        x = random.uniform(0, 20)
        x_arr.append(x)
    x_arr.sort()
    for x in x_arr:
        y = (1 / (o * (2 * math.pi)**(1/2))) * math.e**((-(x-m)**2) / 2 * o ** 2)
        y_arr.append(norm_zak_rasp(y, o, m))
    return x_arr, y_arr

#------------------ TASK 3 ------------------

