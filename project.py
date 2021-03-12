import nltk
from nltk.corpus import stopwords
import glob
import string

# list of stop words
stop_words = stopwords.words('english')

# add capitalized stop words
added_stops = ['I', 'To', 'The', 'It', 'If', 'And', 'But', 'She', 'He', 'For', 'Where', 'So']
stop_words.extend(added_stops)

# add incorrect words
added_wrong = ["'re", "'m", "'s", "n't"]
stop_words.extend(added_wrong)

# remove the words 'you' and 'we' from stop words
stop_words.remove("you")
stop_words.remove("we")

# list of punctuation
punc = string.punctuation
punc = punc + '’'


# 80s songs
file_names_80s = glob.glob('/home/maayez_imam/project/songs/1980s/*')

# iterate through all files and tokenize the words
final_words_80s = []
for files in file_names_80s:
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    final_words_80s = final_words_80s + words  

# filter the words of stop words and punctuation
filtered_words_80s = []
for w in final_words_80s:
    if (w not in stop_words) and (w not in punc):
        filtered_words_80s.append(w)

# create frequency distribution of filtered words
fd_80s = nltk.FreqDist(filtered_words_80s)

# find and print 25 most common words
common_words_80s = fd_80s.most_common(25)
print("25 most common words in 1980s songs:")
print(common_words_80s)

# 90s songs
file_names_90s = glob.glob('/home/maayez_imam/project/songs/1990s/*')

# iterate through all files and tokenize the words
final_words_90s = []
for files in file_names_90s:
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    final_words_90s = final_words_90s + words  

# filter the words of stop words and punctuation
filtered_words_90s = []
for w in final_words_90s:
    if (w not in stop_words) and (w not in punc):
        filtered_words_90s.append(w)

# create frequency distribution of filtered words
fd_90s = nltk.FreqDist(filtered_words_90s)

# find and print 25 most common words
common_words_90s = fd_90s.most_common(25)
print("25 most common words in 1990s songs:")
print(common_words_90s)

# 2000s songs
file_names_2000s = glob.glob('/home/maayez_imam/project/songs/2000s/*')

# iterate through all files and tokenize the words
final_words_2000s = []
for files in file_names_2000s:
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    final_words_2000s = final_words_2000s + words  

# filter the words of stop words and punctuation
filtered_words_2000s = []
for w in final_words_2000s:
    if (w not in stop_words) and (w not in punc):
        filtered_words_2000s.append(w)

# create frequency distribution of filtered words
fd_2000s = nltk.FreqDist(filtered_words_2000s)

# find and print 25 most common words
common_words_2000s = fd_2000s.most_common(25)
print("25 most common words in 2000s songs:")
print(common_words_2000s)

# 2010s songs
file_names_2010s = glob.glob('/home/maayez_imam/project/songs/2010s/*')

# iterate through all files and tokenize the words
final_words_2010s = []
for files in file_names_2010s:
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    final_words_2010s = final_words_2010s + words  

# filter the words of stop words and punctuation
filtered_words_2010s = []
for w in final_words_2010s:
    if (w not in stop_words) and (w not in punc):
        filtered_words_2010s.append(w)

# create frequency distribution of filtered words
fd_2010s = nltk.FreqDist(filtered_words_2010s)

# find and print 25 most common words
common_words_2010s = fd_2010s.most_common(25)
print("25 most common words in 2010s songs:")
print(common_words_2010s)
