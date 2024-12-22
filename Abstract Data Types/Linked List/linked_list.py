from node import Node
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def insert_head(self,value):
        # new node 
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        # ressign head
        self.head = new_node
        # incrementing count
        self.n = self.n + 1

    def insert_after(self,value,after):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'Item not found'    

    def append(self,value): 
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1    

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):
        if self.head == None:
            return 'Empty Linked List'    
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1


    def remove(self,value):
        if self.head == None:
            return 'Empty Linked List'
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head    
        while curr.next == None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return 'Item not found'
        else:
            curr.next = curr.next.next
            self.n = self.n -1

    def search(self,item):

        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1

        return 'Not Found'

    def __getitem__(self,index):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'IndexError'











