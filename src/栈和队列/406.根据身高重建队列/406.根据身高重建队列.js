/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    people.sort((a, b) => {
        if(a[0] === b[0]){
            return a[1] - b[1]
        } else {
            return b[0] - a[0]
        }
    })
    const res = Array();
    for(let i = 0; i < people.length; i++){
        const resLen = res.length;
        if(people[i][1] >= resLen){
            res.push(people[i])
        } else {
            res.splice(people[i][1], 0, people[i])
        }
    }
    return res;
};