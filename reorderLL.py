class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def split(self, head):
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        return head, second_head
    
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def merge(self, first, second):
        dummy = ListNode()
        current = dummy
        while first and second:
            current.next = first
            first = first.next
            current = current.next
            current.next = second
            second = second.next
            current = current.next
        if first:
            current.next = first
        return dummy.next
    
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        first, second = self.split(head)
        second = self.reverse(second)
        head = self.merge(first, second)
        return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage:
# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
#print("Original Linked List:")
#print_linked_list(head)

head = solution.reorderList(head)

print("Reordered Linked List:")
print_linked_list(head)
