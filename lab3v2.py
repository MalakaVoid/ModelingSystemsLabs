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
#------------------ TASK 2 ------------------

def rasp_norm_zak(x_arr, m=10.0, o=2.0):
    y_arr = []
    for x in x_arr:
        y_arr.append(norm.cdf(x, m, o))
    return y_arr

def gen_x_arr(N):
    x_arr = []
    for i in range(0, N):
        x_arr.append(random.uniform(0, 20))
    x_arr.sort()
    return x_arr

x_arr = gen_x_arr(10**2)
y_arr = rasp_norm_zak(x_arr)
plt.plot(x_arr, y_arr, linewidth=3)
plt.grid(True)
plt.show()
#----------------------- TASK 3 ----------------
# Параметры нормального распределения
mean = 10
std_dev = 2

# Генерация значений для x (значения, для которых будет вычисляться функция распределения)
#x = np.linspace(0, 20, 100)
x = np.random.uniform(0, 20, 100)
x.sort()
# Вычисление значений функции распределения для каждого значения x
y = norm.cdf(x, loc=mean, scale=std_dev)

# Построение графика функции распределения
plt.plot(x, y)
plt.xlabel('Значение')
plt.ylabel('Функция распределения')
plt.title('Нормальное распределение (M={}, σ={})'.format(mean, std_dev))
plt.grid(True)
plt.show()

# Параметры нормального распределения
mean = 10
std_dev = 2

# Диапазон значений
start = 0
end = 20

# Функция обратной функции
def inverse_transform_sampling(n):
    # Генерация равномерно распределенных случайных чисел
    u = np.random.uniform(0, 1, n)

    # Кусочно-линейная аппроксимация обратной функции
    inverse_func = np.interp(u, norm.cdf(x, loc=mean, scale=std_dev), x)

    return inverse_func

# Число экспериментов для моделирования
N = [10**2, 10**3, 10**4, 10**5]

arr = []
# Моделирование и построение гистограмм
for n in N:
    # Моделирование нормально распределенных случайных чисел с использованием обратной функции
    samples = inverse_transform_sampling(n)
    arr.append(samples)
    # Построение гистограммы
    plt.hist(samples, bins=50, density=True, alpha=0.5, label=f'N = {n}')

# Построение графика функции распределения
plt.plot(x, y, color='red', label='Нормальное распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Моделирование нормального распределения с помощью метода обратной функции')
plt.legend()
plt.grid(True)
plt.show()



num_bins = 100

# Моделирование и построение гистограмм
for samples in arr:
    # Вычисление гистограммы относительных частот
    hist, bins = np.histogram(samples, bins=num_bins, density=True)
    bin_width = bins[1] - bins[0]
    hist = hist / (n * bin_width)

    # Построение гистограммы относительных частот
    plt.bar(bins[:-1], hist, width=bin_width, alpha=0.5, label=f'N = {n}')

# Построение графика функции распределения
plt.xlabel('Значение')
plt.ylabel('Относительная частота')
plt.title('Гистограмма относительных частот для моделирования нормального распределения')
plt.legend()
plt.grid(True)
plt.show()



start = 0
end = 20
mse = []

# Расчет экспериментальных распределений и среднеквадратичной погрешности
for samples in arr:
    hist, bins = np.histogram(samples, bins=num_bins, density=True)
    bin_width = bins[1] - bins[0]
    hist = hist / (n * bin_width)
    # Вычисление теоретического распределения
    x = np.linspace(start, end, num_bins)
    y = norm.pdf(x, loc=mean, scale=std_dev)

    # Расчет среднеквадратичной погрешности
    error = np.sqrt(np.mean((hist - y)**2))
    mse.append(error)

# Построение графика зависимости среднеквадратичной погрешности от числа экспериментов
plt.plot(N, mse)
plt.xlabel('Число экспериментов')
plt.ylabel('Среднеквадратичная погрешность')
plt.title('Зависимость среднеквадратичной погрешности от числа экспериментов')
plt.grid(True)
plt.show()
