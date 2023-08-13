class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = Node

class doubly_linked_list:
    def __init__(self):
        self.head = Node

#Adding data elements
    def push(self, new_val):
        NewNode = Node(new_val)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.heaf = NewNode

#Print the Doubly Linked list
    def listprint(self, node):
        while(node is not None):
            print(node.data)
            last = nodenode = node.next




            #Implementation missing 


