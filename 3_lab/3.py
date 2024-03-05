import numpy as np
import math
import matplotlib.pyplot as plt

def normal (n):
    norm = np.random.normal(0, 1, n)
    return norm

def cauchy (n):
    cauchy = np.random.standard_cauchy(n)
    return cauchy

def student (n):
    stud = np.random.standard_t(3, n)
    return stud

def poisson (n):
    pois = np.random.poisson(10, n)
    return pois

def random (n):
    rand = np.random.uniform(-math.sqrt(3), math.sqrt(3), n)
    return rand

labels = [20, 100]
fs = 10
data1 = [normal(20), normal(100)]
data2 = [cauchy(20), cauchy(100)]
data3 = [student(20), student(100)]
data4 = [poisson(20), poisson(100)]
data5 = [random(20), random(100)]


fig, axs = plt.subplots(nrows = 1, ncols = 5)
axs[0].boxplot(data1, labels=labels)
axs[0].set_title('Normal', fontsize = fs)

axs[1].boxplot(data2, labels=labels)
axs[1].set_title('Cauchy', fontsize = fs)

axs[2].boxplot(data3, labels=labels)
axs[2].set_title('Student', fontsize = fs)

axs[3].boxplot(data1, labels=labels)
axs[3].set_title('Poisson', fontsize = fs)

axs[4].boxplot(data1, labels=labels)
axs[4].set_title('Random', fontsize = fs)

plt.show()
