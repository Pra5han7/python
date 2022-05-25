'''
this module has functions printing out particular patterns.
the stars(*) are tricky they use string extend with multiply(*) operator
be cautious they are not equivalent to their numbers counterpart.
for example 
****
***
**
*
and
0123
456
78
9
are not equivalent in logic
'''

def pattern1():
    '''
    prints out a right triangle as below.
    *
    **
    ***
    ****
    *****
    '''
    lower=1
    upper=5
    for i in range(lower,upper+1):
        print('*'*i)

def pattern2():
    '''
    prints out an inverse right triangle as below.
    *****
    ****
    ***
    **
    *
    '''
    lower=1
    upper=5
    for i in range(upper,lower-1,-1):
        print('*'*i)

def pattern3():
    '''
    prints out a right triangle as below.
        *
       **
      ***
     ****
    *****
    '''
    lower=1
    upper=5
    for i in range(lower,upper+1):
        print_ = (upper-i)*' '+str(i*'*')
        print(print_)

def pattern4():
    '''
    prints out an inverse triangle as below.
    *****
     ****
      ***
       **
        *
    '''
    lower=0
    upper=5
    for i in range(upper,lower,-1):
        print_=(upper-i)*' '+(i*'*')
        print(print_)

def pattern5():
    '''
    prints out an even diamond.
        **
       ****
      ******
     ********
    **********
    **********
     ********
      ******
       ****
        **
    '''
    lower=1
    upper=5
    for i in range(lower,upper+1):
        print_upper=(upper-i)*' '+(i*'*')+(i*'*')
        print(print_upper)
    for i in range(upper,lower-1,-1):
        print_lower=(upper-i)*' '+(i*'*')+(i*'*')
        print(print_lower)

def pattern6():
    '''
    prints out an odd diamond.
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    '''
    lower=1
    upper=5
    for i in range(lower,upper+1):
        print_upper=(upper-i)*' '+(i*'*')+((i-1)*'*')
        print(print_upper)
    for i in range(upper-1,lower-1,-1):
        print_lower=(upper-i)*' '+(i*'*')+((i-1)*'*')
        print(print_lower)


if __name__=='__main__':
# uncomment below calls to see the pattern    
    #pattern1()
    #pattern2()
    #pattern3()
    #pattern4()
    #pattern5()
    #pattern6()

