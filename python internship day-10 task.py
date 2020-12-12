Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # a) write a python program for all the cases which can check a string contains only a certain set of characters (in this case a-z,A-Z and 0-9) ?
>>> import re
>>> string = "a-zA-Z0-9"
>>> if re.findall(r'\W',string):
	print("The string contains a set of char")
else:
	print("The string does not contains a set of char")

	
The string contains a set of char
>>> 
>>> # b) write a python program that matches a word containing 'ab'?
>>> import re
>>> pattern=re.compile('a.?b')
>>> match='aaabcd'
>>> if re.search(pattern,match):
	print("found a match")
else:
	print("not match")

	
found a match
>>> 
>>> # c) write a python program to check for a number at the end of a word/sentence?
>>> import re
>>> test_number ="internship python program"
>>> res = len(re.findall(r'\w+', test_number))
>>> print("check the number at the end of the word is:" + str(res))
check the number at the end of the word is:3
>>> 
>>> # d) write a python program to search the number(0-9)of length between 1 to 3in a given string
>>> import re
>>> results = re.finditer(r"([0-9]{1,3})","exercises number 1, 12, 13, and 345 are important")
>>> print("number of length 1 to 3")
number of length 1 to 3
>>> for n in results:
	print(n.group(0))

	
1
12
13
345
>>> 
>>> # e) write a python program to match a string that contains only uppercase letters?
>>> import re
>>> def match(text):
	pattern = '[A-Z]+$'
	if re.search(pattern, text):
		return('match')
	else:
		return('not match')

	
>>> print(match("ABCDEF"))
match
>>> print(match("GEEKS"))
match
>>> 
