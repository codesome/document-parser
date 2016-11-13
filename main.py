from parser import parse

# test sentense
sentence = "I am a movie fanatic. When friends want to know what picture won the Oscar in 1980 or who played the police chief in Jaws, they ask me. My friends, though, have stopped asking me if I want to go out to the movies. The problems in getting to the theater, the theater itself, and the behavior of some patrons are all reasons why I often wait for a movie to show up on TV."

# parsing the test sentence
parsedData = parse(sentence)
freq = parsedData["wordsWithFrequency"]
nouns = parsedData["nouns"]

# printing the most frequently used words
m = min(10,len(freq))
print("Top "+ str(m) + " words")
for i in range(m):
    print( "(" + str(freq[i]["frequency"]) + ", \"" + freq[i]["word"] + "\")")

# printing the nouns
print("\nNouns:")
print(", ".join(nouns))