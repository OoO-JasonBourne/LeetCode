/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function(num) {
    const newNum = [...String(num)].map(Number).sort((a, b) => a - b);
    let num1 = 0, num2 = 0;
    // for(let i = 0; i < newNum.length; i++){
    //     if(i % 2 == 0){
    //         num1 = num1 * 10 + newNum[i]
    //     } else {
    //         num2 = num2 * 10 + newNum[i]
    //     }
    // }
    newNum.forEach((val, i, arr) => {
        i % 2 === 0 ? num1 = num1 * 10 + val : num2 = num2 * 10 + val
    })
    return num1 + num2
};