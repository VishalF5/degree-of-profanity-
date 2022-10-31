import pandas as pd
import re


#reading file
df= pd.read_csv('tweets file location')


#set of words that indicates racial slurs
words = ('word1' ,'word2',.....'wordn')
# or
# words = pd.read_csv('words file location')
# with open(words file location) as file:
#    words = file.readlines()
#    words = [x.rstrip() for x in words]


#removing non word characters
def tokenize(sentence): 
    return re.findall(r'\w+', sentence.lower())
    

# checking degree of profanity
def profanity_degree(tokens):
    return sum(1 for x in tokens if x in words)/len(tokens)
    
    
# applying toknization
df["tokens"] = df['tweets'].apply(tokenize)


# applying profanity checker
df["profanity_degree"] = df['tokens'].apply(profanity_degree)
