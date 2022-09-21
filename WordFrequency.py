

infile = open('sometext.txt','r')

text = infile.read()
wordcount = text.split()

newDict = {}

for word in wordcount:
    if word in newDict:
        newDict[word] += 1
    else:
        newDict[word] = 1

for key in newDict:
    print(key + ': ' + str(newDict[key]))

infile.close()