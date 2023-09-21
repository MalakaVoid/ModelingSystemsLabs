import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

#---------------- TASK 1 --------------------
def draw_graph(m, o):
    global count
    p = lambda x: (1 / (o * (2 * math.pi)**(1/2))) * math.e**((-(x-m)**2) / 2 * o ** 2)
    fig = plt.subplots()
    x = np.linspace(0, 20, 200)
    plt.plot(x, p(x))
    plt.title(f"M = {m}, o = {o}")
    plt.show()

draw_graph(10, 2)
draw_graph(10, 1)
draw_graph(10, 0.5)
draw_graph(12, 1)
plt.show()
#------------------ END ---------------------
#------------------ TASK 2 ------------------
draw_graph(10, 2)
plt.show()