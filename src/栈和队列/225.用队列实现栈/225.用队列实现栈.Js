var MyStack = function() {
    // 新建两个队列, 一个主队列，一个副（备份）队列
    this.queue_main = Array();
    this.queue_backup = Array();
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    this.queue_main.push(x)
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    let temp = this.queue_main.shift();
    while(this.queue_main.length){
        this.queue_backup.push(temp);
        temp = this.queue_main.shift();
    }
    while(this.queue_backup.length){
        const temp2 = this.queue_backup.shift();
        this.queue_main.push(temp2);
    }
    return temp;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    const temp = this.pop();
    this.queue_main.push(temp);
    return temp;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return !this.queue_main.length;
};


/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */