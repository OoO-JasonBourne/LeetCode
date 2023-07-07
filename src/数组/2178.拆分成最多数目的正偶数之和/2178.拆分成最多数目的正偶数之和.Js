var maximumEvenSplit = function(finalSum) {
    if(finalSum % 2 == 1) return [];
    let curNum = 2;
    let res = new Array();
    while(finalSum >= curNum){
        res.push(curNum);
        finalSum -= curNum;
        curNum += 2;
    }
    res[res.length - 1] += finalSum
    return res
};