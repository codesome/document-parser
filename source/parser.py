from parser_resource import *


def parse (args):
    try:

        result = None
        if args and args.get('str'):

            result = {}

            words = tokenize(args.get('str'))
            wordDictionary = None

            if args.get('stopwords')=="false":
                wordDictionary = withoutStopwords(words)
            else:
                wordDictionary = withStopwords(words)

            reducedArray = [ wordDictionary[wrd] for(wrd) in wordDictionary ]
            reducedArray = sorted(reducedArray , key=lambda wd:wd["frequency"] , reverse=True)

            if args.get('limit'):
                limit = int(args.get('limit')) or len(reducedArray)
            else:
                limit = len(reducedArray)


            result['frequencies'] = reducedArray[:limit]


            ## NOUNS
            if args.get('nouns') != "false":

                if args.get('properNouns')=="true":

                    NN_ = getNounsAndProperNouns( getWordTags(reducedArray) )
                    result['nouns'] = NN_['nouns']
                    result['properNoun'] = NN_['properNoun']

                else:
                    result['nouns'] = getNouns( getWordTags(reducedArray) )

            elif args.get('properNouns')=="true":
                result['properNouns'] = getProperNouns( getWordTags(reducedArray) )

            if args.get('tokens')=="true":
                result['tokens'] = words

            if args.get('uniqueWords')=="true":
                result['uniqueWords'] = [ obj["word"] for obj in reducedArray ]


        return result

    except:
        return None

def topics(doc):
    if doc != None:
        try:
            points = topic_points(doc)
            points = [ i for i in points if i["points"]>0 ]
            points = sorted(points , key=lambda i:i["points"] , reverse=True)

            result = []
            if len(points)>0:    
                limit = getDifferenceLimit( (points[0]["points"] or 0) or 0)
                ref = points[0]["points"]
                for i in points:
                    if i["points"]>=20 or (ref-i["points"])<=limit:
                        result.append(i["topic"])
                    else :
                        break

            return { "topics":result }

        except:
            return None
    else :
        return None