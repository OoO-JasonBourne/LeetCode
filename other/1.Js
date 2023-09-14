var MyQueue = function(){
    // 定义两个栈模拟队列
    // 入栈-stack_in    出栈-stack_out
    this.stack_in = Array()
    this.stack_out = Array()
}

MyQueue.prototype.push = function(x){
    this.stack_in.push(x)
};

MyQueue.prototype.pop = function(){
    if(this.stack_out.length){
        return this.stack_out.pop()
    }
    while(this.stack_in.length){
        const temp = this.stack_in.pop()
        this.stack_out.push(temp)
    }
    return this.stack_out.pop()
}

MyQueue.prototype.peek = function(){
    const temp = this.pop()
    this.stack_out.push(temp)
    return temp
}

MyQueue.prototype.empty = function(){
    return not (this.stack_in.length || this.stack_out.length)
}













