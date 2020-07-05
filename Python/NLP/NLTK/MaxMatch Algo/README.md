# MaxMatch Algorithm
This algorithm starts by point at the beginning of a string. It chooses the longest word in the dictionary that matches the input at the current position. If we can’t find such word, we just move the pointer one character forward and create an one-character word.

Note:
``` 
This algorithm has been mainly used for chinease language but in this attempt, I have implementated it on Urdu Corpus.
```

## Files Hierarchy
`wordlist.txt` is Corpus for owrr MaxMatch algorithm in `MaxMatch.ipynb` 
`50_nospaces.txt` is text strings that will be used to test MaxMatch in `MaxMatch.ipynb`

# Notebooks
## `MaxMatch.ipynb`
This function gets the max word size from dictionary using ‘Max_Size’ function and then starts reading words from input sentence with max size of max word size from dictionary. Iterates this whole process until whole string read. The word is only considered a token if it is a max size match.

## `P02.ipynb`
The function calculates size of each word of dictionary. And then calculates average using sum of sizes and number of total words. And the answer is returned 