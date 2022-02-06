import math

import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
import scipy

k = 1
tt = 0.5
a = 2
b = 1


# constants


# end_constants


# plant presentation


def costFunction(position):
    # defining the pid functions
    s = control.tf('s')

    U = 1 / s
    pid1 = position[0] / s + position[1] * s + position[2]
    # pid2 = position[3] / s + position[4] * s + position[5]
    # pid3 = position[6] / s + position[7] * s + position[8]

    Plant = 1 / (s ** 2 + 10 * s + 20)
    # defining the system transfer function

    fullSys = Plant * pid1 / (1 + Plant * pid1)
    controlEffort = pid1 / (1 + Plant * pid1)
    y, t = control.step(fullSys, T=14)
    sumCostEffort = 0

    u, t1 = control.step(Plant, T=14)
    costFE = abs(u)
    sumCostEffort = scipy.integrate.simps(costFE, x=None, dx=14 / len(u))
    costF = abs(1 - y)

    sumAll = 0
    sumCost = 0

    sumCost = scipy.integrate.simps(costF, x=None, dx=14 / len(y))

    sumAll = sumCost + sumCostEffort
    plt.plot(t1, u)
    plt.plot(t, y)
    plt.grid()
    plt.show()
    return rev


xx = np.array((0, 1, 0.12))
ff = costFunction(xx)
print(xx)
