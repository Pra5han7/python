'''
this module has coding snippet from different practice questions.
'''

def unique(string):
    '''
    evaluates if a string has unique
    characters in it or not.
    returns: bool
    '''
    return len(string)==len(set(string))

def palindrome(string):
    '''
    checks if the given string is palindrome
    returns: bool
    hint: 'fraud is fraud' is palindrome too
    '''
    if ' ' in string:
        checklist = string.split(' ')
        return checklist==checklist[::-1]

    return string==string[::-1]

def look_and_say(string):
    '''
    look and say sequence is implemented here.
    1
    11
    21
    1211
    look at the sequence and the next sequence would be 
    what you see :)
    google for more on look and say.
    return: (str) the next sequence
    to get the nth sequence call the function in a loop.
    '''
    result=[]
    i=0
    while i<len(string):
        count=1
        while i+1<len(string) and string[i]==string[i+1]:
            i=i+1
            count=count+1
        result.append(str(count)+string[i])
        i=i+1
    return "".join(result)

def char_frequency(string):
    '''
    returns the frequency of the characters
    in the string.
    return: dict{char:frequency}
    '''
    #treat spaces in the string
    string = string.replace(' ','')
    d={}

    for item in string:
        if item in d.keys():
            d[item] = d[item]+1
        else:
            d[item]=1
    return d

if __name__=='__main__':
