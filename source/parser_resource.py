import re
from keywords import keywords
from point_table import point_table
from nltk.corpus import stopwords
from nltk import pos_tag
stop = set(stopwords.words('english'))

topic_keywords = point_table()

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
    """ Returns words with their frequencies (includes stopwords) """
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
    """ Returns words with their frequencies (excludes stopwords) """
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

def getWordTags(reducedArray):
    """ To return parts of speech tagged words """
    return pos_tag( [ obj["word"] for obj in reducedArray ] )

def getNouns(wordTags):
    """ To return nouns from the tagged words """
    isNoun = (lambda tag: tag[:2]=="NN")
    return [ wrd for(wrd,tag) in wordTags if isNoun(tag) ]

def getProperNouns(wordTags):
    """ To return proper nouns from the tagged words """
    isProperNoun = (lambda tag: tag[:3]=="NNP")
    return [ wrd for(wrd,tag) in wordTags if isProperNoun(tag) ]

def getNounsAndProperNouns(wordTags):
    """ To return nouns and proper nouns from the tagged words """
    return {
        "nouns": getNouns(wordTags),
        "properNouns": getProperNouns(wordTags)
    }


def topic_points(doc):
    """ Assigns points to the topics """
    
    lda_topics = keywords(doc.lower())

    points = {
        "entertainment":0,
        "sports":0
    }

    for i in lda_topics:
        if i in topic_keywords:
            for j in topic_keywords[i]:
                points[ j[0] ] += j[1]

    return [ {"topic":t,"points":points[t]} for t in points ]

def getDifferenceLimit(val):
    if val>0 and val<5:
        return 1
    elif val>=5 and val<10:
        return 2
    elif val>=10 and val<20:
        return 5
    elif val>=20 and val<25:
        return 7
    elif val>=25 and val<30:
        return 10
    else:
        return 15
