def maximumEvenSplit(finalSum):
    res = []
    i = 1
    while finalSum > 0 and finalSum not in res:
        finalSum -= 2 * i
        res.append(2 * i)
        i += 1




    res[0] += finalSum
    return res


finalSum = 28
print(maximumEvenSplit(finalSum))
