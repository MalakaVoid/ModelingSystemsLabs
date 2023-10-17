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
    x_arr = np.linspace(0, 20, 100)
    y_arr = []
    for x in x_arr:
        #Формула:
        first = 1 / (o * ((2*math.pi)**(1/2)))
        second = - (((x-m)**2) / (2*(o**2)))
        third = math.e**second
        result = first * third
        y = result
        y_arr.append(y)
    return x_arr, y_arr


fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
x_arr, y_arr = rasp_plot(2, 10)
axs[0][0].plot(x_arr, y_arr, linewidth=3)
axs[0][0].set_title("o=2 m=10")
x_arr, y_arr = rasp_plot(1, 10)
axs[0][1].plot(x_arr, y_arr, linewidth=3)
axs[0][1].set_title("o=1 m=10")
x_arr, y_arr = rasp_plot(0.5, 10)
axs[1][0].plot(x_arr, y_arr,linewidth=3)
axs[1][0].set_title("o=0.5 m=10")
x_arr, y_arr = rasp_plot(1, 12)
axs[1][1].plot(x_arr, y_arr, linewidth=3)
axs[1][1].set_title("o=1 m=12")
plt.show()
#------------------ END ---------------------
#------------------ TASK 2 ------------------
def norm_zak_rasp(x, o=2.0, m=10.0):
    first = 1 / (o * ((2*math.pi)**(1/2)))
    second = - (((x-m)**2) / (2*(o**2)))
    third = math.e**second
    result = first * third
    return result

def gen_x_y(N, o=2.0, m=10.0):
    x_arr = []
    y_arr = []
    for i in range(0, N):
        x = random.uniform(0, 20)
        x_arr.append(x)
    x_arr.sort()
    for x in x_arr:
        y_arr.append(norm_zak_rasp(x, o, m))
    return x_arr, y_arr

x_arr_e2, y_arr_e2 = gen_x_y(10**4)

plt.figure(figsize=(12, 7))
plt.plot(x_arr_e2, y_arr_e2, linewidth=3)
plt.title("o=2 m=10 N=10^2")
plt.grid(True)
plt.show()
#------------------ TASK 3 ------------------

x_rev_e2 = norm.ppf(y_arr_e2, 10, 2)
print(len(x_rev_e2))
x_arr_e3, y_arr_e3 = gen_x_y(10**3)
x_rev_e3 = norm.ppf(x_arr_e3, 10, 2)

x_arr_e4, y_arr_e4 = gen_x_y(10**4)
x_rev_e4 = norm.ppf(x_arr_e4, 10, 2)

x_arr_e5, y_arr_e5 = gen_x_y(10**5)
x_rev_e5 = norm.ppf(y_arr_e5, 10, 2)

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
axs[0][0].plot(x_rev_e2, y_arr_e2, linewidth=3)
axs[0][0].set_title("N=10^2")
axs[0][0].grid(True)
axs[0][1].plot(x_rev_e3, x_arr_e3, linewidth=3)
axs[0][1].set_title("N=10^3")
axs[0][1].grid(True)
axs[1][0].plot(x_rev_e4, x_arr_e4, linewidth=3)
axs[1][0].set_title("N=10^4")
axs[1][0].grid(True)
axs[1][1].plot(x_rev_e5, y_arr_e5, linewidth=3)
axs[1][1].set_title("N=10^5")
plt.grid(True)
plt.show()

#--------------------- TASK 4 ---------------
def GetFreqDistr(RParamsArr, A, B, IntervalsCount):
    dY = (B - A) / IntervalsCount
    Freq = list()
    for i in range(0, IntervalsCount):
        Freq.append(0)
    for j in range(0, len(RParamsArr)):
        Yc = RParamsArr[j]
        fN = math.floor(Yc / dY)
        Freq[fN] += 1
    for i in range(0, IntervalsCount):
        Freq[i] /= (len(RParamsArr) * dY)
    return Freq

print(GetFreqDistr(x_rev_e5, 0, 20, 100))

