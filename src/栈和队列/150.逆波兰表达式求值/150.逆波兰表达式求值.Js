/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    // 新建一个空栈
    const stack = []
    for(let item of tokens){
        if(!'+-*/'.includes(item)){
            stack.push(Number(item))
        } else {
            right = stack.pop();
            left = stack.pop();
            stack.push(calc(left, right, item))
        }
    }
    return stack[0]
};

function calc(left, right, simple){
    switch(simple){
        case '+':
            return left + right;
        case '-':
            return left - right;
        case '*':
            return left * right;
        case '/':
            return parseInt(left / right);
        default:
            throw new Error("Error")
    }
}