def camelMatch(queries, pattern):
    n = len(queries)
    res = [True] * n
    for i in range(n):
        object = queries[i]
        left = right = 0
        while left < len(object) and right < len(pattern):
            if object[left] == pattern[right]:
                left += 1
                right += 1
            else:
                if object[left].islower():
                    left += 1
                else:
                    res[i] = False
                    break
        if res[i] != False:
            qq = i
            ss = n
            for i in range(left, n):
                if object[i].isupper():
                    res[i] = False
                    break

    return res
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"

print(camelMatch(queries, pattern))