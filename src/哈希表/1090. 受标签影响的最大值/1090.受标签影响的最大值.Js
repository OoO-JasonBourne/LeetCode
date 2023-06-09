var largestValsFromLabels = function (values, labels, numWanted, useLimit) {
    const n = values.length;
    let coll = new Array();
    for (let i = 0; i < n; i++) {
        coll.push([labels[i], values[i]])
    };
    coll.sort((a, b) => b[1] - a[1])
    res = 0 //最终结果
    hashTable = {} // 构建哈希表存储次数
    for (let i = 0; i < n; i++) {
        // console.log(coll[i])
        if (numWanted == 0) break
        if (coll[i][0] in hashTable == false) {
            res += coll[i][1]
            numWanted--
            hashTable[coll[i][0]] = 1
        } else if (hashTable[coll[i][0]] < useLimit) {
            res += coll[i][1]
            numWanted--
            hashTable[coll[i][0]]++
        }
    }
    return res
};

const values = [5, 4, 3, 2, 1]
const labels = [1, 1, 2, 2, 3]
const numWanted = 3
const useLimit = 1
console.log(largestValsFromLabels(values, labels, numWanted, useLimit))