/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
  const arr = [...Array(n).keys()].map(x => x + 1).concat([...Array(n).keys()].map(x => n - 1 - x))
  return arr[time % (2 * (n - 1))]
};