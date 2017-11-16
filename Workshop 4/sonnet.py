
# finding the amount of words within the file Sonnet.txt

myFile = open("Sonnet.txt", "r")

dog = 0

for words in myFile:
    go = words.split(' ')
    dog += len(go)

myFile.close()

print dog
