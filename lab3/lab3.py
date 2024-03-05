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

data = [normal(20), normal(100)]
#plt.boxplot(data, labels = labels)
plt.suptitle('Normal', fontsize = fs)

data = [cauchy(20), cauchy(100)]
#plt.boxplot(data, labels=labels)
plt.suptitle('Cauchy', fontsize = fs)

data = [student(20), student(100)]
#plt.boxplot(data, labels=labels)
plt.suptitle('Student', fontsize = fs)

data = [poisson(20), poisson(100)]
#plt.boxplot(data, labels=labels)
plt.suptitle('Poisson', fontsize = fs)

data = [random(20), random(100)]
#plt.boxplot(data, labels=labels)
plt.suptitle('Random', fontsize = fs)

plt.show()
