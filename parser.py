import re
from nltk import pos_tag

### Uncomment these below 2 lines for stopwords ###
# from nltk.corpus import stopwords
# stop = set(stopwords.words('english'))

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


def parse(string):
    """
        Returns a dictionary with
            1. An array of words in the string
            2. An array of words with their frequencies in descending
            3. Nouns in the string
    """

    words = tokenize(string)
    wordDictionary = {} # words with their frequencies

    for i in range(len(words)):
        w_lower = words[i].lower()

        ### Uncomment these below 2 line to exclude stop words ###
        #if w_lower in stop:
        #   continue

        if not w_lower in wordDictionary:
            wordDictionary[w_lower] = {
                "word": words[i],
                "indices": [], # indices of that word in the array 'words'
                "frequency": 0 # frequency of the word
            }
        # end if

        wordDictionary[w_lower]["indices"].append(i)
        wordDictionary[w_lower]["frequency"] += 1
    # end for

    reducedArray = [ wordDictionary[wrd] for(wrd) in wordDictionary ]

    wordTags = [ wordDictionary[wrd]["word"] for(wrd) in wordDictionary ]
    wordTags = pos_tag(wordTags)

    isNoun = (lambda tag: tag[:2]=="NN")
    nouns = [ wrd for(wrd,tag) in wordTags if isNoun(tag) ]

    del wordTags
    del wordDictionary

    # sorting in descending
    reducedArray = sorted(reducedArray , key=lambda wd:wd["frequency"] , reverse=True)

    return {
        "words": words,
        "wordsWithFrequency": reducedArray, # in descending order
        "nouns": nouns
    }
# end parse

