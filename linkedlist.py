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
        while i<n:
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

    def show(self,head):
        t=head
        print("list of nodes:")
        s=0
        while t:
            print(t.val,end=" ")
            #s=s+t.val
            t=t.next
        print("\n Total ",s)

#To split the Linked list into two halves
    def split(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None
        print("First Linked List: ")
        self.show(self.head)
        print("second Linked List: ")
        self.show(second)


#To remove duplicate elements in the Linked List
    def removeElement(self,head,val):
        temp=Node(0) #temp=ListNode(0)
        temp.next=head
        prev, curr=temp,head
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return temp.next

    #reverse of linked list
    def reverseLL(self,head):
        prev=None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev

"""##palindrome Linked List
    def isPalindrome(self,head):
        if head is None:
            return True
    #split into two parts
    slow=head
    fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next

    #reversing second part
    prev=None
    curr=slow*
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp

    #check node by node for palindrome
    first=head
    second=prev*
    while second:
        if first.val != second.val:
            return False
        first=first.next
        second=second.next
    return True

    #Middle of LL
    def middleNode(self,head):
        tmp=head
        while tmp and tmp.next:
            head=head.next
            tmp=tmp.next.next
        return head

    #delete node in LL
    def deleteNode(self,node):
        node.val=node.next.val
        node.next=node.next.next

    #Odd Even LL
    def oddEvenLL(self,head):
        head1=odd=ListNode()
        head2=odd=ListNode()
        t=head
        i=0
        while t:
        """
            
obj=LinkedList()
n=int(input("Enter n: "))
obj.createLL(n)
obj.show(obj.head)
#obj.split()

#val=int(input("Enter val"))
#obj.head=obj.removeElement(obj.head,val)
#print("\nAfter deleting: ")
#obj.show(obj.head)

obj.head=obj.reverseLL(obj.head)
print("\nReversed LL")
obj.show(obj.head)

#obj.head=obj.isPalindrome(obj.head)
#print("Palindrome or not: ")
#obj.show(obj.head)

#obj.head=obj.middleNode(obj.head)
#print("Middle node is: ")
#obj.middleNode(obj.head)


            
