import glob
import nltk
import pickle
import math

# load model
model = pickle.load(open('sentiment.nb', 'rb'))

# P(POS)
p_pos = model['pos_n'] / (model['pos_n'] + model['neg_n'])

# P(NEG)
p_neg = model['neg_n'] / (model['neg_n'] + model['pos_n'])

# open output file
output_file = open('predictions.txt', 'w')

file_names = glob.glob('/home/maayez_imam/hw2/data/test/*.txt')

# iterate through all files
for files in file_names:
    running_p = 0
    running_n = 0
    myfile = open(files, 'r')
    text = myfile.read()
    words = nltk.word_tokenize(text)
    #iterate through each token
    for word in words:
        # P(word|POS)
        p = (model['pos_fd'][word] + 1) / (model['pos_fd'].N() + model['pos_fd'].B())
        log_p = math.log(p)

        # running probability
        running_p = running_p + log_p

        # P(word|NEG)
        n = (model['neg_fd'][word] + 1) / (model['neg_fd'].N() + model['neg_fd'].B())
        log_n = math.log(n)

        # running probability
        running_n = running_n + log_n

    # P(POS|review)
    prob_p = running_p + math.log(p_pos)

    # P(NEG|review)
    prob_n = running_n + math.log(p_neg)

    # P(POS|review) > P(NEG|review)
    if prob_p > prob_n:
        pred_label = 'pos'
    # P(NEG|review) > P(POS|review)
    elif prob_n > prob_p:
        pred_label = 'neg'
    else:
        pred_label = 'error'
    
    # print to output file
    print(files, pred_label, file=output_file)

# close output file
output_file.close()
