import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from nltk import pos_tag, word_tokenize
from nltk.tokenize import sent_tokenize
import json
import nltk.data
import pprint
import re

NUMBER_SCALE_WORDS = ['hundred','thousand','million','billion', 'trillion']
CLAIM_CORE_WORDS = ['rising','falling','highest','lowest','all-time','level',
                    'doubled','half','halved','tripled','biggest','largest',
                    'smallest','slowest','average','fastest','record']

def clean_text(text):
  stripped_newline_characters = text.replace('\n', ' ')
  cleaned_text = re.sub(r'(?<=[.])(?=[^\s])', r' ', stripped_newline_characters)
  return cleaned_text

# Checks if a phrase's tags has the requisites parts of speech for being declarative.
def phrase_is_declarative(tags):
  if "NN" not in tags and "NNP" not in tags and "NNPS" not in tags and "NNS" not in tags:
    return False
  elif "VB" not in tags and "VBN" not in tags and "VBP" not in tags and "VBZ" not in tags and "VBD" not in tags:
    return False
  else:
      return True

if __name__ == '__main__':
  # Downloads the nltk libraries needed for Part-of-Speech (POS) tagging.
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')

  # Reads in the input.
  with open('demo_excerpt.txt', 'r') as f:
    phrases = re.compile(r", |\. ").split(clean_text(f.read()))

  declarative_phrases = []
  claim_phrases = []

  # Computes tags within a given phrase.
  for phrase in phrases:
    tags = [tag_tuple[1] for tag_tuple in pos_tag(phrase.split())]

    if phrase_is_declarative(tags):
      declarative_phrases.append(phrase)

    if (phrase_is_declarative(tags) and 
        any(number_scale_word in phrase for number_scale_word in NUMBER_SCALE_WORDS) or 
        any(claim_core_word in phrase for claim_core_word in CLAIM_CORE_WORDS)):
      claim_phrases.append(phrase)
      
  # Writes the identified phrases to a JSON file.
  with open('claim_phrases.txt', 'w') as output:
    json.dump(claim_phrases, output)
  with open('declarative_phrases.txt', 'w') as output:
    json.dump(declarative_phrases, output)
  print('Output written.')