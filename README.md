# parser

[http://codesome.pythonanywhere.com/](http://codesome.pythonanywhere.com/)

### About API

* `http://codesome.pythonanywhere.com/parse`
  * To get words with frequencies, tokens, nouns
* `http://codesome.pythonanywhere.com/topics`
  * To get topic related to the text
  * Note: Only `Sports` and `Entertainment` are supported

---

### `http://codesome.pythonanywhere.com/parse`

#### Request parameters
* `str`: the text to be parsed

* `stopwords`: "true" or "false"
  * Set it to `false` to ignore stopwords.
  * Default:`true`.

* `limit`: Number
  * Limit on number of words with frequency to receive.
  * Default: All the words

* `nouns`: "true" or "false"
  * Set it to `false` for not to receive nouns.
  * Default: `true`

* `properNouns`: "true" or "false"
  * Set it to `true` to get proper nouns.
  * Default: `false`

* `tokens`: "true" or "false"
  * Set it to `true` to get all the tokens in `str`.
  * Default:`false`

* `uniqueWords`: "true" or "false"
  * Set it to `true` to get all the unique words in `str`.
  * Default: `false`



#### Example request patterns

```
http://codesome.pythonanywhere.com/parse?str=Hello%20World

http://codesome.pythonanywhere.com/parse?str=I%20am%20one%20sentence.%20And%2C%20I%20am%20another%20sentence

http://codesome.pythonanywhere.com/parse?str=This%20is%20parser&stopwords=false

http://codesome.pythonanywhere.com/parse?str=This%20is%20parser&tokens=true

http://codesome.pythonanywhere.com/parse?str=This%20is%20parser&stopwords=false&uniqueWords=true

http://codesome.pythonanywhere.com/parse?str=This%20is%20parser&nouns=false&limit=2

```

### Result structure

Result type: [JSON string](http://json.org/example.html)

```
{
  "frequencies": [
      {
          "word": String,
          "frequency": Number
      }
  ],

  "properNouns": [ String ],

  "nouns": [ String ],

  "tokens": [ String ],

  "uniqueWords": [ String ],

}
```

---

### `http://codesome.pythonanywhere.com/topics`

#### Request parameters
* `str`: the text to be parsed

### Result structure

Result type: [JSON string](http://json.org/example.html)

```
{
  "topics": [ String ]
}
```

---

### Example results

#### `http://codesome.pythonanywhere.com/parse`

str = "I am a movie fanatic. When friends want to know what picture won the Oscar in 1980 or who played the police chief in Jaws, they ask me. My friends, though, have stopped asking me if I want to go out to the movies. The problems in getting to the theater, the theater itself, and the behavior of some patrons are all reasons why I often wait for a movie to show up on TV."


```bash
str=I%20am%20a%20movie%20fanatic.%20When%20friends%20want%20to%20know%20what%20picture%20won%20the%20Oscar%20in%201980%20or%20who%20played%20the%20police%20chief%20in%20Jaws%2C%20they%20ask%20me.%20My%20friends%2C%20though%2C%20have%20stopped%20asking%20me%20if%20I%20want%20to%20go%20out%20to%20the%20movies.%20The%20problems%20in%20getting%20to%20the%20theater%2C%20the%20theater%20itself%2C%20and%20the%20behavior%20of%20some%20patrons%20are%20all%20reasons%20why%20I%20often%20wait%20for%20a%20movie%20to%20show%20up%20on%20TV.
```

* #### Default settings
  ```
  {
    "frequencies": [
      {
        "frequency": 7,
        "word": "the"
      },
      {
        "frequency": 5,
        "word": "to"
      },
      {
        "frequency": 3,
        "word": "in"
      },
      {
        "frequency": 3,
        "word": "I"
      },
      {
        "frequency": 2,
        "word": "want"
      },
      {
        "frequency": 2,
        "word": "movie"
      },
      {
        "frequency": 2,
        "word": "me"
      },
      {
        "frequency": 2,
        "word": "friends"
      },
      {
        "frequency": 2,
        "word": "a"
      },
      {
        "frequency": 2,
        "word": "theater"
      },
      {
        "frequency": 1,
        "word": "and"
      },
      {
        "frequency": 1,
        "word": "all"
      },
      {
        "frequency": 1,
        "word": "have"
      },
      {
        "frequency": 1,
        "word": "played"
      },
      {
        "frequency": 1,
        "word": "reasons"
      },
      {
        "frequency": 1,
        "word": "Jaws"
      },
      {
        "frequency": 1,
        "word": "am"
      },
      {
        "frequency": 1,
        "word": "itself"
      },
      {
        "frequency": 1,
        "word": "are"
      },
      {
        "frequency": 1,
        "word": "go"
      },
      {
        "frequency": 1,
        "word": "if"
      },
      {
        "frequency": 1,
        "word": "some"
      },
      {
        "frequency": 1,
        "word": "what"
      },
      {
        "frequency": 1,
        "word": "police"
      },
      {
        "frequency": 1,
        "word": "for"
      },
      {
        "frequency": 1,
        "word": "TV"
      },
      {
        "frequency": 1,
        "word": "though"
      },
      {
        "frequency": 1,
        "word": "When"
      },
      {
        "frequency": 1,
        "word": "won"
      },
      {
        "frequency": 1,
        "word": "asking"
      },
      {
        "frequency": 1,
        "word": "show"
      },
      {
        "frequency": 1,
        "word": "patrons"
      },
      {
        "frequency": 1,
        "word": "out"
      },
      {
        "frequency": 1,
        "word": "picture"
      },
      {
        "frequency": 1,
        "word": "fanatic"
      },
      {
        "frequency": 1,
        "word": "Oscar"
      },
      {
        "frequency": 1,
        "word": "who"
      },
      {
        "frequency": 1,
        "word": "problems"
      },
      {
        "frequency": 1,
        "word": "often"
      },
      {
        "frequency": 1,
        "word": "know"
      },
      {
        "frequency": 1,
        "word": "they"
      },
      {
        "frequency": 1,
        "word": "ask"
      },
      {
        "frequency": 1,
        "word": "why"
      },
      {
        "frequency": 1,
        "word": "wait"
      },
      {
        "frequency": 1,
        "word": "on"
      },
      {
        "frequency": 1,
        "word": "getting"
      },
      {
        "frequency": 1,
        "word": "of"
      },
      {
        "frequency": 1,
        "word": "up"
      },
      {
        "frequency": 1,
        "word": "movies"
      },
      {
        "frequency": 1,
        "word": "chief"
      },
      {
        "frequency": 1,
        "word": "stopped"
      },
      {
        "frequency": 1,
        "word": "behavior"
      },
      {
        "frequency": 1,
        "word": "My"
      },
      {
        "frequency": 1,
        "word": "or"
      }
    ],
    "nouns": [
      "movie",
      "theater",
      "reasons",
      "Jaws",
      "police",
      "TV",
      "show",
      "patrons",
      "picture",
      "Oscar",
      "problems",
      "wait",
      "movies",
      "chief",
      "My"
    ]
  }

  ```

* #### limit=10&uniqueWords=true

  ```
  {
    "frequencies": [
      {
        "frequency": 7,
        "word": "the"
      },
      {
        "frequency": 5,
        "word": "to"
      },
      {
        "frequency": 3,
        "word": "in"
      },
      {
        "frequency": 3,
        "word": "I"
      },
      {
        "frequency": 2,
        "word": "want"
      },
      {
        "frequency": 2,
        "word": "movie"
      },
      {
        "frequency": 2,
        "word": "me"
      },
      {
        "frequency": 2,
        "word": "friends"
      },
      {
        "frequency": 2,
        "word": "a"
      },
      {
        "frequency": 2,
        "word": "theater"
      }
    ],
    "nouns": [
      "movie",
      "theater",
      "reasons",
      "Jaws",
      "police",
      "TV",
      "show",
      "patrons",
      "picture",
      "Oscar",
      "problems",
      "wait",
      "movies",
      "chief",
      "My"
    ],
    "uniqueWords": [
      "the",
      "to",
      "in",
      "I",
      "want",
      "movie",
      "me",
      "friends",
      "a",
      "theater",
      "and",
      "all",
      "have",
      "played",
      "reasons",
      "Jaws",
      "am",
      "itself",
      "are",
      "go",
      "if",
      "some",
      "what",
      "police",
      "for",
      "TV",
      "though",
      "When",
      "won",
      "asking",
      "show",
      "patrons",
      "out",
      "picture",
      "fanatic",
      "Oscar",
      "who",
      "problems",
      "often",
      "know",
      "they",
      "ask",
      "why",
      "wait",
      "on",
      "getting",
      "of",
      "up",
      "movies",
      "chief",
      "stopped",
      "behavior",
      "My",
      "or"
    ]
  }
  ```

* #### limit=10&nouns=false&tokens=true

  ```
  {
    "frequencies": [
      {
        "frequency": 7,
        "word": "the"
      },
      {
        "frequency": 5,
        "word": "to"
      },
      {
        "frequency": 3,
        "word": "in"
      },
      {
        "frequency": 3,
        "word": "I"
      },
      {
        "frequency": 2,
        "word": "want"
      },
      {
        "frequency": 2,
        "word": "movie"
      },
      {
        "frequency": 2,
        "word": "me"
      },
      {
        "frequency": 2,
        "word": "friends"
      },
      {
        "frequency": 2,
        "word": "a"
      },
      {
        "frequency": 2,
        "word": "theater"
      }
    ],
    "tokens": [
      "I",
      "am",
      "a",
      "movie",
      "fanatic",
      "When",
      "friends",
      "want",
      "to",
      "know",
      "what",
      "picture",
      "won",
      "the",
      "Oscar",
      "in",
      "or",
      "who",
      "played",
      "the",
      "police",
      "chief",
      "in",
      "Jaws",
      "they",
      "ask",
      "me",
      "My",
      "friends",
      "though",
      "have",
      "stopped",
      "asking",
      "me",
      "if",
      "I",
      "want",
      "to",
      "go",
      "out",
      "to",
      "the",
      "movies",
      "The",
      "problems",
      "in",
      "getting",
      "to",
      "the",
      "theater",
      "the",
      "theater",
      "itself",
      "and",
      "the",
      "behavior",
      "of",
      "some",
      "patrons",
      "are",
      "all",
      "reasons",
      "why",
      "I",
      "often",
      "wait",
      "for",
      "a",
      "movie",
      "to",
      "show",
      "up",
      "on",
      "TV"
    ]
  }

  ```



* #### stopwords=false&limit=5&nouns=false&properNouns=true

  ```
  {
    "frequencies": [
      {
        "frequency": 2,
        "word": "want"
      },
      {
        "frequency": 2,
        "word": "movie"
      },
      {
        "frequency": 2,
        "word": "friends"
      },
      {
        "frequency": 2,
        "word": "theater"
      },
      {
        "frequency": 1,
        "word": "often"
      }
    ],
    "properNouns": [
      "Jaws",
      "Oscar"
    ]
  }


  ```


#### `http://codesome.pythonanywhere.com/topics`


* str=this%20article%20is%20about%20a%20movie

  ```
  {
    "topics": [
      "entertainment"
    ]
  }
  ```


* str=the%20next%20match%20is%20going%20to%20be%20played%20in%20england

  ```
  {
    "topics": [
      "sports"
    ]
  }
  ```

---

References:
* [https://gist.github.com/alexbowe/879414](https://gist.github.com/alexbowe/879414)
* [https://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf](https://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf)