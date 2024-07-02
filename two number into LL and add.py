class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def createLL(self, num):  
        for d in num:
            newnode = Node(int(d))
            if self.head is None:
                self.head = newnode
            else:
                t = self.head
                while t.next:
                    t = t.next
                t.next = newnode

    def show(self):
        t = self.head
        while t:
            print(t.data, end=",")
            t = t.next

    def addLinkedLists(self, list1, list2):
        carry = 0
        result = MyLinkedList()
        p1 = list1
        p2 = list2
        while p1 or p2:
            val1 = p1.data if p1 else 0
            val2 = p2.data if p2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            result.createLL(str(total % 10))
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry > 0:
            result.createLL(str(carry))
        return result

# Take two numbers as input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Create linked lists for each number
list1 = MyLinkedList()
list1.createLL(num1)
list2 = MyLinkedList()
list2.createLL(num2)

# Add the linked lists representing the numbers
result = list1.addLinkedLists(list1.head, list2.head)

# Display the result
result.show()
