import scipy.stats as sps
import numpy as np
import array as ar
import statistics
import math
from scipy import stats

n_mid = ar.array('f')
n_med = ar.array('f')
n_zr = ar.array('f')
n_zq = ar.array('f')
n_ztr = ar.array('f')

def normal (n):
    norm = np.random.normal(0, 1, n)
    return norm
def cauchy (n):
    cauch = np.random.standard_cauchy(n)
    return cauch
def student (n):
    stud = np.random.standard_t(3, n)
    return stud
def poisson (n):
    pois = np.random.poisson(10, n)
    return pois
def random (n):
    rand = np.random.uniform(-math.sqrt(3),math.sqrt(3), n)
    return rand

for i in range(1000):
    a = normal(10)
    n_mid.append(a.mean())
    n_med.append(statistics.median(a))
    n_zr.append(0.5 * (a[0] + a[len(a) - 1]))
    n_zq.append((np.quantile(a, 0.25) + np.quantile(a, 0.75)) * 0.5)
    n_ztr.append(stats.trim_mean(a, 0.25))

print("Normal n = 10:")
print("Mid:", statistics.mean(n_mid), statistics.variance(n_mid))
print("Med:", statistics.mean(n_med), statistics.variance(n_med))
print("Zr:", statistics.mean(n_zr), statistics.variance(n_zr))
print("Zq:", statistics.mean(n_zq), statistics.variance(n_zq))
print("Ztr:", statistics.mean(n_ztr), statistics.variance(n_ztr))

n_mid = ar.array('f')
n_med = ar.array('f')
n_zr = ar.array('f')
n_zq = ar.array('f')
n_ztr = ar.array('f')

for i in range(1000):
    a = normal(100)
    n_mid.append(a.mean())
    n_med.append(statistics.median(a))
    n_zr.append(0.5 * (a[0] + a[len(a) - 1]))
    n_zq.append((np.quantile(a, 0.25) + np.quantile(a, 0.75)) * 0.5)
    n_ztr.append(stats.trim_mean(a, 0.25))

print("Normal n = 100:")
print("Mid:", statistics.mean(n_mid), statistics.variance(n_mid))
print("Med:", statistics.mean(n_med), statistics.variance(n_med))
print("Zr:", statistics.mean(n_zr), statistics.variance(n_zr))
print("Zq:", statistics.mean(n_zq), statistics.variance(n_zq))
print("Ztr:", statistics.mean(n_ztr), statistics.variance(n_ztr))

for i in range(1000):
    a = normal(1000)
    n_mid.append(a.mean())
    n_med.append(statistics.median(a))
    n_zr.append(0.5 * (a[0] + a[len(a) - 1]))
    n_zq.append((np.quantile(a, 0.25) + np.quantile(a, 0.75)) * 0.5)
    n_ztr.append(stats.trim_mean(a, 0.25))

print("Normal n = 1000:")
print("Mid:", statistics.mean(n_mid), statistics.variance(n_mid))
print("Med:", statistics.mean(n_med), statistics.variance(n_med))
print("Zr:", statistics.mean(n_zr), statistics.variance(n_zr))
print("Zq:", statistics.mean(n_zq), statistics.variance(n_zq))
print("Ztr:", statistics.mean(n_ztr), statistics.variance(n_ztr))
