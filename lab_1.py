import math
from random import uniform

#------------------- TASK 1 --------------------
def CALC_PI(x0, y0, r0, exp_num):
    x_min = x0 - r0
    x_max = x0 + r0
    y_min = y0 - r0
    y_max = y0 + r0
    m = 0
    for j in range(1, exp_num):
        p = uniform(0, 1)
        x = (x_max - x_min)*p + x_min
        p = uniform(0, 1)
        y = (y_max - y_min)*p + y_min
        if ((x - x0)**2 + (y - y0)**2) < r0**2:
            m += 1
    pi = m / exp_num * 4
    return pi

print(f'Result: {CALC_PI(2, 1, 4, 10**5)}')
#-------------------- END -----------------------

#-------------------- TASK 2 --------------------
def seria_fill(seria_list):
    for i in range(4, 9):
        seria_list.append(CALC_PI(1, 2, 5, 10 ** i))

SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5 = list(), list(), list(), list(), list()
seria_fill(SERIA_1)
seria_fill(SERIA_2)
seria_fill(SERIA_3)
seria_fill(SERIA_4)
seria_fill(SERIA_5)

print(f"Seria 1 = {SERIA_1}")
print(f"Seria 2 = {SERIA_2}")
print(f"Seria 3 = {SERIA_3}")
print(f"Seria 4 = {SERIA_4}")
print(f"Seria 5 = {SERIA_5}")
#------------------- END --------------------------------

#-------------------- TASK 3 ----------------------------
def eps_fill(eps_list, seria_list):
    for i in range(0, 5):
        eps = math.fabs((seria_list[i] - math.pi) / math.pi)
        eps_list.append(eps)

eps_1, eps_2, eps_3, eps_4, eps_5 = list(), list(), list(), list(), list()
eps_fill(eps_1, SERIA_1)
eps_fill(eps_2, SERIA_2)
eps_fill(eps_3, SERIA_3)
eps_fill(eps_4, SERIA_4)
eps_fill(eps_5, SERIA_5)

print(f"Eps1 = {eps_1}")
print(f"Eps2 = {eps_2}")
print(f"Eps3 = {eps_3}")
print(f"Eps4 = {eps_4}")
print(f"Eps5 = {eps_5}")

def avg_eps_fill(s_1, s_2, s_3, s_4, s_5):
    e = 4
    for i in range(0, 5):
        s_e = (s_1[i] + s_2[i] + s_3[i] + s_4[i] + s_5[i]) / 5
        eps_s_e = math.fabs((s_e - math.pi)/math.pi)
        print(f'Eps_S_e{e} = {eps_s_e}')
        e += 1

avg_eps_fill(eps_1, eps_2, eps_3, eps_4, eps_5)
#-------------------- END ---------------------------

#------------------ TASK 4 ------------------------------
def func(x):
    return x**3 + 1


def CALC_INTEGRAL(a, b, f, ExpNmb):
    x_min, x_max, y_min, y_max = a, b, 0, f(b)
    m = 0
    for exp in range(ExpNmb):
        p = uniform(0, 1)
        x = (x_max - x_min) * p + x_min
        p = uniform(0, 1)
        y = (y_max - y_min) * p + y_min
        if f(x) > y:
            m += 1
    s = m / ExpNmb * (b - a) * f(b)
    return s

def seria_integral_fill(seria_list):
    for i in range(4, 9):
        seria_list.append(CALC_INTEGRAL(0, 2, func, 10 ** i))

SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5 = list(), list(), list(), list(), list()
seria_integral_fill(SERIA_1)
seria_integral_fill(SERIA_2)
seria_integral_fill(SERIA_3)
seria_integral_fill(SERIA_4)
seria_integral_fill(SERIA_5)

print(f"Seria 1 = {SERIA_1}")
print(f"Seria 2 = {SERIA_2}")
print(f"Seria 3 = {SERIA_3}")
print(f"Seria 4 = {SERIA_4}")
print(f"Seria 5 = {SERIA_5}")

eps_1, eps_2, eps_3, eps_4, eps_5 = list(), list(), list(), list(), list()
eps_fill(eps_1, SERIA_1)
eps_fill(eps_2, SERIA_2)
eps_fill(eps_3, SERIA_3)
eps_fill(eps_4, SERIA_4)
eps_fill(eps_5, SERIA_5)

print(f"Eps1 = {eps_1}")
print(f"Eps2 = {eps_2}")
print(f"Eps3 = {eps_3}")
print(f"Eps4 = {eps_4}")
print(f"Eps5 = {eps_5}")

avg_eps_fill(eps_1, eps_2, eps_3, eps_4, eps_5)