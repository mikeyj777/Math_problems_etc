# frog on a bank of a river with 9 lily pads to cross the river to get to the other side.
# what is the expected number of jumps for the frog to make it across?
# is there a general formula for n lily pads?

import random
import matplotlib.pyplot as plt
import numpy as np


def jumper(spacesleft=20, numjumps=0):
    if spacesleft <= 0:
        return numjumps

    jump = random.randint(1, spacesleft)
#     print("spaces left: ", spacesleft, ". jump: ",
#           jump, "num jumps: ", numjumps + 1)
    return jumper(spacesleft - jump, numjumps + 1)


def looper(epochs=1000, spacesleft=20):
    spaces = 3
    meansvsspaces = []
    while spaces <= spacesleft:
        alljumps = []
        i = 1
        while i <= epochs:
            #         print("_______")
            currjumps = jumper(spacesleft=spaces, numjumps=0)
            alljumps.append(currjumps)
            i += 1
        meansvsspaces.append([spaces, np.mean(alljumps)])
        spaces += 1

    return meansvsspaces


a = looper()
a = np.asarray(a)
# print(np.mean(a))
print(a)
plt.plot(a[:, 0], a[:, 1])
plt.show()
