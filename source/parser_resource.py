import re
from keywords import keywords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

topic_keywords = {

    "entertainment": {
        "sets": [
            {
                "words":["entertainment","song","movie","film","music","actor"],
                "points": 3
            },
            {
                "words":["character","director","action","fiction","role"],
                "points": 2
            },
            {
                "words":["market","party","play"],
                "points": 1
            }
        ]
    },

    "sports": {
        "sets": [
            {
                "words":["sport","olympics","soccer","football","cricket","archery", "athletics", "badminton", "basketball", "volleyball", "boxing", "cycling", "diving", "fencing", "golf", "gymnastics", "handball", "hockey", "judo", "rowing", "rugby", "sailing", "shooting", "swimming", "tennis", "wrestling", "weightlifting"],
                "points": 3
            },
            {
                "words":["match","athelete","tournament","team","player","players","series","runner","goal","league","hole","batsman","game","cup","wicket"],
                "points": 2
            },
            {
                "words":["play","association","season","court","test","club","round","track"],
                "points": 1
            }
        ]
    }

}

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

def topic_points(doc):
    """ Assigns points to the topics """
    
    lda_topics = keywords(doc.lower())

    points = {
        "entertainment":0,
        "sports":0
    }

    for i in lda_topics:
        for tp in topic_keywords:
            for s in topic_keywords[tp]["sets"]:
                if i in s["words"]:
                    points[tp] += s["points"]

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
