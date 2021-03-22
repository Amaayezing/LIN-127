import nltk

# Washington's 1789 speech
myfile = open('/home/maayez_imam/hw1/inaugural/1789-Washington.txt', 'r')
text = myfile.read()
words = nltk.word_tokenize(text)
fd = nltk.FreqDist(words)
twentyWashington = fd.most_common(20)
print("20 most common words in Washington's 1789 speech:")
for twentyW in twentyWashington:
    print(twentyW)

print("\n")

# Obama's 2009 speech
myfile2 = open('/home/maayez_imam/hw1/inaugural/2009-Obama.txt', 'r')
text2 = myfile2.read()
words2 = nltk.word_tokenize(text2)
fd2 = nltk.FreqDist(words2)
twentyObama = fd2.most_common(20)
print("20 most common words in Obama's 2009 speech:")
for twentyO in twentyObama:
    print(twentyO)
