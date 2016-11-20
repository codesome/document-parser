from pos import *
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

                    NN = getNounsAndProperNouns( getWordTags(reducedArray) )
                    result['nouns'] = NN['nouns']
                    result['properNoun'] = NN['properNoun']

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

