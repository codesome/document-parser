# parser

```bash
$ git clone https://github.com/thecodesome/parser.git
$ cd parser/
$ npm install
$ npm start
```
Note: You can set server port in `app.js`. Default is `3000`

#### About API

##### Request route: `/parse`
* Example `http://localhost:3000/parse`

##### Request parameters
* `str`: the string to be parsed

* `stopwords`: "true" or "false"
  * Set it to `false` to ignore stopwords.
  * Default:`true`.

* `tokens`: "true" or "false"
  * Set it to `true` to get all the tokens in `str`.
  * Default:`false`

* `uniqueWords`: "true" or "false"
  * Set it to `true` to get all the unique words in `str`.
  * Default: `false`

* `nouns`: "true" or "false"
  * Set it to `false` for not to receive nouns.
  * Default: `true`

* `limit`: Number
  * Limit on number of words with frequency to receive.
  * Default: All the words

##### Example request patterns

```
http://localhost:3000/parse?str=Hello%20World

http://localhost:3000/parse?str=I%20am%20one%20sentence.%20And%2C%20I%20am%20another%20sentence

http://localhost:3000/parse?str=This%20is%20parser&stopwords=false

http://localhost:3000/parse?str=This%20is%20parser&tokens=true

http://localhost:3000/parse?str=This%20is%20parser&stopwords=false&uniqueWords=true

http://localhost:3000/parse?str=This%20is%20parser&nouns=false&limit=2

```

##### Result structure

