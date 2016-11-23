from parser_resource import *
from keywords import keywords

def parse (args):
    """ for '/parse' request """
    try:

        result = None
        if args and args.get('str'):

            result = {}

            words = tokenize(args.get('str'))
            wordDictionary = None

            # unique words with their frequencies
            if args.get('stopwords')=="false":
                # exclude stopwords
                wordDictionary = withoutStopwords(words)
            else:
                # include stopwords
                wordDictionary = withStopwords(words)

            # dictionary reduced to arrays
            reducedArray = [ wordDictionary[wrd] for(wrd) in wordDictionary ]

            # sorting in descending order based on frequency
            reducedArray = sorted(reducedArray , key=lambda wd:wd["frequency"] , reverse=True)

            # limit on number of words in 'frequency' list
            if args.get('limit'):
                limit = int(args.get('limit')) or len(reducedArray)
            else:
                limit = len(reducedArray)

            # words with frequency
            result['frequencies'] = reducedArray[:limit]


            # NOUNS [start]
            if args.get('nouns') != "false":
                
                # requested for nouns
                if args.get('properNouns')=="true":
                    # requested for nouns and proper nouns
                    NN_ = getNounsAndProperNouns( getWordTags(reducedArray) )
                    result['nouns'] = NN_['nouns']
                    result['properNoun'] = NN_['properNoun']

                else:
                    # not requested for proper nouns
                    result['nouns'] = getNouns( getWordTags(reducedArray) )

            elif args.get('properNouns')=="true":
                # requested for only proper nouns
                result['properNouns'] = getProperNouns( getWordTags(reducedArray) )
            # NOUNS [end]

            if args.get('tokens')=="true":
                # requested for all the tokens
                result['tokens'] = words

            if args.get('uniqueWords')=="true":
                # requested for all unique words (stopwords filter is applied here)
                result['uniqueWords'] = [ obj["word"] for obj in reducedArray ]

        return result

    except:
        return None

all_topics = ["entertainment","sports"]

def topic_points(doc):
    """ Assigns points to the topics """
    
    kw = keywords(doc.lower())
    print kw
    points = {}
    for i in all_topics:
        points[i] = 0

    for i in kw:
        if i in word_points:
            for j in word_points[i]:
                points[ j[0] ] += j[1]

    return [ {"topic":t,"points":points[t]} for t in points ]


def topics(doc):
    """ for '/topics' request """
    if doc != None:
        try:
            points = topic_points(doc)
            points = sorted(points , key=lambda i:i["points"] , reverse=True)

            print points

            result = []
            if len(points)>0:    
                limit = getDifferenceLimit( (points[0]["points"] or 0) or 0)
                ref = points[0]["points"] # highest point
                for i in points:
                    if i["points"]>=20 or (i["points"]>0 and (ref-i["points"])<=limit):
                        result.append(i["topic"])
                    else :
                        break

            return { "topics":result }

        except:
            return None
    else :
        return None