"""Assignment 1. September 2015. T.Jeremiah"""


 class Book(object):
	author = " "
	title = " "
		
	def __init__(ans,author,title):
		ans.author = author
		ans.title = title
		
	def display(ans):
		x = "%s written by %s" % (ans.title,ans.author)
		print x
		
book_1 = Book("Harper Lee", "To Kill a Mockingbird")

book_2 = Book("John Steinbeck", "Of Mice and Men")

book_1.display()

book_2.display()
