# tutorial.py 

# I. Read entire file

# METHOD 1:

# load file using built-in open(file, mode) fxn
# named 'in_file' because the variable literally contains what is, well, in the file.
# From webpage: "Here, in_file is the name we give to our file object. We named it "in_file" to remind ourselves that it is being used only for input (reading), not output (writing)."
# 'rt' = read file in text mode. Text mode is default and the one you'll probably always want; the other option is binary mode, 'b'. We're using 'rt' instead of just 'r' because "explicit is always better than implicit."
# to use this function with HTML, include a third argument, "encoding='utf-8'"
def readMethod1():
	in_file = open('lorem.txt', 'rt')

	# extract contents into string variable
	contents = in_file.read()
	# if we've opened something, we've gotta close it (~rules to live by~)
	in_file.close()
	# show me the money
	print(contents)

# METHOD 2:

# use 'with...as' statements to encapsulate. This syntax automatically calls the method's '__exit__()' method, which, for 'open()', is 'close()'. Consequently, we don't have to include a 'close()' statement.
# NB: since this isn't enclosed in a function, it executes automatically. Seems weird b/c you're unfamiliar with this syntax, but it's the same thing you'd expect an 'if' statement, etc., to do.
def readMethod2():
	with open('lorem.txt', 'rt') as in_file:
		contents = in_file.read()
		print(contents)

# Read line-by-line

# From tutorial: "For text files, the file object iterates one line of text at a time. It considers one line of text a "unit" of data, so we can use a for...in loop statement to iterate on the data one line at a time[.]"
# So, basically, it's like working with an array. We know that arrays have a certain number of objects, and we know that the computer understands those objects to be separate the same way that I do. Here, think about the lines as the 'objects' in question.
# NB: it does *not* know length, though... I think best way to grab number of lines is probably using enumerate(file) and storing the maximum index number + 1.

def readLineByLine(file):
	with open(file, 'rt') as in_file:
		for i, line in enumerate(in_file):
			print(line, i+1)

# store as list
def fileToList(file):
	lines = []
	with open(file, 'rt') as text:
		for line in text:
			lines.append(line)
	return lines

# print(fileToList('lorem.txt'))

# remove characters at end of line using 'rstrip()'. Here, we want to remove redundant '\n' characters.
# NB: it can remove as much stuff at the end as you want. If I wanted to remove the periods at the end of each line, I could just do 'rstrip(".\n")'. (This does *not* remove the periods at the end of each sentence - the sentences =/= lines! Also for multiple kinds of punctuation I imagine you'd wanna do regex.)
def listSansNewlines(file):
	lines = []
	with open(file, 'rt') as text:
		for line in text:
			lines.append(line.rstrip('\n'))
	return lines

# print(listSansNewlines('lorem.txt'))

# using regex to search and grab
def regexTextSearch(file, pattern):
	import re

	with open(file, 'rt') as myfile:
		matches = re.findall(pattern, myfile.read())
		for match in matches:
			print(match)

regexTextSearch('lorem.txt', r'sit')