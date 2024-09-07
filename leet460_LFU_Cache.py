# Dictionary and Doubly Linked List
class LFUCache:
    class node:
        def __init__(self,prev,next,key):
            self.prev = prev
            self.next = next
            self.key = key

    class doublyLinkedList:
        def __init__(self):
            self.head = LFUCache.node(None,None,None)
            self.tail = LFUCache.node(None,None,None)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        
        def insertAtHead(self,node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1
        
        def deleteAtTail(self):
            toBeDeleted = self.tail.prev
            toBeDeleted.prev.next = self.tail
            self.tail.prev = toBeDeleted.prev
            self.size -= 1
            return toBeDeleted
        
        def deleteANode(self,node):
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1

    def __init__(self, capacity: int):
        self.LFUCache = {}
        self.LFUll = {}
        self.capacity = capacity
        self.min = 0
    
    def increaseFrequency(self,key):
        curFreq = self.LFUCache[key][1]
        curNode = self.LFUCache[key][2]
        tempDll = self.LFUll[curFreq]
        tempDll.deleteANode(curNode)
        if tempDll.size <= 0:
            del self.LFUll[curFreq]
            if curFreq == self.min:
                self.min += 1
        
        curFreq += 1
        if curFreq in self.LFUll:
            tempDll = self.LFUll[curFreq]
        else:
            tempDll = self.doublyLinkedList()
            self.LFUll[curFreq] = tempDll
        
        self.LFUCache[key][1] = curFreq
        
        tempDll.insertAtHead(curNode)

    def get(self, key: int) -> int:
        if key in self.LFUCache:
            self.increaseFrequency(key)
            return self.LFUCache[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.LFUCache and len(self.LFUCache) == self.capacity:
            minLl = self.LFUll[self.min]
            tempNodeP = minLl.head
            lruNode = minLl.deleteAtTail()
            del self.LFUCache[lruNode.key]
            if minLl.size == 0:
                del self.LFUll[self.min]
                self.min += 1

        if key in self.LFUCache:
            self.LFUCache[key][0] = value
            self.increaseFrequency(key)
        else:
            self.min = 1
            curNode = self.node(None,None,key)
            self.LFUCache[key] = [value,1,curNode]

            if 1 in self.LFUll:
                tempDll = self.LFUll[1]
            else:
                tempDll = self.doublyLinkedList()
                self.LFUll[1] = tempDll
            
            tempDll.insertAtHead(curNode)

# Time Limit exceeds for below solution(Dictionary and Priority Queue)
# class LFUCache:
    # class node:
    #     def __init__(self,label,lfu,lru):
    #         self.label = label
    #         self.lfu = lfu
    #         self.lru = lru
        
    #     def __lt__(self,other):
    #         if self.lfu == other.lfu:
    #             return self.lru < other.lru
    #         else:
    #             return self.lfu < other.lfu
            

#     def __init__(self, capacity: int):
#         self.LFUCache = {}
#         self.LFUUsed = {}
#         self.oprCount = 0
#         self.capacity = capacity
        

#     def get(self, key: int) -> int:
#         self.oprCount += 1
#         if key in self.LFUCache:
#             self.LFUUsed[key][0] += 1
#             self.LFUUsed[key][1] = self.oprCount
#             return self.LFUCache[key]
#         else:
#             return -1
        

#     def put(self, key: int, value: int) -> None:

#         if key not in self.LFUCache and len(self.LFUCache) == self.capacity:
#             # Remove the lfu or lru
#             heap = []
#             for keyTemp,item in self.LFUUsed.items():
#                 heapq.heappush(heap,self.node(keyTemp,item[0],item[1]))
            
#             nodeTemp = heapq.heappop(heap)
#             del self.LFUCache[nodeTemp.label]
#             del self.LFUUsed[nodeTemp.label]

#         self.oprCount += 1
#         if key in self.LFUCache:
#             self.LFUCache[key] = value
#             self.LFUUsed[key][0] += 1
#             self.LFUUsed[key][1] = self.oprCount
#         else:
#             self.LFUCache[key] = value
#             self.LFUUsed[key] = []
#             self.LFUUsed[key].append(1)
#             self.LFUUsed[key].append(self.oprCount)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)