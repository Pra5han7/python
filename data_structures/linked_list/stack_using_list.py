from llist import LinkedList

class Stack:
    def __init__(self):
        self.items=LinkedList()

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return self.items.is_empty()

    def peek(self):
        '''
        shows the top of the stack
        '''
        return self.items.head.data

    def push(self,data):
        '''
        push data in the stack.
        '''
        self.items.prepend(data)

    def pop(self):
        '''
        pops data from the stack.
        return: data element
        '''
        if not self.items.is_empty():
            top = self.peek()
            res = self.items.delete(top)
            return res
        else:
            raise LookupError('empty stack')
