# coding: utf-8

# Bare bones fireworks algorithm
# https://www.sciencedirect.com/science/article/pii/S1568494617306609
# by Junzhi Li
# ljz@pku.edu.cn
from numpy import *


# sphere function
def f(x):
    return sum(x * x, 0)


dim = 10
maxeval = 300000
lb = 0 * ones((dim, 1))  # upper bound vector of the search space
ub = 360 * ones((dim, 1))  # lower bound vector of the search space
n = 2  # a constant parameter which controls the total number of explosion sparks in one generation
Cr = 0.9  # reduction coefficient
Ca = 1.2  # amplification coefficient
A = ub - lb
x = random.rand(dim, 1) * (ub - lb) + lb
fx = f(x)
eval = 1
while eval < maxeval:
    s = (random.rand(dim, n) * 2 - 1) * tile(A, (1, n)) + tile(x, (1, n))

    # boundary handling
    # for i in range(dim):
    #    index = logical_or(s[i,:] > ub[i], s[i,:] < lb[i])
    #    s[i,index] = random.rand(1,sum(index)) * (ub[i] - lb[i]) + lb[i];
    fs = f(s)
    eval = eval + n
    if min(fs) < fx:
        print("s:" + str(s.min()))
        x = s[:, argmin(fs)].reshape(dim, 1)
        fx = min(fs)
        A = A * Ca
        print(fx)
    else:
        A = A * Cr
print(fx)
