from nltk import pos_tag

def getWordTags(reducedArray):
    return pos_tag( [ obj["word"] for obj in reducedArray ] )

def getNouns(wordTags):
    isNoun = (lambda tag: tag[:2]=="NN")
    return [ wrd for(wrd,tag) in wordTags if isNoun(tag) ]

def getProperNouns(wordTags):
    isProperNoun = (lambda tag: tag[:3]=="NNP")
    return [ wrd for(wrd,tag) in wordTags if isProperNoun(tag) ]

def getNounsAndProperNouns(wordTags):
    return {
        "nouns": getNouns(wordTags),
        "properNouns": getProperNouns(wordTags)
    }
