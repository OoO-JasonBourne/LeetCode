# LinkList 链表

### 构建虚拟头节点
dummy_head = ListNode(next = head)

### 获取链表长度
在Python中，链表对象本身没有内置的函数来获取链表的长度，需要自己编写代码 
###### def get_length(self): 
###### &emsp;&emsp;   count = 0
###### &emsp;&emsp;   current = self.head
###### &emsp;&emsp;   while current is not None:
###### &emsp;&emsp;&emsp;&emsp;      count += 1
###### &emsp;&emsp;&emsp;&emsp;       current = current.next
###### &emsp;&emsp;   return count