'''
Author: Vincent
Date: 2021-02-11 18:13:07
LastEditors: Vincent
LastEditTime: 2021-02-11 22:15:11
Description: file content
'''
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

class Node:
    def __init__(self, key, val) -> None:
        self.next = None
        self.prev = None

        self.key = key
        self.val = val

class DoubleList:

    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x: Node):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def removeNode(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev

        self.size -= 1

    def removeFirst(self) -> Node:
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.removeNode(first)
        return first

    def getSize(self):
        return self.size
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = dict()
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deleteKey(key)
            self.addRecently(key, value)
            return
        
        if self.cap == self.cache.getSize():
            self.removeLeastRecently()

        self.addRecently(key, value)


    def makeRecently(self, key):
        x = self.map[key]
        self.cache.removeNode(x)
        self.cache.addLast(x)

    def addRecently(self, key, val):
        x = Node(key, val)
        self.cache.addLast(x)
        self.map[key]= x

    def deleteKey(self, key):
        x = self.map[key]
        self.cache.removeNode(x)
        self.map.pop(key)

    def removeLeastRecently(self):
        deletedNode = self.cache.removeFirst()
        self.map.pop(deletedNode.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == '__main__':
    lRUCache = LRUCache(2);
    lRUCache.put(1, 1); # 缓存是 {1=1}
    lRUCache.put(2, 2); # 缓存是 {1=1, 2=2}
    print(lRUCache.get(1));    # 返回 1
    lRUCache.put(3, 3); # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(lRUCache.get(2));    # 返回 -1 (未找到)
    lRUCache.put(4, 4); # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(lRUCache.get(1));    # 返回 -1 (未找到)
    print(lRUCache.get(3));    # 返回 3
    print(lRUCache.get(4));    # 返回 4
    print(lRUCache)
    