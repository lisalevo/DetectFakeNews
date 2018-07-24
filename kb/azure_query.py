import articleDateExtractor
from blacklisted import blacklistedDomains
import datetime
import json
import newspaper
from newspaper import Article
import requests
import unidecode
import urllib

webSearchKeyA = "c7e39ef5a9a44d8cb35d00f7a8854ed6"
webSearchKeyB = "3c30ceeaae95429880730179e42f5720"
azureApiHeaders = {}
azureApiHeaders["Ocp-Apim-Subscription-Key"] = webSearchKeyA
MAX_DATE = datetime.datetime(2018, 1, 29, 0, 0)
MAX_DATE = MAX_DATE.date()

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

def canUseArticle(url):
    try:
        d = articleDateExtractor.extractArticlePublishedDate(url)
        if (type(d) == datetime.datetime):
            d = d.date()
            #print("Date of article = " + str(d))
            return d <= MAX_DATE
        else:
            #print("Could not find date of article")
            return False
    except Exception:
        return False

def isSafe(url):
    for domain in blacklistedDomains:
        if (url.find(domain) != -1):
            return False
    
    return True

def getArticlesForQuery(query):
    results = []
    myQueryUrl = makeQueryUrl(query, count=100)
    req = requests.get(myQueryUrl, headers=azureApiHeaders)
    apiOutput = json.loads(req.content)
    webResults = apiOutput["webPages"]["value"]
    
    for i in xrange(0, len(webResults)):
        webResultUrl = webResults[i]["url"]
        results.append(webResultUrl)

    results = [result for result in results if isSafe(result)]
    results = [result for result in results if canUseArticle(result)]
    return results

