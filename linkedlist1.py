class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(30)
def show(head):
    t=head
    while(t):
        print(t.data,end=",")
        t=t.next
show(head)
def find(head):
    t=set()
    flag=1
    h=head
    while(h):
        if h.data in t:
            print(h.data,"duplicate found")
            flag=0
        else:
            t.add(h.data)
        h=h.next
    if flag==1:
        print("no duplicates")
find(head)
def split(head):
    slow=fast=head
    while fast and fast.next:
        fast=fast.next.next
        prev=slow
        slow=slow.next
    prev.next=None
    second=slow
split(head) 
