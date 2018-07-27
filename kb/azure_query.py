from blacklisted import blacklistedDomains
import json
import newspaper
from newspaper import Article
import requests
import unidecode
import urllib

webSearchKeyA = "BING_WEB_SEARCH_API_KEY_HERE"
azureApiHeaders = {}
azureApiHeaders["Ocp-Apim-Subscription-Key"] = webSearchKeyA

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
    return results

