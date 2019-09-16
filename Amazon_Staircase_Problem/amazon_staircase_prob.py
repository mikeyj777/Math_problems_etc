moves = 0


def move(stepstotop, allowablesteps, currresult=[], resultlist=[]):
    if stepstotop == 0 or len(allowablesteps) == 0:
        resultlist.append(currresult[:])
        print(currresult)
#         currresult = []
        return resultlist[:]

    for i in allowablesteps:
        if i <= stepstotop:
            stepstotop -= i
            currresult.append(i)
            resultlist = move(
                stepstotop, allowablesteps[:], currresult[:], resultlist[:])
            currresult.pop(len(currresult) - 1)
            stepstotop += i

    return resultlist[:]


a = move(10, [1, 4, 8, 15])

print(len(a), a)
