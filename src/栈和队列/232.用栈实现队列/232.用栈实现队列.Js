
var MyQueue = function() {
    this.stack_in = [];
    this.stack_out = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.stack_in.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    const size = this.stack_out.length
    if(size){
        return this.stack_out.pop()
    };
    // if(this.stack_in == []) return;
    while(this.stack_in.length){
        let temp = this.stack_in.pop();
        this.stack_out.push(temp);
    }
    return this.stack_out.pop()
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    const x = this.pop();
    this.stack_out.push(x)
    return x
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return !this.stack_in.length && !this.stack_out.length
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */



// var MyQueue = function(){
//     // 定义两个栈模拟队列
//     // 入栈-stack_in    出栈-stack_out
//     this.stack_in = Array()
//     this.stack_out = Array()
// }
//
// MyQueue.prototype.push = function(x){
//     this.stack_in.push(x)
// };
//
// MyQueue.prototype.pop = function(){
//     if(this.stack_out.length){
//         return this.stack_out.pop()
//     }
//     while(this.stack_in.length){
//         const temp = this.stack_in.pop()
//         this.stack_out.push(temp)
//     }
//     return this.stack_out.pop()
// }
//
// MyQueue.prototype.peek = function(){
//     const temp = this.pop()
//     this.stack_out.push(temp)
//     return temp
// }
//
// MyQueue.prototype.empty = function(){
//     return !this.stack_in.length && !this.stack_out.length
// }
//
//
//
// /**
//  * Your MyQueue object will be instantiated and called as such:
//  * var obj = new MyQueue()
//  * obj.push(x)
//  * var param_2 = obj.pop()
//  * var param_3 = obj.peek()
//  * var param_4 = obj.empty()
//  */
