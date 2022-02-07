import math
import Parameters as Par
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

    if Par.pid1 == 2:
        pid1 = position[0] / s + position[1] * s + position[2]
    elif Par.pid1 == 0:
        pid1 = 0
    elif Par.pid1 == 1:
        pid1 = 1
    else:
        print("Choose a proper pid1 number in Parameters: 0 or 1 or 2")

    if Par.pid2 == 2:
        pid2 = position[3] / s + position[4] * s + position[5]
    elif Par.pid2 == 0:
        pid2 = 0
    elif Par.pid2 == 1:
        pid2 = 1
    else:
        print("Choose a proper pid2 number in Parameters: 0 or 1 or 2")

    if Par.pid3 == 2:
        pid3 = position[6] / s + position[7] * s + position[8]
    elif Par.pid3 == 0:
        pid2 = 0
    elif Par.pid3 == 1:
        pid3 = 1
    else:
        print("Choose a proper pid3 number in Parameters: 0 or 1 or 2")

    Plant = Par.Plant
    # defining the system transfer function
    sys1 = Plant / (1 - Plant * pid3)
    sys2 = sys1 * pid1

    fullSys = sys2 / (1 - sys2 * pid2)

    yStep, tStep = control.step(fullSys, T=14)

    costF = abs(1 - yStep)

    sumCost = scipy.integrate.simps(costF, x=None, dx=14 / len(yStep))

    # plt.plot(t, y)
    # plt.grid()
    # plt.show()
    return sumCost

# xx = np.array((0, 1, 0.12))
# ff = costFunction(xx)
# print(xx)
