#####
## reference: https://gist.github.com/alexbowe/879414
#####

import nltk
import re
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

def tokenize(sentence):
    """ Returns an array with all the words in the sentence """
    s = sentence[:]

    # comment out the any of the following 4 lines according to the need
    s = re.compile("\t").sub(" ",s) # replacing tab space with single space
    s = re.compile("[-_(),&.]").sub(" ",s) # removing special characters - _ ( ) , & .
    s = re.compile("[^A-Za-z ]").sub("",s) # removing non alphabets
    s = re.compile("\s\s+").sub(" ",s) # replacing multiple spaces with single space

    s = s.split()
    return s
# end tokenize

lemmatizer = nltk.WordNetLemmatizer()

#Taken from Su Nam Kim Paper...
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

def normalise(word):
    """Normalises words to lowercase and lemmatizes it."""
    return lemmatizer.lemmatize(word.lower())

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    return bool(2 <= len(word) <= 40 and word.lower() not in stopwords)


def get_terms(tree):
    return [
        normalise(w) 
        for leaf in leaves(tree)
        for (w,t) in leaf
        if acceptable_word(w)
    ]

def keywords(text):

    toks = tokenize(text)
    postoks = nltk.tag.pos_tag(toks)

    tree = chunker.parse(postoks)

    return get_terms(tree)
