import random
import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#----------------- TSAK 1 -----------------
def RAND(a, b, m, x_i):
    return math.fmod(a*x_i + b, m)

a = 22695477
b = 1
m = 2 ** 32
#---------------- END ----------------------

#---------------- TASK 2 -------------------
def task_2_func(x_0, a, b, m, RNumsArr, RParamsArr, counter):
    A = 0
    B = 10
    N = 10**counter

    RNumsArr.append(RAND(a, b, m, x_0))

    for i in range(1, N):
        RNumsArr.append(RAND(a, b, m, RNumsArr[i - 1]))

    for i in range(0, N):
        RNumsArr[i] /= m
        RParamsArr.append(A + (B - A) * RNumsArr[i])

    print(f"e{counter} = {max(RParamsArr)}")
    print(f"e{counter} = {min(RParamsArr)}")


x_0 = 1
A = 0
B = 10

RNumsArr_e2 = list()
RParamsArr_e2 = list()
task_2_func(x_0, a, b, m, RNumsArr_e2, RParamsArr_e2, 2)

RNumsArr_e3 = list()
RParamsArr_e3 = list()
task_2_func(x_0, a, b, m, RNumsArr_e3, RParamsArr_e3, 3)

RNumsArr_e4 = list()
RParamsArr_e4 = list()
task_2_func(x_0, a, b, m, RNumsArr_e4, RParamsArr_e4, 4)

RNumsArr_e5 = list()
RParamsArr_e5 = list()
task_2_func(x_0, a, b, m, RNumsArr_e5, RParamsArr_e5, 5)
#----------------------- END --------------------------
print()
#---------------------- TASK 3 ------------------------
M = (A + B) / 2
D = ((B - A) ** 2) / 12
print(f"M = {M}\nD = {D}\n")

def sum_pow_func(arr, pow):
    result = 0.0
    for each in arr:
        result += each**pow
    return result

def get_M_D(M, D, N, RParamsArr, counter):
    M_e = sum_pow_func(RParamsArr, 1) / N
    D_e = ((sum_pow_func(RParamsArr, 2) / N) - M_e ** 2) * (N / (N - 1))

    print(f"M_e{counter} = {M_e}")
    print(f"D_e{counter} = {D_e}")

    EpsM = math.fabs((M - M_e) / M) * 100
    EpsD = math.fabs((D - D_e) / D) * 100

    print(f"EpsM{counter - 1} = {EpsM}")
    print(f"EpsD{counter - 1} = {EpsD}\n")

    return M_e, D_e, EpsM, EpsD


N = 10 ** 2
M_e2, D_e2, EpsM1, EpsD1 = get_M_D(M, D, N, RParamsArr_e2, 2)

N = 10 ** 3
M_e3, D_e3, EpsM2, EpsD2 = get_M_D(M, D, N, RParamsArr_e3, 3)

N = 10 ** 4
M_e4, D_e4, EpsM3, EpsD3 = get_M_D(M, D, N, RParamsArr_e4, 4)

N = 10 ** 5
M_e5, D_e5, EpsM4, EpsD4 = get_M_D(M, D, N, RParamsArr_e5, 5)
#------------------------- END --------------------------------

#------------------------ TASK 4 ------------------------------
def RANDPeriod(X):
    n = len(X)
    period = 0
    first_pos = 1
    second_pos = 2
    result = []
    for i in range(0, n):
        element = X[i]
        for j in range(i, n):
            if element == X[j] and i != j:
                result.append(j - i)
                result.append(i)
                result.append(j)
                return result
    result.append(-1)
    result.append(-1)
    result.append(-1)
    return result

# TEST_1 = RANDPeriod(RParamsArr_e2)
# TEST_2 = RANDPeriod(RParamsArr_e3)
# TEST_3 = RANDPeriod(RParamsArr_e4)
# TEST_4 = RANDPeriod(RParamsArr_e5)
#
# print(f"Test_1 = {TEST_1}\n"
#       f"Test_2 = {TEST_2}\n"
#       f"Test_3 = {TEST_3}\n"
#       f"Test_4 = {TEST_4}\n")
#------------------ END ---------------------------

#------------------ TASK 5 ------------------------
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
#----------------- END ---------------------------

#----------------- TASK 6 -------------------------
def get_x2_func(resY, K):
    x2 = 0
    for i in range(0, K):
        tmp = (1 / K - resY[i]) ** 2
        x2 += tmp / resY[i]
    return x2


K = 10
resX = list()
for k in range(0, K):
    resX.append(((B - A) / K) * (0.5 + k))

resY_e2 = GetFreqDistr(RParamsArr_e2, A, B, K)
x2_e2 = get_x2_func(resY_e2, K)

resY_e3 = GetFreqDistr(RParamsArr_e3, A, B, K)
x2_e3 = get_x2_func(resY_e3, K)

resY_e4 = GetFreqDistr(RParamsArr_e4, A, B, K)
x2_e4 = get_x2_func(resY_e4, K)

resY_e5 = GetFreqDistr(RParamsArr_e5, A, B, K)
x2_e5 = get_x2_func(resY_e5, K)



print(f"x2_e2 = {x2_e2}")
print(f"x2_e3 = {x2_e3}")
print(f"x2_e4 = {x2_e4}")
print(f"x2_e5 = {x2_e5}")

print(f"resY_e2 = {resY_e2}")
print(f"resY_e3 = {resY_e3}")
print(f"resY_e4 = {resY_e4}")
print(f"resY_e5 = {resY_e5}")

