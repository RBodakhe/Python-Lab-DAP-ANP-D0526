"""
Write a Python program to count the occurrences of each word in a given sentence 

string = “To change the overall look of your document. To change the look available in the gallery”
"""
def getWordCounts(word, wordList):
    counter = 0
    for w in wordList:
        if word == w:
            counter += 1
    return str(counter)


string = "To change the overall look of your document. To change the look available in the gallery"

wordList = string.split(" ")

print("Word\t\t\tOccurrences")
for word in wordList:
    print(word + "\t\t\t" + getWordCounts(word, wordList))
