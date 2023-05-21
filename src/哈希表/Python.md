###
###### 
在Python中，可以使用字典（Dictionary）数据结构来构建哈希表。
字典是一种无序的键值对集合，其中每个键对应一个值。键必须是唯一的，而值可以重复。
######
哈希表（Hash Table）是一种根据键（Key）直接访问值（Value）的数据结构，它通过哈希函数将键映射到哈希表中的位置。在Python中，哈希表的实现是字典（Dictionary），用花括号{}表示。字典中的每个元素由键和对应的值组成，键和值之间使用冒号:分隔，键值对之间使用逗号分隔。
hash_map = {"key1": value1, "key2": value2, "key3": value3}
{1, 2, 3}表示的是一个集合（Set）
集合是一种无序且不重复的数据结构，它的主要特点是元素之间没有顺序关系，并且保证元素的唯一性。集合用花括号{}表示，其中的元素用逗号分隔。在集合中，元素的存储顺序与添加顺序无关
######
在Python的字典中，添加键值对的操作是使用赋值操作符=，
###### 
哈希表set(),set添加数据为 set.add()
######
数组添加为 nums.append()

###### 
定义一个无穷大的数  x = float('inf')
       无穷小     x = float('-inf')

###### 
排序： nums.sort()
添加： nums.append()

### 构建哈希表
hashTable = {}
### 查询哈希表中相同字符串的最大数目
max(hashTable.values())
### 哈希表计数
if item not in hashTable:
    hashTable[item] = 1
else:
    hashTable[item] += 1

### for循环遍历矩阵
for row in matrix:
    for item in row:
        ...
### 列表 list 转字符串 str
str = ''.