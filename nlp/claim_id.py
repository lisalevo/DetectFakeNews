import nltk.data
import pprint
import re
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
from nltk import pos_tag, word_tokenize
from nltk.tokenize import sent_tokenize

# checks if a sentece is delcarative with a number based on tags
def check_if_declarative(sentence, tags):
  if sentence[0].isupper() == False:
    if sentence[1].isupper() == False:
      return False
    else:
      return True
  elif sentence[-1] != ".":
    return False
  elif "NN" not in tags and "NNP" not in tags and "NNPS" not in tags and "NNS" not in tags:
    return False
  elif "?" in sentence or "!" in sentence:
    return False
  elif "VB" not in tags and "VBN" not in tags and "VBP" not in tags and "VBZ" not in tags and "VBD" not in tags:
    return False
  elif "CD" not in tags:
    return False
  else:
      return True

with open('exerpt.txt', 'r') as f:
	text = f.read()

phrases = re.compile(", |\. ").split(text)
#pprint.pprint(phrases)

claimCoreWords = r"rising|falling|highest|lowest|all-time|level|doubled|half|halved|tripled|biggest|largest|smallest|slowest|average|fastest|record" 
claims = []
for phrase in phrases:
	if(len(re.findall(claimCoreWords, phrase)) >0):
		claims.append(phrase)

pprint.pprint(claims)

# checking for full sentences with claims
sent_tok_list = sent_tokenize(text)
for sentence in sent_tok_list:
  tagged = pos_tag(sentence.split())
  tags = []
  for tag in tagged:
    tags.append(tag[1])
  if(len(re.findall(claimCoreWords, sentence)) >0):
	  if check_if_declarative(sentence, tags):
	    print('DECL:')
	    print(sentence)
