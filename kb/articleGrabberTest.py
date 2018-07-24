import articleDateExtractor
import datetime
import json
import newspaper
from newspaper import Article
import requests
from unidecode import unidecode
import urllib

PARAGRAPH_MIN_LEN = 200

def segmentArticle(url):
    articleText = ""
    try:
        # Download the content of each link
        print("Downloading: " + url)
        articleObj = Article(url=url, language="en")
        articleObj.download()
        articleObj.parse()
        articleText = articleObj.text.replace("\r\n", "\n")

    except newspaper.article.ArticleException:
        return None
    
    articleText = articleText.split("\n")
    paragraphs = []
    loneText = ""
    for p in xrange(0, len(articleText)):
        articleText[p] = articleText[p].strip()
        if articleText[p] != "" and len(articleText[p]) > PARAGRAPH_MIN_LEN:
            # Large enough chunk of text to consider a paragraph
            paragraphs.append(loneText + articleText[p])
            loneText = ""
        elif articleText[p] != "":
            # Else append it to buffer
            loneText += articleText[p] + " "

    if (loneText != ""):
        paragraphs.append(loneText)

    return paragraphs


url = "https://www.usatoday.com/story/news/2018/01/26/trumps-message-strong-america-davos/1068441001/"
paragraphs = segmentArticle(url)
print("Num paragraphs: " + str(len(paragraphs)))
print(paragraphs)
