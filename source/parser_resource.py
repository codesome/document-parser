import re
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

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

def withStopwords(words):
    wordDictionary = {}
    for i in range(len(words)):
        w_lower = words[i].lower()

        if not w_lower in wordDictionary:
            wordDictionary[w_lower] = {
                "word": words[i],
                "frequency": 0 # frequency of the word
            }
        # end if

        wordDictionary[w_lower]["frequency"] += 1
    # end for
    return wordDictionary

def withoutStopwords(words):
    wordDictionary = {}
    for i in range(len(words)):
        w_lower = words[i].lower()

        if not w_lower in stop:

            if not w_lower in wordDictionary:
                wordDictionary[w_lower] = {
                    "word": words[i],
                    "frequency": 0 # frequency of the word
                }
            # end if

            wordDictionary[w_lower]["frequency"] += 1

        # end if
    # end for
    return wordDictionary
