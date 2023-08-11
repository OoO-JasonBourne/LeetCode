while True:
    try:
        s = int(input())
        if s == 0:
            break
        values = list(map(int, input().split()))
        n = values[0]
        values_use = values[1:]
        result = []
        def backTracking(s, startIndex, path, result):
            if sum(path) == s:
                result.append(len(path()[:]))
                return
            for i in range(startIndex, n):
                path.append(values_use[i])
                backTracking(s, i + 1, path, result)
                path.pop()
            return min(result)
        res = backTracking(s, 0, [], result)
        print(s)


    except:
        break
    
