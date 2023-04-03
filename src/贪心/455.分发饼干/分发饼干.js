var findContentChildren = function(g, s) {
    g.sort((a, b) => (a - b))
    s.sort((a, b) => (a - b))
    let i = 0; j = 0; res = 0;
    while(i < g.length && j < s.length){
        if(g[i] <= s[j]){
            res++;
            i++;
            j++;
        } else {
            j++
        }
    }
    return res
};