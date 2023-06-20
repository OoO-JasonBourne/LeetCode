## 单调栈
### 定义栈 
stack = []

### 取栈顶元素
stack[-1]

### 取栈底元素
stack[0]

### 进栈
stack.append(i)

### 出栈
stack.pop()

### 获取字典键和值
1. keys()、 values()

my_dict = {0: 1} \
keys = list(my_dict.keys())[0] \
values = list(my_dict.values())[0] \
print(keys)   # 输出 0 \
print(values) # 输出 1

2. 使用循环遍历字典的键和值

my_dict = {0: 1} \
for key, value in my_dict.items(): \
    keys = key \
    values = value \
print(keys)   # 输出 0 \
print(values) # 输出 1

3. 通过字典索引获取键和值

my_dict = {0: 1}  \
keys = list(my_dict)[0]  \
values = my_dict[keys] \
print(keys)   # 输出 0 \
print(values) # 输出 1




