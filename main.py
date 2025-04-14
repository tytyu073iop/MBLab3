import matplotlib.pyplot as plt
from splain import splain
import math

def func(x):
    return pow(math.e, math.cos(x))

n = 100
xs = [0] * n
a = -3
b = 3
for i in range(0,n):
    xs[i] = a + i * (b - a) / n

fss = [0] * n
fs = [0] * n
max = 0
for i in range(0,n):
    fss[i] = splain(func, a, b, 15, xs[i])
    fs[i] = func(xs[i])
    if (max < abs(fss[i] - fs[i])):
        max = abs(fss[i] - fs[i])

print(f"max pog: {max}")

fig, ax = plt.subplots()
ax.plot(xs, fss, label="splain")
ax.plot(xs, fs, label="function")
ax.legend()
plt.show()
