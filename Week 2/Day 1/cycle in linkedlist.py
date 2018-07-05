def contains_cycle(first_node):
    x = first_node
    y = first_node    
    while x and x.next and x.next.next:
        x = x.next
        y = y.next.next        
        if x is y:
            return True        
    return False

# Test Cases

class LinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

def test_linked_list_with_no_cycle():
    fourth = LinkedListNode(4)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    result = contains_cycle(first)
    print(result == False)

def test_cycle_loops_to_beginning():
    fourth = LinkedListNode(4)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    fourth.next = first
    result = contains_cycle(first)
    print(result == True)

def test_cycle_loops_to_middle():
    fifth = LinkedListNode(5)
    fourth = LinkedListNode(4, fifth)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    fifth.next = third
    result = contains_cycle(first)
    print(result == True)

def test_two_node_cyle_at_end():
    fifth = LinkedListNode(5)
    fourth = LinkedListNode(4, fifth)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)
    fifth.next = fourth
    result = contains_cycle(first)
    print(result == True)

def test_empty_list():
    result = contains_cycle(None)
    print(result == False)

def test_one_element_linked_list_no_cycle():
    first = LinkedListNode(1)
    result = contains_cycle(first)
    print(result == False)

def test_one_element_linked_list_cycle():
    first = LinkedListNode(1)
    first.next = first
    result = contains_cycle(first)
    print(result == True)

test_linked_list_with_no_cycle()
test_cycle_loops_to_beginning()
test_cycle_loops_to_middle()
test_two_node_cyle_at_end()
test_empty_list()
test_one_element_linked_list_no_cycle()
test_one_element_linked_list_cycle()