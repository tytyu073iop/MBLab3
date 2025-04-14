from thomas import thomas
import math

def splain(func, a, b, n, x):
    n += 1
    
    moments = [0] * n

    def dFunc2(x):
        return pow(math.e, math.cos(x)) * (-math.sin(x)) * math.cos(x) + pow(math.e, math.cos(x)) * (-math.cos(x))
    
    moments[0] = dFunc2(a)
    moments[n - 1] = dFunc2(b)

    hs = [0] * n
    xs = [0] * n
    deltas = [0] * n
    diff = (b - a) / (n - 1)
    xs[0] = a
    for i in range(1, n):
        xs[i] = a + diff * i
        hs[i] = diff
        deltas[i] = func(xs[i]) - func(xs[i - 1])

    a = [0] * (n - 2)
    b = [0] * (n - 2)
    c = [0] * (n - 2)
    d = [0] * (n - 2)
    b[0] = (hs[1] + hs[2]) / 3
    c[0] = hs[2] / 6
    d[0] = deltas[2] / hs[2] - deltas[1] / hs[1] - (hs[1] * moments[0]) / 6 
    for i in range(2, n - 2):
        a[i - 1] = hs[i] / 6
        b[i - 1] = (hs[i] + hs[i + 1]) / 3
        c[i - 1] = hs[i + 1] / 6
        d[i - 1] = deltas[i + 1] / hs[i + 1] - deltas[i] / hs[i]
    a[n - 3] = hs[n - 2] / 6
    b[n - 3] = (hs[n - 2] + hs[n - 1]) / 3
    d[n - 3] = deltas[n - 1] / hs[n - 1] - deltas[n - 2] / hs[n - 2] - (hs[n - 1] * moments[n - 1]) / 6

    moments[1 : n - 1] = thomas(a, b, c, d)

    i = 1
    while (True):
        if (x <= xs[i] and x >= xs[i - 1]):
            break
        else:
            i += 1

    return moments[i - 1] * pow(xs[i] - x, 3) / (6 * hs[i]) + moments[i] * pow(x - xs[i - 1], 3) / (6 * hs[i]) + (func(xs[i - 1]) - pow(hs[i],2) / 6 * moments[i - 1]) * (xs[i] - x) / hs[i] + (func(xs[i]) - pow(hs[i],2) / 6 * moments[i]) * (x - xs[i - 1]) / hs[i]