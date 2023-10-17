import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.special import erfinv
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
#-------------------Task 2-----------------------
m = 10
o = 2
x = np.random.uniform(0, 20, 100)
x.sort()
y = norm.cdf(x, loc=m, scale=o)
plt.plot(x, y)
plt.xlabel('Значение')
plt.ylabel('Функция распределения')
plt.title('Нормальное распределение (M={}, σ={})'.format(m, o))
plt.grid(True)
plt.show()

#-------------------Task 3----------------------
# Параметры нормального распределения
m = 10
o = 2
start = 0
end = 20

# Функция обратной функции
def inverse_transform_sampling(n):
    # Генерация равномерно распределенных случайных чисел
    u = np.random.uniform(0, 1, n)
    # Кусочно-линейная аппроксимация обратной функции
    inverse_func = np.interp(u, norm.cdf(x, loc=m, scale=o), x)
    return inverse_func

N = [10**2, 10**3, 10**4, 10**5]
experiments = []
for n in N:
    samples = inverse_transform_sampling(n)
    experiments.append(samples)
    print(f"Для количества экспериментов {n}:")
    print(samples[0:10])

#-------------------Task 4-----------------------

num_bins = 100
tmp = 2
# Моделирование и построение гистограмм
for samples in experiments:
    # Вычисление гистограммы относительных частот
    hist, bins = np.histogram(samples, bins=num_bins, density=True)
    bin_width = bins[1] - bins[0]
    hist = hist / ((10**tmp) * bin_width)
    # Построение гистограммы относительных частот
    plt.bar(bins[:-1], hist, width=bin_width, alpha=0.5)
    plt.xlabel('Значение')
    plt.ylabel('Относительная частота')
    plt.title(f'Гистограмма относительных частот для {10**tmp}')
    plt.grid(True)
    plt.show()
    tmp+=1

#-------------------Task 5-----------------------

mse = []
tmp =2
for samples in experiments:
    hist, bins = np.histogram(samples, bins=num_bins, density=True)
    bin_width = bins[1] - bins[0]
    hist = hist / ((10**tmp) * bin_width)
    tmp+=1
    # Вычисление теоретического распределения
    x = np.linspace(start, end, num_bins)
    y = norm.pdf(x, loc=m, scale=o)

    # Расчет среднеквадратичной погрешности
    error = np.sqrt(np.mean((hist - y)**2))
    mse.append(error)

plt.plot(N, mse)
plt.xlabel('Число экспериментов')
plt.ylabel('Среднеквадратичная погрешность')
plt.title('Зависимость среднеквадратичной погрешности от числа экспериментов')
plt.grid(True)
plt.show()
