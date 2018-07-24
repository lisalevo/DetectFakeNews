# -*- coding: utf-8 -*-
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
MIN_ARTICLE_SIZE = 600
MAX_ARTICLE_SIZE = 3000
MIN_PARAGRAPH_SIZE = 200
MAX_SENTENCES_PER_SNIPPET = 3

def largeEnough(paragraph):
    return len(paragraph) > MIN_PARAGRAPH_SIZE

def allSubArrays(xs, n):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        if (j-i) < n:
            yield " ".join(xs[i:j])

def getAllContiguousSentences(sentences, n):
    contiguousSentences = list(allSubArrays(sentences, n))
    #print("Found " + str(len(contiguousSentences)) + " contiguous sentences")
    return contiguousSentences

def getSpacySimilarities(docs):
    #print("Getting Spacy similarities")
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
    #print("Getting Tf-Idf similarities")
    tfidf = TfidfVectorizer().fit_transform(docs)
    # no need to normalize, since Vectorizer will return normalized tf-idf
    pairwiseSimilarity = tfidf * tfidf.T
    return pairwiseSimilarity

def getMostSimilarSnippet(query, document):
    lines = [line for line in unidecode(document).split("\n")]
    snippets = getAllContiguousSentences(lines, MAX_SENTENCES_PER_SNIPPET)
    snippets = [snippet for snippet in snippets if largeEnough(snippet)]
    snippets.append(query)
    
    processedSnippets = []
    for snippet in snippets:
        wordTokens = word_tokenize(snippet)
        filteredSentence = ""
    
        for w in wordTokens:
            if w not in stopWords:
                filteredSentence += w + " "
        
        processedSnippets.append(filteredSentence)

    #pairwiseSimilarity = getTfidfPairwiseSimilarities(processedSnippets)
    pairwiseSimilarity = getSpacySimilarities(processedSnippets)
    #print(pairwiseSimilarity)

    queryIndex = len(snippets) - 1    
    mostSimilarIndex = 0
    maxSimilarityScore = pairwiseSimilarity[queryIndex, 0]
    for snippetIter in xrange(1, queryIndex):
        similarityOfSnippet = pairwiseSimilarity[queryIndex, snippetIter]
        if (similarityOfSnippet > maxSimilarityScore):
            mostSimilarIndex = snippetIter
            maxSimilarityScore = similarityOfSnippet
    
    return (snippets[mostSimilarIndex], maxSimilarityScore)

def getMostSimilarSnippetFromArticles(query, articleUrls):
    # First, get the most relevant snippet from each article
    maxSimilarityFound = 0
    urlOfMostSimilarSnippet = None
    mostSimilarSnippet = None

    for url in articleUrls:
        document = None
        try:
            articleObj = Article(url=url, language="en")
            articleObj.download()
            articleObj.parse()
            document = articleObj.text
            
            if (len(document) < MIN_ARTICLE_SIZE) or (len(document) > MAX_ARTICLE_SIZE):
                continue
            
            (snippet, similarityScore) = getMostSimilarSnippet(query, document)
            
            if (similarityScore > maxSimilarityFound):
                maxSimilarityFound = similarityScore
                urlOfMostSimilarSnippet = url
                mostSimilarSnippet = snippet

        except:
            # Skip article if fail to load
            continue
    
    snippetResult = {}
    snippetResult["claim"] = query
    snippetResult["url"] = urlOfMostSimilarSnippet
    snippetResult["similarity"] = maxSimilarityFound
    snippetResult["snippet"] = mostSimilarSnippet
    return snippetResult
