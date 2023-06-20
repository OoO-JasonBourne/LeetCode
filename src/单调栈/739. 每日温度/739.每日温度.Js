var dailyTemperatures = function (temperatures) {
    var stack = [];
    const n = temperatures.length;
    let res = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && temperatures[stack[stack.length - 1]] < temperatures[i]) {
            let cur = stack.pop()   // 将栈顶元素弹出，并用cur记录下标
            res[cur] = i - cur
        }
        stack.push(i)
    }
    return res
};

