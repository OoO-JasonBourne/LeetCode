/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let solve = 1; mix = 0;
    for(let i of String(n)){
        solve *= parseInt(i);
        mix += parseInt(i)
    }
    return solve - mix
};