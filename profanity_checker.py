import pandas as pd

import re

#reading tweets file

df = pd.read_csv("tweets file.txt")
#removing non word characters from
sentences

def tokenize(sentence):

return re.findall(r'\w#", sentence.lower())

def profanity_degree(tokens):

return sum(1 for i in tokens if i in
profane_words)/len(tokens)

with open(location2) as file:
profane_words = file.readlines()
profane_words = [profane_word.rstrip()
for profane_word in profane_words]

dff'tokens'] = df.tweets.apply(tokenize)

dff’profanity_degree'] = df.head(100000).tok
ens.apply(profanity_degree)

# saving the result (tweet file along with
profanity degree for every tweet )

df[["tweets’,'profanity_degree']].to_csv("“twe

ets_output.csv',index=False)

print(‘results have been saved in filename

Created with Mi Notes