import json
import newspaper
from newspaper import Article
import requests
import urllib

apiHeaders = {}
apiHeaders["X-Api-Key"] = "NEWS_API_KEY" # News API key

baseQueryUrl = "https://newsapi.org/v2/everything"
def makeQueryUrl(query, sources=None, domains=None, fromDate=None, toDate=None, language="en", sortBy="relevancy", pageSize=100):
    if (query is None):
        query = "pizzagate"
    queryParts = {}
    queryParts["q"] = query

    if (sources is not None):
        queryParts["sources"] = ",".join(sources)
    
    if (domains is not None):
        queryParts["domains"] = ",".join(domains)
    
    if (fromDate is not None):
        queryParts["from"] = fromDate
    
    if (toDate is None):
        toDate = "2018-01-22"
    queryParts["to"] = toDate
    
    if (language is not None):
        queryParts["language"] = language

    if (sortBy is not None):
        queryParts["sortBy"] = sortBy
    
    if (pageSize is not None):
        queryParts["pageSize"] = str(pageSize)

    queryParts["apiKey"] = "3fc778a92fd2494f92c7e9e979028675"
    
    print(queryParts)
    return baseQueryUrl + "?" + urllib.urlencode(queryParts)


def findBlurbWithClaim(url, claim, tags):
    blurb = None

    try:
        print("Parsing: " + url)
        # Download the content of each link
        articleObj = Article(url=url, language="en")
        articleObj.download()
        articleObj.parse()

        articleText = articleObj.text
        if (len(articleText) < 500):
            return None
        
        paragraphs = []
        ps = articleText.split("\n")
        for p in xrange(0, len(ps)):
            if ps[p].strip() != "":
                paragraphs.append(ps[p])

        print("Found " + str(len(paragraphs)) + " paragraphs in article:\n" + url)
        for p in xrange(0, len(paragraphs)):
            print(paragraphs[p] + "\n")

        blurb = ""

    except newspaper.article.ArticleException:
        # Error loading article
        blurb = None

    return blurb


def getBlurbsForClaim(claim, tags):
    query = claim
    
    sources = ["bbc-news"]
    myQueryUrl = makeQueryUrl(query, sources=sources)
    print("Query url: " + myQueryUrl)
    req = requests.get(myQueryUrl, headers=apiHeaders)
    print(req)
    apiOutput = json.loads(req.content)
    results = apiOutput["articles"]
    print("Found " + str(len(results)) + " results")

    for i in xrange(1, len(results)):
        url = results[i]["url"]
        blurb = findBlurbWithClaim(url, claim, tags)
        if blurb is not None:
            return

#getBlurbsForClaim("Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone.",
getBlurbsForClaim("2018 jobs report",
    ["Trump", "November 2016", "jobs"])
