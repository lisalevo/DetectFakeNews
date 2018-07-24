import azure_query
import article_analyzer
import pprint

matthew_claims = ["we are finally seeing rising wages",
    "African American unemployment stands at the lowest rate ever recorded",
    "and Hispanic American unemployment has also reached the lowest levels in history",
    "Small-business confidence is at an all-time high",
    "The stock market has smashed one record after another",
    "we enacted the biggest tax cuts and reforms in American history",
    "we nearly doubled the standard deduction for everyone",
    "We also doubled the child tax credit."
]

print("Checking matthews claims...\n")
for claim in matthew_claims:
    webResults = azure_query.getArticlesForQuery(claim)
    snippetForClaim = article_analyzer.getMostSimilarSnippetFromArticles(claim, webResults[0:10]) # Take first 10
    pprint.pprint(snippetForClaim)


maddys_claims = ['Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone',
    'After years and years of wage stagnation, we are finally seeing rising wages. Unemployment claims have hit a 45-year low',
    'The stock market has smashed one record after another, gaining $8 trillion and more in value in just this short amount of time',
    'Americans 401k, retirement, pension, and college-savings accounts have gone through the roof. And just as I promised the American people from this podium 11 months ago, we enacted the biggest tax cuts and reforms in American history. Our massive tax cuts provide tremendous relief for the middle class and small businesses. To lower tax rates for hardworking Americans, we nearly doubled the standard deduction for everyone',
    'Now, the first $24,000 earned by a married couple is completely tax-free'
]

print("\n\nChecking maddys claims...\n")
for claim in maddys_claims:
    webResults = azure_query.getArticlesForQuery(claim)
    snippetForClaim = article_analyzer.getMostSimilarSnippetFromArticles(claim, webResults[0:10]) # Take first 10
    pprint.pprint(snippetForClaim)