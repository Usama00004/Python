class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data_val):
        if data_val not in self.stack:
            self.stack.append(data_val)
            print(self.stack)
            return True
        else:
            return False   
    def peek(self):
        return self.stack[-1]
                 
    def pop(self):
        if len(self.stack) <= 0:
            return("No element in the stack")
        else:
            return self.stack.pop()                   




