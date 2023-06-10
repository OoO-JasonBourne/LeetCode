var numSmallerByFrequency = function (queries, words) {
    var f = function (s) {
        let minS = 'z'; 
        let count = 0;
        for (let _ of s) {
            if (_ < minS) {
                minS = _
                count = 1
            } else if (_ == minS) {
                count++
            }
        }
        return count
    };

    // let sortedWords = words.map(function (m) {
    //     return f(m)
    // }).sort();
    for (let j = 0; j < words.length; j++) {
        words[j] = f(words[j]);
    }
    words.sort(function(a, b) {
        return b - a;
    });
    let res = new Array(queries.length).fill(0);
    for (let i = 0; i < queries.length; i++) {
        queries[i] = f(queries[i]);
        for (let j = 0; j < words.length; j++) {
            if (queries[i] >= words[j]) {
                break;
            }
            res[i]++;
        }
    }
    return res
};
const queries =["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]; words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"];
console.log(numSmallerByFrequency(queries, words))