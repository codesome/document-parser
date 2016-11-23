point_distribution = {

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

def point_table():
    """ 
        To return the reduced dictionary of the keywords from 'point_distribution' 
        Reduced dictionary format:
            {
                "word1": [ ("topic1",points) , ("topic2", points) , . . . ],
                "word2": [ ("topicX",points) , ("topicY", points) , . . . ],
                .
                .
                .
            }
    """
    allWords = {}

    for tp in point_distribution:
    	for s in point_distribution[tp]["sets"]:
    		for w in s["words"]:
    			if w not in allWords:
    				allWords[w] = []    

				allWords[w].append( (tp , s["points"]) )

    return allWords
