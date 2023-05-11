var queryString = function(s, n) {
    for(let i = 1; i <= n; i++){
        binaryNum = i.toString(2);
        if(!s.includes(binaryNum)){
            return false
        }
    }
    return true
};