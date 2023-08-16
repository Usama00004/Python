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

    # magic methid for print result
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
            return '[' + result[:-1] + ']' 
   
    #indexing (magic method)
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
    def __delitem__(self,pos):
        if 0 <= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1 

   # making array
    def make_array(self,capacity):
        # creates a C type array (static, referential) with size capacity
        return (capacity*ctypes.py_object)

    # appending new item to array 
    def append(self,item):
        if self.n == self.size:
            #resize
            self.resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n = self.n + 1 

    # pop out last element from list
    def pop(self):
        if self.n == 0:
            return 'Empty List'    
        else:
            print(self.A[self.n -1])
            self.n = self.n -1

    # clear all the list
    def clear(self):
        self.size = 1 
        self.n =0

    # find item in the list
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Value Error'   
    # inserting new element 
    def insert(self,pos,item):
        if self.n == self.size:
            self.resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1


    def remove(self,item):
        pos = self.find(item)
        if type (pos) == int:
            # delete 
            self.__delitem__(pos)
        else:
            return pos
    # resizing array
    def resize(self,new_capacity):
        # create new array with new capacity 
        B = self.make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range (self.n):
            B[i] = self.A[i]
        # Resign A 
        self.A = B

 
