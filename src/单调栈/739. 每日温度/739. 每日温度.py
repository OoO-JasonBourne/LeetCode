def dailyTemperatures(temperatures):
    # 暴力解法： 超时
    # ans = [0] * len(temperatures)
    # for i in range(len(temperatures)):
    #     j = i + 1
    #     while j < len(temperatures):
    #         diff = temperatures[j] - temperatures[i]
    #         if diff > 0:
    #             ans[i] = j - i
    #             break
    #         else:
    #             j += 1
    # return ans
    stack = []
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        if stack != [] and temperatures[stack[-1]] < temperatures[i]:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
        while len(stack) > 1 and temperatures[stack[-1]] > temperatures[stack[-2]]:
            res[stack[-2]] = stack[-1] - stack[-2]
            curr = stack.pop()
            stack.pop()
            stack.append(curr)
    return res

