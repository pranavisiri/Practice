#remove duplicates in LinkedList

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class removeElements(self,head,val):
    temp=Node(0) #dummy node
    temp.next=head
    prev,curr=temp,head

    while curr:
        if curr.val==val:
            prev.next=curr.next
        else:
            prev=curr
        curr=curr.next
    return temp.next
            
        
    
