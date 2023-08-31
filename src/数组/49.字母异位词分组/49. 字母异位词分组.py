def groupAnagrams(strs):
    """
    计数 + 哈希
    """
    # n = len(strs)
    # strs_record = []
    # for strSingle in strs:
    #     str_record = [0] * 26
    #     for _ in strSingle:
    #         str_record[ord(_) - ord('a')] += 1
    #     strs_record.append(str_record)
    # hashTable = {}
    # for i in range(n):
    #     hashTable[str(strs_record[i])] = []
    # for i in range(n):
    #     hashTable[str(strs_record[i])].append(strs[i])
    # return list(hashTable.values())

    # 精简版     计数 + 哈希
    # res = collections.defaultdict(list)
    # for st in strs:
    #     count = [0] * 26
    #     for s in st:
    #         count[ord(s) - ord('a')] += 1
    #     res[tuple(count)].append(st)
    # return list(res.values())

    """
    排序 + 哈希
    """
    res = collections.defaultdict(list)

    for st in strs:
        key = ''.join(sorted(st))
        res[key].append(st)
    return list(res.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
