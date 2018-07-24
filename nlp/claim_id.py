import nltk.data
import pprint
import re
import numpy
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
from nltk import pos_tag, word_tokenize, ne_chunk
from nltk.tokenize import sent_tokenize

# checks if a sentence is delcarative with a number based on tags
def check_if_declarative(sentence, tags):
  if "NN" not in tags and "NNP" not in tags and "NNPS" not in tags and "NNS" not in tags:
    return False
  elif "?" in sentence:
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

claimCoreWords = r"rising|falling|highest|lowest|all-time|level|doubled|half|halved|tripled|biggest|largest|smallest|slowest|average|fastest|record" 
claims = []

for phrase in phrases:
  tagged = pos_tag(phrase.split())
  tags = []
  for t in tagged:
    tags.append(t[1])
  if(len(re.findall(claimCoreWords, phrase)) > 0):
    claims.append(phrase)
  elif check_if_declarative(phrase, tags):
    claims.append(phrase)

pprint.pprint(claims)
