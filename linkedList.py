
class Node(object):
    """Element of a linked list"""
    def __init__(self):
        self.data = None
        self.next = None

class LL(object):
    """Linked List"""
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node
    
    def pop_node(self):
        if not self.is_empty:
            node = self.head
            self.head = self.head.next
            return node.data
        #return None

    def is_empty(self):
        return self.head == None
    
    def __str__(self):
        if self.is_empty():
            return ""
        output = ""
        node   = self.head
        while node.next:
            output += str(node.data) + " "
            node    = node.next
        output += str(node.data)
        return output
    
       
x = LL()

assert x.is_empty()

for i in range(10):
    x.add_node(i)
    
print x

