## JS建立哈希表
### hashMap = new Set()
### hashMap = new Map()
### let hashTable = {} 


## 循环元素
for(let item of items):

## 哈希表操作
### 修改值
hashTable['key1'] = 'new value1';

### 删除值
delete hashTable['key2'];

### 检查键是否存在
console.log('key1' in hashTable); // 输出: true \
console.log('key2' in hashTable); // 输出: false

### 获取哈希表的键数组
const keys = Object.keys(hashTable); \
console.log(keys); // 输出: ['key1', 'key3']

### 数组排序
###### 使用 Array.sort() 方法来对二维数组按照内部数组的第二个元素进行反向排序
arr.sort((a, b) => b[1] - a[1]);

### 判断一个元素是否存在于哈希表的键中
1. "key" in hashTable
2. Object.keys(hashTable).includes("key")
3. hashTable.hasOwnProperty("key")

