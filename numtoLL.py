class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,num):
        for d in num:
            newnode=Node(d)
            if self.head==None:
                self.head=newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
    def show(self):
        t=self.head
        while t:
            print(t.data,end=",")
            t=t.next
num=input("enter number: ")
obj=MyLinkedList()
obj.createLL(num)
obj.show()
