def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def toDoy(date):
        month = int(date[:2])
        dayOfYear = 0
        for i in range(month - 1):
            dayOfYear += daysOfMonth[i]
        dayOfYear += int(date[3:5])
        return dayOfYear

    # arriveAlice, leaveAlice, arriveBob, leaveBob = toDoy(arriveAlice, toDoy(leaveAlice), toDoy(arriveBob), toDoy(leaveBob)
    arriveAlice = toDoy(arriveAlice)
    leaveAlice = toDoy(leaveAlice)
    arriveBob = toDoy(arriveBob)
    leaveBob = toDoy(leaveBob)

    left, right, res = arriveAlice, arriveBob, 0
    while left <= leaveAlice and right <= leaveBob:
        if left < right:
            left += 1
        elif right < left:
            right += 1
        else:
            res += 1
            left += 1
            right += 1
    return res

arriveAlice = "10-01"
leaveAlice = "10-31"
arriveBob = "11-01"
leaveBob = "12-31"
print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))