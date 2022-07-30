def summation_pairs(list_,sum_):
    '''
    returns the values of those indexes in the list_ which
    adds up to sum_
    return: List of tuples
    example:
    ---------------------------
    list_= [0,1,2,3,4,5]
    sum_= 5
    returns [(0,5),(1,4),(2,3)]
    ---------------------------
    Hint: the maximum pairs in the list would always be half
    the value of sum_. why??
    '''
    result=[]
    index=0
    upper_index=sum_/2
    max_index=len(list_)-1

    while index<upper_index:

        if(index+max_index)==var:
            result.append((list_[index],list_[max_index]))
            index=index+1
            max_index=max_index-1
        
        elif (index+max_index)<var:
            while (index+max_index)!=var:
                index = index+1
        
        elif (index+max_index)>var:
            max_index=max_index-1

    if result:
        return result
    else:
        return 'no pairs possible'
