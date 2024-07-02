class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
#To create a Linked List
    
    def createLL(self,n):
        i=0
        ctr=0
        while i<n and ctr<5:
            val=int(input("Enter data:"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new_node
            i=i+1
        new_node.next=self.head
        ctr=ctr+1

            
    def show(self,head):
        t=head
        print("list of nodes:")
        s=0
        while t:
            print(t.val,end=" ")
            t=t.next

    """def show(self):
        i=0
        curr=self.head
        while i<100:
            print(curr.val,end="-->")
            curr=curr.next
            i+=1"""

obj=LinkedList()
n=int(input("Enter n: "))
obj.createLL(n)
obj.show(obj.head)
#obj.show()
