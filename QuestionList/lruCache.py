class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, capacity):
        self.length = 0
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addToFront(self, node):
        self.length += 1
        nextNode = self.head.next
        node.next = nextNode
        nextNode.prev = node
        self.head.next = node
        node.prev = self.head
        if self.length > self.capacity:
            return self.removeFromBack()
        return -1
    
    def removeFromBack(self):
        if self.length > 0:
            nodeToRemove = self.tail.prev
            self.removeNode(nodeToRemove)
            return self.getNodeKey(nodeToRemove)
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.length -= 1
    
    def updateNode(self, node, val):
        node.value = val
    
    def getNodeVal(self, node):
        return node.value
    
    def getNodeKey(self, node):
        return node.key
    
class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMapping = {}
        self.linkedList = LinkedList(capacity)

    def get(self, key: int) -> int:
        if key not in self.nodeMapping:
            return -1
        
        value = self.linkedList.getNodeVal(self.nodeMapping[key])
        self.linkedList.removeNode(self.nodeMapping[key])
        self.linkedList.addToFront(self.nodeMapping[key])
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMapping:
            self.linkedList.updateNode(self.nodeMapping[key], value)
            self.linkedList.removeNode(self.nodeMapping[key])
            self.linkedList.addToFront(self.nodeMapping[key])
        else:
            newNode = ListNode(key, value)
            self.nodeMapping[key] = newNode
            keyToRemove = self.linkedList.addToFront(newNode)
            if keyToRemove != -1:
                del self.nodeMapping[keyToRemove]