fig, ax = plt.subplots(1, 4)
ax[0].bar([i for i in range(1, len(resY_e2)+1)], resY_e2)
ax[0].set_title('resY_e2')
ax[1].bar([i for i in range(1, len(resY_e3)+1)], resY_e3)
ax[1].set_title('resY_e3')
ax[2].bar([i for i in range(1, len(resY_e4)+1)], resY_e4)
ax[2].set_title('resY_e4')
ax[3].bar([i for i in range(1, len(resY_e5)+1)], resY_e5)
ax[3].set_title('resY_e5')
plt.show()
#-----------------TASK 7  -------------------
print("---------------------777777777777-------------------")
def task_2_func(RParamsArr, counter):
    A = 0
    B = 10
    N = 10**counter

    for i in range(1, N):
        RParamsArr.append(random.uniform(A,B))

    print(f"e{counter} = {max(RParamsArr)}")
    print(f"e{counter} = {min(RParamsArr)}")


A = 0
B = 10

RParamsArr_e2 = list()
task_2_func(RParamsArr_e2, 2)

RParamsArr_e3 = list()
task_2_func(RParamsArr_e3, 3)

RParamsArr_e4 = list()
task_2_func(RParamsArr_e4, 4)

RParamsArr_e5 = list()
task_2_func(RParamsArr_e5, 5)

print()

M = (A + B) / 2
D = ((B - A) ** 2) / 12
print(f"M = {M}\nD = {D}\n")

def sum_pow_func(arr, pow):
    result = 0.0
    for each in arr:
        result += each**pow
    return result

def get_M_D(M, D, N, RParamsArr, counter):
    M_e = sum_pow_func(RParamsArr, 1) / N
    D_e = ((sum_pow_func(RParamsArr, 2) / N) - M_e ** 2) * (N / (N - 1))

    print(f"M_e{counter} = {M_e}")
    print(f"D_e{counter} = {D_e}")

    EpsM = math.fabs((M - M_e) / M) * 100
    EpsD = math.fabs((D - D_e) / D) * 100

    print(f"EpsM{counter - 1} = {EpsM}")
    print(f"EpsD{counter - 1} = {EpsD}\n")

    return M_e, D_e, EpsM, EpsD


N = 10 ** 2
M_e2, D_e2, EpsM1, EpsD1 = get_M_D(M, D, N, RParamsArr_e2, 2)

N = 10 ** 3
M_e3, D_e3, EpsM2, EpsD2 = get_M_D(M, D, N, RParamsArr_e3, 3)

N = 10 ** 4
M_e4, D_e4, EpsM3, EpsD3 = get_M_D(M, D, N, RParamsArr_e4, 4)

N = 10 ** 5
M_e5, D_e5, EpsM4, EpsD4 = get_M_D(M, D, N, RParamsArr_e5, 5)

def RANDPeriod(X):
    n = len(X)
    period = 0
    first_pos = 1
    second_pos = 2
    result = []
    for i in range(0, n):
        element = X[i]
        for j in range(i, n):
            if element == X[j] and i != j:
                result.append(j - i)
                result.append(i)
                result.append(j)
                return result
    result.append(-1)
    result.append(-1)
    result.append(-1)
    return result

# TEST_1 = RANDPeriod(RParamsArr_e2)
# TEST_2 = RANDPeriod(RParamsArr_e3)
# TEST_3 = RANDPeriod(RParamsArr_e4)
# TEST_4 = RANDPeriod(RParamsArr_e5)
#
# print(f"Test_1 = {TEST_1}\n"
#       f"Test_2 = {TEST_2}\n"
#       f"Test_3 = {TEST_3}\n"
#       f"Test_4 = {TEST_4}\n")

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


def get_x2_func(resY, K):
    x2 = 0
    for i in range(0, K):
        tmp = (1 / K - resY[i]) ** 2
        x2 += tmp / resY[i]
    return x2


K = 10
resX = list()
for k in range(0, K):
    resX.append(((B - A) / K) * (0.5 + k))

resY_e2 = GetFreqDistr(RParamsArr_e2, A, B, K)
x2_e2 = get_x2_func(resY_e2, K)

resY_e3 = GetFreqDistr(RParamsArr_e3, A, B, K)
x2_e3 = get_x2_func(resY_e3, K)

resY_e4 = GetFreqDistr(RParamsArr_e4, A, B, K)
x2_e4 = get_x2_func(resY_e4, K)

resY_e5 = GetFreqDistr(RParamsArr_e5, A, B, K)
x2_e5 = get_x2_func(resY_e5, K)



print(f"x2_e2 = {x2_e2}")
print(f"x2_e3 = {x2_e3}")
print(f"x2_e4 = {x2_e4}")
print(f"x2_e5 = {x2_e5}")

print(f"resY_e2 = {resY_e2}")
print(f"resY_e3 = {resY_e3}")
print(f"resY_e4 = {resY_e4}")
print(f"resY_e5 = {resY_e5}")

fig, ax = plt.subplots(1, 4)
ax[0].bar([i for i in range(1, len(resY_e2)+1)], resY_e2)
ax[0].set_title('resY_e2')
ax[1].bar([i for i in range(1, len(resY_e3)+1)], resY_e3)
ax[1].set_title('resY_e3')
ax[2].bar([i for i in range(1, len(resY_e4)+1)], resY_e4)
ax[2].set_title('resY_e4')
ax[3].bar([i for i in range(1, len(resY_e5)+1)], resY_e5)
ax[3].set_title('resY_e5')
plt.show()