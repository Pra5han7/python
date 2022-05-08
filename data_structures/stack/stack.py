'''
implements stack data structure
'''

class Stack:
    def __init__(self):
        self.item=[]

    def __len__(self):
        return(len(self.item))

    def __repr__(self):
        return str(self.item)

    def is_empty(self):
        return len(self.item)==0

    def push(self,data):
        self.item.append(data)

    def pop(self):
        if self.is_empty():
            return 'nothing to pop'
        return self.item.pop()

