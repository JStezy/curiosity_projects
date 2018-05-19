from collections import Counter
import string

filename = ""

#This function joins each character together as long as it's not punctuation, hence removing punctuation
def strip_punct(word):
  exclude = set(string.punctuation)
  word = ''.join(ch for ch in word if ch not in exclude)
  return word

def make_word_list(filename):
  file = open(filename)
  contents = file.readlines()
  words = []
  for line in contents:
    words.extend([strip_punct(word).lower() for word in line.split())
  file.close()
  return words

words = make_word_list(filename)
tally = Counter(words)

word = "A"
while word != "":
  word = input("What word would you like to tally up in %s?" % filename)
  print tally[word]
