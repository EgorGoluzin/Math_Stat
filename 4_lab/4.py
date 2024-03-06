import numpy as np
import math
import matplotlib.pyplot as plt
import statistics

import scipy.stats

alpha = 0.05

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

def norm_math_wait(n, data, q):
    average = statistics.mean(data)
    otkl = statistics.stdev(data, average)
    m_min = average - (otkl * q) / math.sqrt(n - 1)
    m_max = average + (otkl * q) / math.sqrt(n - 1)
    a = [m_min, m_max]
    return a

def norm_sqrt(n, data, q1, q2):
    average = statistics.mean(data)
    otkl = statistics.stdev(data, average)
    sigma_min = math.sqrt(n - 1) * otkl / math.sqrt(q1)
    sigma_max = math.sqrt(n - 1) * otkl / math.sqrt(q2)
    a = [sigma_min, sigma_max]
    return a

def assimpt_math_wait(n, data, q):
    average = statistics.mean(data)
    otkl = statistics.stdev(data, average)
    m_min = average - (otkl * q) / math.sqrt(n)
    m_max = average + (otkl * q) / math.sqrt(n)
    a = [m_min, m_max]
    return a
def assimpt_sqrt(n, data, q):
    k = scipy.stats.kurtosis(data, bias = False)
    average = statistics.mean(data)
    otkl = statistics.stdev(data, average)
    sigma_min = otkl * (1 - 0.5 * q * math.sqrt((k + 2) / n))
    sigma_max = otkl * (1 + 0.5 * q * math.sqrt((k + 2) / n))
    a = [sigma_min, sigma_max]
    return a

names = ["Normal", "Cauchy", "Student", "Poisson", "Random"]
n_1 = 20
n_2 = 100

data_1 = normal(n_1)
data_2 = normal(n_2)
print(names[0], n_1)
res_norm = norm_math_wait(n_1, data_1, 2.09)
res_sqrt = norm_sqrt(n_1, data_1, 32.9, 8.91)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_1, data_1, 2.09)
res_sqrt = assimpt_sqrt(n_1, data_1, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

print(names[0], n_2)
res_norm = norm_math_wait(n_2, data_2, 1.96)
res_sqrt = norm_sqrt(n_2, data_2, 71.42, 32.34)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_2, data_2, 1.96)
res_sqrt = assimpt_sqrt(n_2, data_2, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

data_1 = cauchy(n_1)
data_2 = cauchy(n_2)
print(names[1], n_1)
res_norm = norm_math_wait(n_1, data_1, 2.09)
res_sqrt = norm_sqrt(n_1, data_1, 32.9, 8.91)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_1, data_1, 2.09)
res_sqrt = assimpt_sqrt(n_1, data_1, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

print(names[1], n_2)
res_norm = norm_math_wait(n_2, data_2, 1.96)
res_sqrt = norm_sqrt(n_2, data_2, 71.42, 32.34)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_2, data_2, 1.96)
res_sqrt = assimpt_sqrt(n_2, data_2, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

data_1 = student(n_1)
data_2 = student(n_2)
print(names[2], n_1)
res_norm = norm_math_wait(n_1, data_1, 2.09)
res_sqrt = norm_sqrt(n_1, data_1, 32.9, 8.91)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_1, data_1, 2.09)
res_sqrt = assimpt_sqrt(n_1, data_1, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

print(names[2], n_2)
res_norm = norm_math_wait(n_2, data_2, 1.96)
res_sqrt = norm_sqrt(n_2, data_2, 71.42, 32.34)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_2, data_2, 1.96)
res_sqrt = assimpt_sqrt(n_2, data_2, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

'''
data_1 = poisson(n_1)
data_2 = poisson(n_2)
print(names[3], n_1)
res_norm = norm_math_wait(n_1, data_1, 2.09)
res_sqrt = norm_sqrt(n_1, data_1, 32.9, 8.91)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_1, data_1, 2.09)
res_sqrt = assimpt_sqrt(n_1, data_1, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
'''

print(names[3], n_2)
res_norm = norm_math_wait(n_2, data_2, 1.96)
res_sqrt = norm_sqrt(n_2, data_2, 71.42, 32.34)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_2, data_2, 1.96)
res_sqrt = assimpt_sqrt(n_2, data_2, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

data_1 = random(n_1)
data_2 = random(n_2)
print(names[4], n_1)
res_norm = norm_math_wait(n_1, data_1, 2.09)
res_sqrt = norm_sqrt(n_1, data_1, 32.9, 8.91)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_1, data_1, 2.09)
res_sqrt = assimpt_sqrt(n_1, data_1, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])

print(names[4], n_2)
res_norm = norm_math_wait(n_2, data_2, 1.96)
res_sqrt = norm_sqrt(n_2, data_2, 71.42, 32.34)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
res_norm = assimpt_math_wait(n_2, data_2, 1.96)
res_sqrt = assimpt_sqrt(n_2, data_2, 1.96)
print(res_norm[0], "< m <", res_norm[1], " ", res_sqrt[0], "< sigma <", res_sqrt[1])
