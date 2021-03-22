from collections import Counter

# Washington's 1789 speech
myfile = open('/home/maayez_imam/hw1/inaugural/1789-Washington.txt', 'r')
text = myfile.read()
words = text.split()
wordcount = Counter(words)
twentyWashington = wordcount.most_common(20)
print("20 most common words in Washington's 1789 speech:")
for twentyW in twentyWashington:
    print(twentyW)

print("\n")

# Obama's 2009 speech
myfile2 = open('/home/maayez_imam/hw1/inaugural/2009-Obama.txt', 'r')
text2 = myfile2.read()
words2 = text2.split()
wordcount2 = Counter(words2)
twentyObama = wordcount2.most_common(20)
print("20 most common words in Obama's 2009 speech:")
for twentyO in twentyObama:
    print(twentyO)
