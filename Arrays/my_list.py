import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a ctype array with size = self.size
        self.A = self.make_array(self.size)

    # magic method which triggered when some put object in len() funtion    
    def __len__(self):
        return self.n
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i])

    
    def make_array(self,capacity):
        # creates a C type array (static, referential) with size capacity
        return (capacity*ctypes.py_object)

    def append(self,item):
        if self.n == self.size:
            #resize
            self.resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n = self.n + 1 

    def resize(self,new_capacity):
        # create new array with new capacity 
        B = self.make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range (self.n):
            B[i] = self.A[i]
        # Resign A 
        self.A = B


