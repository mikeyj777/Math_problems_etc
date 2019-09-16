# frog on a bank of a river with 9 lily pads to cross the river to get to the other side.
# what is the expected number of jumps for the frog to make it across?
# is there a general formula for n lily pads?

import random


def jumper(spacesleft=10, numjumps=0):
    if spacesleft <= 0:
        return numjumps

    jump = random.randint(1, spacesleft)

    jumper(spacesleft - jump, numjumps + 1)

    return None


def looper(epochs=10):
    alljumps = []
    currjumps = jumper()
    alljumps.append(currjumps)
