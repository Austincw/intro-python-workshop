# coding: utf-8



'''
TODO: 
	1. Read all of the text in Sonnet.txt and write it a new file the number of lines and the number of words you found.
    2. As you are counting the words, save them all to a single list called 'words'
    3. For each word in this list, print them like such:
        1. <word 1>
        2. <word 2>
        3. <word 3>
        ...

'''

myFile = open("Sonnet.txt", "r")
words = []
lines = 0

for var in myFile:
    temp = var.split()
    words += temp
    lines += 1

myFile = open("sonnet_fun.txt", "w")
myFile.write("Number of lines is: "+str(lines)+"\n")
myFile.write("Number of words is: "+str(len(words))+"\n")

count = 1
for word in words:
    myFile.write(str(count)+". "+word+"\n")
    count += 1


