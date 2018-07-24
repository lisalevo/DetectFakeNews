import nltk.data
import pprint
import re
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

with open('exerpt.txt', 'r') as f:
	text = f.read()

phrases = re.compile(", |\. ").split(text)
pprint.pprint(phrases)

claimCoreWords = r"rising|falling|highest|lowest|all-time|level|doubled|half|halved|tripled|biggest|largest|smallest|slowest|average|fastest|record" 
claims = []
for phrase in phrases:
	#print(re.findall(claimCoreWords, phrase))
	if(len(re.findall(claimCoreWords, phrase)) >0):
		claims.append(phrase)

pprint.pprint(claims)