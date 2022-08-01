class Node():
    
    def __init__(self,val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 0
        self.hashSetHead = Node(None)

    def add(self, key: int) -> None:
        if not self.hashSetHead:
            self.hashSetHead(key)
        elif MyHashSet.contains(self,key):
            pass
        else:
            temp = self.hashSetHead
            self.hashSetHead = Node(key)
            self.hashSetHead.next = temp
            
            

    def remove(self, key: int) -> None:
        if self.hashSetHead:
            temp = self.hashSetHead
        if temp.val == key:
            self.hashSetHead = temp.next
            return
        while temp:
            if temp.val == key:
                break
            prev = temp
            temp = temp.next
            
        if not temp:
            return 
        
        prev.next = temp.next
        

    def contains(self, key: int) -> bool:
        temp = self.hashSetHead
        while temp:
            if temp.val == key:
                return True
            temp = temp.next
        return False
        

# Your MyHashSet object will be instantiated and called as such:
#obj = MyHashSet()
#obj.add(3)
#obj.remove(3)
# param_3 = obj.contains(key)
