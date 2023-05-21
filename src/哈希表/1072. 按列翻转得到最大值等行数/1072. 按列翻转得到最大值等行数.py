def maxEqualRowsAfterFlips(matrix):
    """
    思路：因为反转的是列，所以反转前后每一列的数只有0，1两个选择，即
    第一行 为 0， 0， 1
    第二行 为 1， 1， 0
    那么 只要两行上每一列的数相同或相反，反转过后可得到每行全相等的结果
    因此，我们将 以0开头的行保持不变，将以1开头的行全部反转，如果第一行 == 第二行，那么都两行可以通过反转成为行内元素全相等的行
    那么这道题就变成了计算每一行在矩阵中出现的最大次数
    建立一个哈希表进行统计即可
    :param matrix:
    :return:
    """

    """
    hashMap = {}
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        if matrix[i][0] == 1:
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1
        matrix[i] = str(matrix[i])
        if matrix[i] not in hashMap:
            hashMap[matrix[i]] = 1
        else:
            hashMap[matrix[i]] += 1
    return max(hashMap.values())
    """


    # 简约代码
    hashMap = {}
    for row in matrix:
        if row[0] == 0:
            row = tuple(bit for bit in row)
        else:
            row = tuple(1 - int(bit) for bit in row)
        hashMap[row] = hashMap.get(row, 0) + 1
    return hashMap
