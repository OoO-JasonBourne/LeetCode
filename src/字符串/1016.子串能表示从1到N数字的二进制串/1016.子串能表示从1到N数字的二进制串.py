def queryString(s, n):
    for i in range(1, n + 1):
        if bin(i)[2:] not in s: return False
    return True

s, n = "0110", 3
print(queryString(s, n))