Result type: [JSON string](http://json.org/example.html)

```
{
  "frequencies": [
      {
          "word": String,
          "frequency": Number
      }
  ],

  "nouns": [ String ],

  "tokens": [ String ],

  "uniqueWords": [ String ],

}
```

##### Example results

str = "I am a movie fanatic. When friends want to know what picture won the Oscar in 1980 or who played the police chief in Jaws, they ask me. My friends, though, have stopped asking me if I want to go out to the movies. The problems in getting to the theater, the theater itself, and the behavior of some patrons are all reasons why I often wait for a movie to show up on TV."

* ##### Default settings
  ```
  { frequencies:
   [ { word: 'the', frequency: 7 },
     { word: 'to', frequency: 5 },
     { word: 'I', frequency: 3 },
     { word: 'in', frequency: 3 },
     { word: 'a', frequency: 2 },
     { word: 'movie', frequency: 2 },
     { word: 'friends', frequency: 2 },
     { word: 'want', frequency: 2 },
     { word: 'me', frequency: 2 },
     { word: 'theater', frequency: 2 },
     { word: 'what', frequency: 1 },
     { word: 'picture', frequency: 1 },
     { word: 'won', frequency: 1 },
     { word: 'TV', frequency: 1 },
     { word: 'Oscar', frequency: 1 },
     { word: 'fanatic', frequency: 1 },
     { word: 'or', frequency: 1 },
     { word: 'who', frequency: 1 },
     { word: 'played', frequency: 1 },
     { word: 'police', frequency: 1 },
     { word: 'chief', frequency: 1 },
     { word: 'Jaws', frequency: 1 },
     { word: 'they', frequency: 1 },
     { word: 'ask', frequency: 1 },
     { word: 'When', frequency: 1 },
     { word: 'My', frequency: 1 },
     { word: 'though', frequency: 1 },
     { word: 'am', frequency: 1 },
     { word: 'stopped', frequency: 1 },
     { word: 'asking', frequency: 1 },
     { word: 'if', frequency: 1 },
     { word: 'go', frequency: 1 },
     { word: 'out', frequency: 1 },
     { word: 'movies', frequency: 1 },
     { word: 'problems', frequency: 1 },
     { word: 'getting', frequency: 1 },
     { word: 'know', frequency: 1 },
     { word: 'itself', frequency: 1 },
     { word: 'and', frequency: 1 },
     { word: 'behavior', frequency: 1 },
     { word: 'of', frequency: 1 },
     { word: 'some', frequency: 1 },
     { word: 'patrons', frequency: 1 },
     { word: 'are', frequency: 1 },
     { word: 'all', frequency: 1 },
     { word: 'reasons', frequency: 1 },
     { word: 'why', frequency: 1 },
     { word: 'often', frequency: 1 },
     { word: 'wait', frequency: 1 },
     { word: 'for', frequency: 1 },
     { word: 'show', frequency: 1 },
     { word: 'up', frequency: 1 },
     { word: 'on', frequency: 1 },
     { word: 'have', frequency: 1 } ],
  nouns:
   [ 'movie',
     'friends',
     'theater',
     'picture',
     'TV',
     'Oscar',
     'fanatic',
     'police',
     'Jaws',
     'movies',
     'problems',
     'behavior',
     'patrons',
     'reasons',
     'show' ] }

  ```

* ##### limit=10&uniqueWords=true

  ```
  { frequencies:
   [ { word: 'the', frequency: 7 },
     { word: 'to', frequency: 5 },
     { word: 'I', frequency: 3 },
     { word: 'in', frequency: 3 },
     { word: 'a', frequency: 2 },
     { word: 'movie', frequency: 2 },
     { word: 'friends', frequency: 2 },
     { word: 'want', frequency: 2 },
     { word: 'me', frequency: 2 },
     { word: 'theater', frequency: 2 } ],
  uniqueWords:
   [ 'the',
     'to',
     'I',
     'in',
     'a',
     'movie',
     'friends',
     'want',
     'me',
     'theater',
     'what',
     'picture',
     'won',
     'TV',
     'Oscar',
     'fanatic',
     'or',
     'who',
     'played',
     'police',
     'chief',
     'Jaws',
     'they',
     'ask',
     'When',
     'My',
     'though',
     'am',
     'stopped',
     'asking',
     'if',
     'go',
     'out',
     'movies',
     'problems',
     'getting',
     'know',
     'itself',
     'and',
     'behavior',
     'of',
     'some',
     'patrons',
     'are',
     'all',
     'reasons',
     'why',
     'often',
     'wait',
     'for',
     'show',
     'up',
     'on',
     'have' ],
  nouns:
   [ 'movie',
     'friends',
     'theater',
     'picture',
     'TV',
     'Oscar',
     'fanatic',
     'police',
     'Jaws',
     'movies',
     'problems',
     'behavior',
     'patrons',
     'reasons',
     'show' ] }
  ```

* ##### limit=10&nouns=false&tokens=true

  ```
  { tokens:
   [ 'I',
     'am',
     'a',
     'movie',
     'fanatic',
     'When',
     'friends',
     'want',
     'to',
     'know',
     'what',
     'picture',
     'won',
     'the',
     'Oscar',
     'in',
     'or',
     'who',
     'played',
     'the',
     'police',
     'chief',
     'in',
     'Jaws',
     'they',
     'ask',
     'me',
     'My',
     'friends',
     'though',
     'have',
     'stopped',
     'asking',
     'me',
     'if',
     'I',
     'want',
     'to',
     'go',
     'out',
     'to',
     'the',
     'movies',
     'The',
     'problems',
     'in',
     'getting',
     'to',
     'the',
     'theater',
     'the',
     'theater',
     'itself',
     'and',
     'the',
     'behavior',
     'of',
     'some',
     'patrons',
     'are',
     'all',
     'reasons',
     'why',
     'I',
     'often',
     'wait',
     'for',
     'a',
     'movie',
     'to',
     'show',
     'up',
     'on',
     'TV' ],
  frequencies:
   [ { word: 'the', frequency: 7 },
     { word: 'to', frequency: 5 },
     { word: 'I', frequency: 3 },
     { word: 'in', frequency: 3 },
     { word: 'a', frequency: 2 },
     { word: 'movie', frequency: 2 },
     { word: 'friends', frequency: 2 },
     { word: 'want', frequency: 2 },
     { word: 'me', frequency: 2 },
     { word: 'theater', frequency: 2 } ] }
  ```

* ##### stopwords=false&nouns=false

  ```
  { frequencies:
   [ { word: 'movie', frequency: 2 },
     { word: 'friends', frequency: 2 },
     { word: 'theater', frequency: 2 },
     { word: 'picture', frequency: 1 },
     { word: 'won', frequency: 1 },
     { word: 'Oscar', frequency: 1 },
     { word: 'played', frequency: 1 },
     { word: 'police', frequency: 1 },
     { word: 'chief', frequency: 1 },
     { word: 'Jaws', frequency: 1 },
     { word: 'fanatic', frequency: 1 },
     { word: 'movies', frequency: 1 },
     { word: 'problems', frequency: 1 },
     { word: 'TV', frequency: 1 },
     { word: 'behavior', frequency: 1 },
     { word: 'patrons', frequency: 1 },
     { word: 'reasons', frequency: 1 },
     { word: 'wait', frequency: 1 },
     { word: 'show', frequency: 1 },
     { word: 'stopped', frequency: 1 } ] }

  ```
