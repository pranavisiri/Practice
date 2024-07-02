class Node:
    def __init__(self,d):
        self.data=d
        self.next=None



class numLL:
    def __init__(self):
        self.head=None

    def createLL(self,num):
        i=0
        while i<num:
            val=int(input("enter a val: "))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                if t.next!=None:
                    t=t.next
                t.next=new_node
            i=i+1

    def show(self,head):
        t=head
        print("\n List of nodes: ")
        while t:
            print(t.val,end=" ")
            t=t.next

    def rev_show(self,head):
        if (head==None):
            return
        else:
            self.rev_show(head.next)
            print(





def addLL(head,head2):
    head=None
    curr1=head1
    curr2=head2
    c=0
    while(curr1 and curr2):
        sum=c+curr1.val+curr2.val
        c=0
        if sum>9:
            c=1
            sum=sum%10
        new_node=Node(sum)

        if not head:
            head=new_node
            prev=head
        else:
            prev.next=new_node
            prev=new_node

        curr1=curr1.next
        curr2=curr2.next
    return head

list1=numLL()
head1=list1.createLL("23")
list1.show(head1)
print("\n")
list2=numLL()
head2list2.createLL("58")
print("\n")
list2.show(head2)

sum_head=addLL(head1,head2)
print("\n")
list1.rev_show(sum_head)











        
        
