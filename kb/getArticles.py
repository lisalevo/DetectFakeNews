import articleDateExtractor
import datetime
import json
import newspaper
from newspaper import Article
import requests
from unidecode import unidecode
import urllib

webSearchKeyA = "c7e39ef5a9a44d8cb35d00f7a8854ed6"
webSearchKeyB = "3c30ceeaae95429880730179e42f5720"
azureApiHeaders = {}
azureApiHeaders["Ocp-Apim-Subscription-Key"] = webSearchKeyA

PARAGRAPH_MIN_LEN = 200
maxDate = datetime.datetime(2018, 1, 29, 0, 0)
maxDate = maxDate.date()

def canUseArticle(url):
    d = articleDateExtractor.extractArticlePublishedDate(url)
    if (type(d) == datetime.datetime):
        d = d.date()
        print("Date of article = " + str(d))
        return d <= maxDate
    else:
        print("Could not find date of article")
        return False


baseQueryUrl = "https://api.cognitive.microsoft.com/bing/v7.0/search"
def makeQueryUrl(query, count=None, offset=None, mkt="en-US", safesearch=None):
    if (query is None):
        query = "pizzagate"
    queryParts = {}
    queryParts["q"] = query

    if (count is not None):
        queryParts["count"] = str(count)
    
    if (offset is not None):
        queryParts["offset"] = str(offset)
    
    if (mkt is not None):
        queryParts["mkt"] = str(mkt)
    
    if (safesearch is not None):
        queryParts["safesearch"] = str(safesearch)
    
    print(queryParts)
    return baseQueryUrl + "?" + urllib.urlencode(queryParts)


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


def findParagraphWithClaim(claim, paragraphs):
    if paragraphs is None or len(paragraphs) == 0:
        return "No paragraphs found"
    return paragraphs[0]

def getBlurbsForClaim(claim, tags):
    query = claim

    myQueryUrl = makeQueryUrl(query, count=100)
    req = requests.get(myQueryUrl, headers=azureApiHeaders)
    apiOutput = json.loads(req.content)
    webResults = apiOutput["webPages"]["value"]
    print("Found " + str(len(webResults)) + " web results")

    for i in xrange(1, len(webResults)):
        webResultUrl = webResults[i]["url"]
        if (canUseArticle(webResultUrl)):
            paragraphs = segmentArticle(webResultUrl)

            if (len(paragraphs) > 0):
                snippetForDisplay = findParagraphWithClaim(claim, paragraphs)
                print(snippetForDisplay)
            
            return

getBlurbsForClaim("Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone.",
    ["Trump", "November 2016", "jobs"])

