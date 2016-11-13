# parser

#### Run:
```
python3 parser.py
```

Note: If you want to exclude stop words, check line number `4` and `37` in `parser.py`

#### Dependencies
* nltk ([Download here](http://www.nltk.org/install.html), for python3 install with pip3)
  * `pos_tag` from `nltk`
    * If this is not present in default installation of nltk, follow the following procedure to include it

    ``` bash
    Python 3.5.2 (default, Sep 10 2016, 08:21:44)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import nltk
    >>> nltk.download()
    NLTK Downloader
    ---------------------------------------------------------------------------
        d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
    ---------------------------------------------------------------------------
    Downloader> d

    Download which package (l=list; x=cancel)?
      Identifier> averaged_perceptron_tagger
    ```

  * `stopwords` from `nltk.corpus`
    * If this is not present in default installation of nltk, follow the following procedure to include it

    ``` bash
    Python 3.5.2 (default, Sep 10 2016, 08:21:44)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import nltk
    >>> nltk.download()
    NLTK Downloader
    ---------------------------------------------------------------------------
        d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
    ---------------------------------------------------------------------------
    Downloader> d

    Download which package (l=list; x=cancel)?
      Identifier> stopwords
    ```
