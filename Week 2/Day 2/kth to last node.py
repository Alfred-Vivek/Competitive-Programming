def kth_to_last_node(k, head):
    if k == 0:
        raise ValueError('k cant be 0')    
    if k > len(head.get_values()):
        raise ValueError('k cant be greater than length of the list')
    x = head
    i = 0
    while head and head.next:
        head = head.next
        if i == k-1:
            x = x.next
        else:
            i += 1
    return x

# Test Cases
class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

fourth = LinkedListNode(4)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)

def test_first_to_last_node():
    actual = kth_to_last_node(1, first)
    expected = fourth
    print(actual == expected)

def test_second_to_last_node():
    actual = kth_to_last_node(2, first)
    expected = third
    print(actual == expected)

def test_first_node():
    actual = kth_to_last_node(4, first)
    expected = first
    print(actual == expected)

test_first_to_last_node()
test_second_to_last_node()
test_first_node()