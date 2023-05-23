// // 闭包


var createCounter = function(n) {
    return function() {
        return n++
    }
}

 
const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12

// console.log(counter++)   // 报错

/**
 * var add = (function(){
 *      let counter = 10;
 *      return function(){
 *          return(++counter);
 *     }
 *  })();      //这里add已经是执行过后的函数了。即add指定了函数自我调用的返回值
 *  console.log(add());   //counter为1
 *  console.log(add());   //counter为2
 *  console.log(add());   //counter为3
 */
