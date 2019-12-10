import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd
import acquire

def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    string = string.strip()
    string = string.replace('\n', ' ')
    return string 

def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    text_stemmed = ' '.join(stems)
    return text_stemmed

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemmatized = ' '.join(lemmas)
    return text_lemmatized

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    # Tokenize the string
    string = tokenize(string)
    words = string.split()
    stopword_list = stopwords.words('english')
    # Remove the excluded words from the stopword list 
    stopword_list = set(stopword_list) - set(exclude_words)
    # Add in user specified extra words
    stopword_list = stopword_list.union(set(extra_words))
    filtered_words = [w for w in words if w not in stopword_list ]
    final_string = " ".join(filtered_words)
    return final_string  

# just readme_contents
def prep_contents(df):
    df['original'] = df.readme_contents
    df['stemmed'] = df.readme_contents.apply(basic_clean).apply(stem)
    df['lemmatized'] = df.readme_contents.apply(basic_clean).apply(lemmatize)
    df['clean'] = df.readme_contents.apply(basic_clean).apply(remove_stopwords)
    return df