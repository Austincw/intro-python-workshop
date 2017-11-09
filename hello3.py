# coding: utf-8

'''
TODO: 
	1. Use a for loop to open the 'names.txt' file for reading.
	2. Print "Hello <name>!" to each name listed in the file.

Every line in a file ends with a newline character (\n). 
To remove the newline, you can use the string's rstrip() function.

'''


myFile = open("names.txt", "r")

for name in myFile:
    print "Hello {0}".format(name).rstrip()

