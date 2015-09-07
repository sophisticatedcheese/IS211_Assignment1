    
 """WEEK 1 Assignment 1. T.Jeremiah September 2015"""
'WEEK 1 Assignment 1. T.Jeremiah September 2015'
 class listDivideException(Exception):
	pass

 def listDivide(numbers,divide=2):
	count=0
	try:
		for x in numbers:
			if x % divide==0:
				count=count+1
	except:
		raise ListDivideException()
		print count
		return count

	
 def testListDivide():
	try:
		listDivide([1,2,3,4,5])
		listDivide([2,4,6,8,10])
		listDivide([30,54,63,98,100],divide=10)
		listDivide([])
		listDivide([1,2,3,4,5],1)
	except Rewind:
		raise listDivideException
	testListDivide()

	
 
