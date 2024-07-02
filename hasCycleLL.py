def hasCycle(self):
    if self.head==None:
        return False
    slow=self.head
    fast=self.head.next
    while slow!=fast:
        slow=slow.next
        fast=fast.next.next
        if fast==None or fast.next==None:
            return False
    return True
        
