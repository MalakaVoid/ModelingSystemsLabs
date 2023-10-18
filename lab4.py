import random
from collections import Counter
import math

#------------- TASK 1 -------------------
print("------------- TASK 1 -------------------")
def generate_sequence(length, a, b, M, x0):
    sequence = [x0]
    for i in range(1, length):
        sequence.append(math.fmod(a*sequence[i-1] + b, M))
    sequence.sort()
    return sequence

TZmin = 4
TZmax = 12
a_TZ = 39
b = 1
M = 1000
x0 = 1

TSmin = 2
TSmax = 8
a_TS = 39

X_TZ = generate_sequence(10, a_TZ, b, M, x0)
X_TS = generate_sequence(10, a_TS, b, M, x0)

T_Z = []
T_S = []

for i in range(len(X_TZ)):
    T_Z.append(TZmin + (X_TZ[i] / M) * (TZmax - TZmin))
    T_S.append(TSmin + (X_TS[i] / M) * (TSmax - TSmin))

print("Время поступления заявок:")
print(T_Z)

print("Время обработки заявок на сервере:")
print(T_S)

#----------------- TASK 2 -------------------
print("----------------- TASK 2 -------------------")

arrival_times = []
processing_time = T_Z[0]

for i in range(len(T_Z)):
    if processing_time < T_Z[i]:
        arrival_times.append(T_Z[i])
        processing_time = T_Z[i] + T_S[i]
    else:
        arrival_times.append(processing_time)
        processing_time += T_S[i]


print("Время прихода программ в вычислительную систему:")
print(arrival_times)

#------------- TASK 3 ---------------------
print("------------- TASK 3 ---------------------")
def get_programs_time_in_buffer(arrival_times, proccesing_times):
    #Рассчитываем время начала обработки программы сервером
    all_time_of_start_computing = []
    time_of_start_computing = arrival_times[0]

    for i in range(0, len(arrival_times)):
        if time_of_start_computing < arrival_times[i]:
            all_time_of_start_computing.append(arrival_times[i])
            time_of_start_computing = arrival_times[i] + proccesing_times[i]
        else:
            all_time_of_start_computing.append(time_of_start_computing)
            time_of_start_computing += proccesing_times[i]

    #Рассчитываем время нахождение в буфере
    time_in_buffer_each = []
    time_in_buffer = 0
    for i in range(0, len(arrival_times)):
        time_in_buffer = all_time_of_start_computing[i] - arrival_times[i]
        time_in_buffer_each.append(time_in_buffer)
    return time_in_buffer_each

#------------------ TASK 4 ----------------------------
print("------------------ TASK 4 ----------------------------")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Возник вопрос, нужно ли делать то что я снизу делаю
#Нужно ли расчитывать время нахождения одной, двух и тд программ в буфере одновременно или нужно просто время
#нахождения в буфере просто каждой программы
def get_time_in_buffer_together(arrivals, buffers):
    count_of_programs = 1
    buffers_pr_time = [0 for i in range(0, 10)]
    arrival = 0
    exit_time = 0
    for i in range(0, len(arrivals)):
        if exit_time > arrivals[i]:
            arrival = exit_time
        else:
            arrival = arrivals[i]

        count_of_programs = 0

        if buffers[i] != 0:
            count_of_programs = 1

        exit_time = arrivals[i] + buffers[i]

        for j in range(i+1, len(arrivals)):
            if arrival < arrivals[j] and arrivals[j] < exit_time:
                buffers_pr_time[count_of_programs] += arrivals[j] - arrival
                count_of_programs += 1
                arrival = arrivals[j]

        buffers_pr_time[count_of_programs] += exit_time - arrival
    return buffers_pr_time


time_in_buffer_each = get_programs_time_in_buffer(T_Z, T_S)
buffers_pt_time = get_time_in_buffer_together(T_Z, time_in_buffer_each)

print("Время в буфере нескольких программ одновременно")
for i in range(1, len(buffers_pt_time)):
    print(f"{i} программ одновременно: {buffers_pt_time[i]}")

print()
print("Время в буфере каждой программы")
print(time_in_buffer_each)


#------------------- TASK 5 ---------------------------
print("------------------- TASK 5 ---------------------------")
print("Вероятность нахождения заявок в буфере")
tmp = 0
probability = 1
for each in time_in_buffer_each:
    if probability == 0:
        probability = 1
    probability = each / sum(time_in_buffer_each)
    print(f"Вероятность нахождения в буфере программы {tmp}: {probability}")
    tmp += 1

print()
print("Вероятность нахождения количества заявок в буфере одновременно")
probability = 1
for i in range(1, len(buffers_pt_time)):
    if probability == 0:
        probability = 1
    probability = buffers_pt_time[i] / sum(buffers_pt_time)
    print(f"Вероятность нахождения в буфере {i} программ: {probability}")
#------------------ Task 6 ---------------------------
print("------------------- TASK 6 ---------------------------")
def generate_requests_sequence(n, lambda_param):
    requests_sequence = []
    for _ in range(n):
        u = random.random()  # генерация случайного числа U из равномерного распределения [0, 1)
        x = -math.log(1 - u) / lambda_param  # рассчитываем значение X согласно обратной функции
        requests_sequence.append(x)
    requests_sequence.sort()
    return requests_sequence

n = 10  # количество заявок
lambda_param = 1/3

requests_sequence = generate_requests_sequence(n, lambda_param)
print("Время прихода программы")
print(requests_sequence)

def generate_processing_times_sequence(n, mu_param):
    processing_times_sequence = []
    for _ in range(n):
        u = random.random()  # генерация случайного числа U из равномерного распределения [0, 1)
        x = -math.log(1 - u) / mu_param  # рассчитываем значение X согласно обратной функции
        processing_times_sequence.append(x)
    return processing_times_sequence

n = 10  # количество заявок
mu_param = 1/4

processing_times_sequence = generate_processing_times_sequence(n, mu_param)
print("Время обработки программы")
print(processing_times_sequence)
#------------------- TASK 7 ---------------------------
print("------------------- TASK 7 ---------------------------")

time_in_buffer_each = get_programs_time_in_buffer(requests_sequence, processing_times_sequence)
buffers_pt_time = get_time_in_buffer_together(T_Z, time_in_buffer_each)

print("Время в буфере нескольких программ одновременно")
for i in range(1, len(buffers_pt_time)):
    print(f"{i} программ одновременно: {buffers_pt_time[i]}")
print("Время в буфере каждой программы")
print(time_in_buffer_each)

print("Вероятность нахождения заявок в буфере")
tmp = 0
probability = 1
for each in time_in_buffer_each:
    if probability == 0:
        probability = 1
    probability = each / sum(time_in_buffer_each)
    print(f"Вероятность нахождения в буфере программы {tmp}: {probability}")
    tmp += 1

print()
print("Вероятность нахождения количества заявок в буфере одновременно")
probability = 1
for i in range(1, len(buffers_pt_time)):
    if probability == 0:
        probability = 1
    probability = buffers_pt_time[i] / sum(buffers_pt_time)
    print(f"Вероятность нахождения в буфере {i} программ: {probability}")
