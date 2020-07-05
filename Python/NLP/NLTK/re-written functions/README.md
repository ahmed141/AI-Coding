# ‘concordance’ function
## Problem Statement
 Concordance basically returns all fixed length contexts of a given word. You need to implement the function of concordance on your own, whose context (considered as words not characters) window size would be will not be fixed. The word and window length would be passed to the function as parameter and the function should return window length number of words before and after the passed word.

## Solution
This function is implemented and tested in `concordanc.ipynb` notebook.

# 'similar' Function
## Porblem Statement
Similar basically gets all the contexts of a given word and returns all words whose contexts match with the context of given word. You need to implement the function of similar on your own, to which a word and a window length would be passed. Get all contexts of that word and length of context on each side should be equal to passed window length, match context in the whole corpus and return words whose back AND forward context matches with the back and forward context of any occurrence of passed word. This will be your own implementation of similar function. 

## Solution
This function is implemented and tested in `similar.ipynb` notebook.

# ‘approximate similar without context’ function
## Problem Statement
In this part you will implement the approximate similar function in which you do not need to take care of context.

## Solution
This function is implemented and tested in `approximate similar with context.ipynb` notebook.

# ‘approximate similar with context’ function
## Problem Statement
In this part you will implement the approximate similar function in which you need to take care of context and order in which words are occurring in the sentence.

## Solution
This function is implemented and tested in `approximate similar without context.ipynb` notebook.