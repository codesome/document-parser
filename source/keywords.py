#####
## reference: https://gist.github.com/alexbowe/879414
#####

import nltk
import re
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
from parser_resource import tokenize

lemmatizer = nltk.WordNetLemmatizer()

#Taken from Su Nam Kim Paper [http://www.aclweb.org/anthology/C10-1065]
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def get_terms(tree):
    return [
        lemmatizer.lemmatize(w) 
        for leaf in leaves(tree)
        for (w,t) in leaf
        if (2 <= len(w) <= 40 and w not in stopwords)
    ]

def keywords(text):

    toks = tokenize(text)
    postoks = nltk.tag.pos_tag(toks)

    tree = chunker.parse(postoks)

    return get_terms(tree)
