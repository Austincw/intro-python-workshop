# coding: utf-8

'''
TODO: 
	1. Create a variable called 'name' that holds a name.
	2. Print "Hello <name>" using the name variable.
	   For example, if the name is "Ron" it should print:
	   Hello Ron!
    3. Create a function called 'sum' that takes to arguments
       (strings or integers) and returns the sum of them
    4. Using your function 'sum' add two integers together and
       print the resulting sum.

There are a few ways to use variables in strings:
	- Adding strings together using '+'.
	- Using a comma between the string and the variable. 
	  The comma combines the strings and adds a space between them.
	- Using the string's format() function.

You can make notes in a script by using comments.
	- The hash sign, #, is used for a one-line comment. 
	  Python ignores all text after the #.
	- A three-quote comment (single or double quotes) lets you put 
	  any number of lines of text between the opening and closing 
	  three quotes.
'''



name = "Austin"
print "Hello " + name
print "Hello",name
print "Hello {0}".format(name)
print

def add(x,y):
    return x + y

var = add(5,8)
val = add("Hello ",name)

print var
print val