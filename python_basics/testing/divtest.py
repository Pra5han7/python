
'''
	Created on Tue Apr 16 21:36:15 2018

	@author: Prashant

	This is the example division module. supplies on function divide(n1,n2)
	>>> divide(10,5)
	2
'''
def divide(n1,n2):

	'''
	return division of exact case
	>>> divide(40,5)
	8

	return division of unexact case
	python2 truncates division
	>>> divide(19,2)
	9
	

	>>> divide(4,10)
	Traceback (most recent call last):
	        ...
	ValueError: n1 must be > n2
	'''
	if n1>n2 and n1%n2==0:
		return n1/n2
	if n1<n2:
		raise ValueError("n1 must be > n2")
	if n1>n2 and n1%n2 !=0:
		return n1/n2
		
if __name__=="__main__":
	import doctest
	doctest.testmod()
