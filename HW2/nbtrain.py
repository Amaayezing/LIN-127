 import glob
import nltk
import pickle

# positive reviews
file_names_pos = glob.glob('/home/maayez_imam/hw2/data/train/pos/*.txt')
for files in file_names_pos:
    all_words = []
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    all_words = all_words + words

# frequency distrubution for pos reviews
fd_pos = nltk.FreqDist(all_words)
num_tokens_pos = fd_pos.N()
num_types_pos = fd_pos.N()

# number of pos reviews
num_reviews_pos = len(file_names_pos)
  

# negative reviews
file_names_neg = glob.glob('/home/maayez_imam/hw2/data/train/neg/*.txt')
for files in file_names_neg:
    all_words = []
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    all_words = all_words + words

# frequency distribution for neg reviews
fd_neg = nltk.FreqDist(all_words)
num_tokens_neg = fd_neg.N()
num_types_neg = fd_neg.B()

# number of neg reviews
num_reviews_neg = len(file_names_neg)

# dictionary for review data
model =  {
    'pos_n' : num_reviews_pos,
    'neg_n' : num_reviews_neg,
    'pos_fd' : fd_pos,
    'neg_fd' : fd_neg
}

# saving my model
pickle.dump(model, open('sentiment.nb', 'wb'))
