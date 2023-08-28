const tests = [
    {input: 33},
    {input: 1234.56},
    {input: 123456789},
    {input: 987654.321},
    {input: -987654.3},
]

function paddingNum(tests){
    for(let test of tests){
        const num = test["input"]
        const formatNum = num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        test["output"] = formatNum
    }
    return tests
}

result = paddingNum(tests)
console.log(result)
// a = {input:33}
// console.log(a["input"])