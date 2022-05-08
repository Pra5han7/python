'''
implements logic to convert a decimal number to binary
using stack.
242 / 2 = 121 remainder--->0
121 / 2 = 60 remainder --->1
60 / 2 =30   remainder --->0
30/2 = 15                  0
15/2 = 7                   1
7/2 = 3                    1
3/2 = 1                    1
1/2 =0                     1

binary would be 11110010
'''
from stack import Stack
def decimal_to_binary(num):
    binary=''
    s=Stack()
    while num>0:
        bit = num % 2
        s.push(bit)
        num = num//2

    while not s.is_empty():
        binary = binary+str(s.pop())

    return binary

if __name__=="__main__":
    num=242
    binary=decimal_to_binary(num)
    print(binary)
