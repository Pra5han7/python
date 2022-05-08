'''
implements linked list.
linked lists are made up of nodes. there is one data section
and one pointer to next node. linked lists are collections of
these nodes.
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
       self.head=None

    def __repr__(self):
        res=''
        if self.is_empty():
            return '[]'

        cur=self.head
        while cur:
            res=res+str(cur.data)+','
            cur=cur.next
        return str(res[:-1:])

    def __len__(self):
        if self.is_empty():
            return 0

        cur=self.head
        count=0
        while cur:
            cur=cur.next
            count=count+1
        return count

    def is_empty(self):
        '''
        checks if the linked list is empty.
        return: bool
        '''
        return self.head==None

    def append(self,data):
        '''
        adds a node at the end of the
        linked list.
        '''
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
            return

        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next = new_node

    def prepend(self,data):
        '''
        adds a node at the beginning
        of the linked list.
        '''
        new_node = Node(data)
        if self.is_empty():
            self.head=new_node

        new_node.next=self.head
        self.head=new_node

    def if_exists(self,data):
        '''
        checks if a node exists in the
        linked list.
        return: bool
        '''
        if self.is_empty():
            return False
        cur=self.head
        while cur:
            if cur.data==data:
                return True
            else:
                cur=cur.next
        return False

    def add(self,data,add_after):
        '''
        adds a node after a given node.
        '''
        new_node=Node(data)
        if self.if_exists(add_after):
            curr=self.head
            while curr:
                if curr.data==add_after:
                    new_node.next=curr.next
                    curr.next=new_node
                    break
                curr=curr.next
        else:
            raise LookupError("{} does not exists in the list".format(add_after))
