class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list_from_number(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    # Initialize the head of the linked list
    head = ListNode()
    current = head
    # Iterate through each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer
        digit_val = int(digit)
        # Create a new node for this digit
        new_node = ListNode(digit_val)
        # Link the current node to the new node
        current.next = new_node
        # Move the current pointer to the new node
        current = current.next
    # Return the head of the linked list, excluding the initial empty node
    return head.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
number = int(input("Enter a number: "))
linked_list = create_linked_list_from_number(number)
print_linked_list(linked_list)
