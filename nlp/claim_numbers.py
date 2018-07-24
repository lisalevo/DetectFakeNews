import re

doesHaveNumber = re.compile('[0-9]')

from nltk import word_tokenize
directory='PathToFolder'
for file in os.listdir(directory):
    path = directory + file
    text = open(path)
    for line in text:
        #print(line)
        tokens = word_tokenize(line)
        #print(tokens)
        for i in tokens:
            regularExpressionCheck = doesHaveNumber.search(i)
            if regularExpressionCheck:
                #print(line)
                print(line)
                break