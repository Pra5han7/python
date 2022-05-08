'''
module to check paranthesis balancing.
logic:
    -set index
    -set the flag is_balanced to true
        -iterate over items if index is in range and is_balanced is True
        -if the item being reviewed in '{[('--> push to stack
        -otherwise check if stack is empty:
        -if empty set is_balanced to False:
        -if not pop the item from stack and check for match
            -if not matched--> set is_balanced to False
    -if is_balanced is True and stack is empty then balanced otherwise not

'''
from stack import Stack

def is_match(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='[' and p2==']':
        return True
    elif p1=='{' and p2=='}':
        return True
    else:
        return False


def paran_balance(sample):
    s=Stack()
    is_balanced=True
    index=0

    while index<len(sample) and is_balanced:
        paran = sample[index]
        if paran in '{[(':
            s.push(paran)
        else:
            if s.is_empty():
                is_balanced=False
            else:
                top=s.pop()
                if not is_match(top,paran):
                    is_balanced=False
        index=index+1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

if __name__=="__main__":
    sample = '((()()()))'
    print(paran_balance(sample))
