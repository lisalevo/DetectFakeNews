# -*- coding: utf-8 -*-
#import gensim
import itertools
import newspaper
from newspaper import Article
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unidecode import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

nlp = spacy.load("en")
stopWords = set(stopwords.words('english'))

# model = gensim.models.KeyedVectors.load_word2vec_format("./GoogleNews-vectors-negative300.bin", binary=True)

# Compute similarity of query and document
# Query is the direct quote
# Document is retrieved article
url = "https://www.politifact.com/truth-o-meter/article/2018/jan/09/fact-checking-donald-trumps-speech-nashville/"
#url = "https://money.cnn.com/2017/08/04/news/economy/jobs-trump-vs-obama/index.html"
#url = "https://www.factcheck.org/2018/01/trumps-numbers-/"
articleObj = Article(url=url, language="en")
articleObj.download()
articleObj.parse()
document = articleObj.text

query = "Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone."
print(unidecode(document))

def largeEnough(paragraph):
    return len(paragraph) > 500

def allSubArrays(xs, n):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        if (j-i) < n:
            yield " ".join(xs[i:j])

def getAllContiguousSentences(sentences, n):
    contiguousSentences = list(allSubArrays(sentences, n))
    print("Found " + str(len(contiguousSentences)) + " contiguous sentences")
    return contiguousSentences

def getSpacySimilarities(docs):
    print("Getting Spacy similarities")
    pairwiseSimilarity = np.zeros((len(docs), len(docs)), dtype=float)
    
    query = docs[-1]
    queryNlp = nlp(unicode(query))

    for i in xrange(0, len(docs)-1):
        docNlp = nlp(unicode(docs[i]))
        simScore = queryNlp.similarity(docNlp)
        #print("\nSimScore = " + str(simScore) + " for doc:\n" + docs[i])
        pairwiseSimilarity[len(docs)-1, i] = simScore

    # Similarity of query with respect to itself is 1
    pairwiseSimilarity[len(docs)-1, len(docs)-1] = 1
    # Expected return is matrix
    return pairwiseSimilarity


def getTfidfPairwiseSimilarities(docs):
    print("Getting Tf-Idf similarities")
    tfidf = TfidfVectorizer().fit_transform(docs)
    # no need to normalize, since Vectorizer will return normalized tf-idf
    pairwiseSimilarity = tfidf * tfidf.T
    return pairwiseSimilarity

def getMostSimilarParagraph(query, document):
    docs = [paragraph for paragraph in unidecode(document).split("\n")]
    docs = getAllContiguousSentences(docs, 5)
    docs = [doc for doc in docs if largeEnough(doc)]
    docs.append(query)
    
    processedDocs = []

    for d in docs:
        wordTokens = word_tokenize(d)
        filteredSentence = ""
    
        for w in wordTokens:
            if w not in stopWords:
                filteredSentence += w + " "
        
        processedDocs.append(filteredSentence)

    pairwiseSimilarity = getTfidfPairwiseSimilarities(processedDocs)
    #pairwiseSimilarity = getSpacySimilarities(processedDocs)
    #print(pairwiseSimilarity)

    queryIndex = len(docs) - 1    
    mostSimilarDocIndex = 0
    maxSimilarityScore = pairwiseSimilarity[queryIndex, 0]
    for p in xrange(1, queryIndex):
        similarityOfParagraph = pairwiseSimilarity[queryIndex, p]
        if (similarityOfParagraph > maxSimilarityScore):
            mostSimilarDocIndex = p
            maxSimilarityScore = similarityOfParagraph
    
    return (processedDocs[mostSimilarDocIndex], maxSimilarityScore)

print("Query: " + query)
print(getMostSimilarParagraph(query, document))

