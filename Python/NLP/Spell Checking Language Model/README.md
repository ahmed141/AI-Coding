# Noisy Channel Model for Spell Checking

### How to Run
    1. open jupyter notebook
    2. open ./code/main.ipynb file
    3. run its all cells
    result will be saved in ./results folder in a file named 'report.txt' once all cells has completed their execution.

## Algorithmic Steps
### Step 01: Train an interpolated (bigram + unigram) language model 
I have used same functions `calculate_unigram_probs` (for calculating unigram probabilities) and `calculate_bigram_probs` (for calculating bigram probabilities) used in assignment#04. For interpolated model I have used `lambda1` = 0.7 and `lambda2` = 0.3. To change this weights simply change `lambda1` and `lambda2` values in arguments of `get_rank10_candidates` function.

### Step 02: Find the candidate words
I have divided this task in following steps.
```
Get all candidate words list at edit distance 1 and 2 
[Note: get_candidates_1n2 function contains the code for this]
    a - Get all candidates after deletion 
    [Note: deletions_list function contains the code for this num argument indicates the number of edits]
    b - Get all candidates after insertion 
    [Note: insertions_list function contains the code for this num argument indicates the number of edits]
    c - Get all candidates after substitution 
    [Note: substitutions_list function contains the code for this num argument indicates the number of edits]

Reducing candidates list
[Note: reduced_candidates function contains the code for this]
    a - In ranking function, to reduce time complexity by removing words from wordlist that are not ±2 length distance away from error word.
    b - Then I have kept only those candidates that are in that wordlist
```

### Step 03: Rank the candidate words
I have taken the candidate words list and calculated the probability for each word candidate based on the interpolation model. Then I have sorted the candidates based on those probabilities.

	[Note:	Code for this is in ‘rank_candidates’ function it takes error_word, candidates list, unigram model, bigram model, lambda1 and lambda2. This function returns the sorted candidate list along with their probabilities. Another modification of this same function is implemented in ‘rank10_candidates’ that returns only top-10 candidates with their probabilities.]

### Step 04: Reporting results
I have encapsulated all the above steps in 1 function named `‘get_rank_candidates’` it takes `error_word`, `urdu_letters_list`, `wordslist`, `unigram model`, `bigram model`, `lambda1` and `lambda2`, and returns the sorted candidates list along with probabilities. I have also implemented a variation of this as `‘get_rank10_candidates’` to get top-10 candidates and probabilities list. I have used the later to produce the `report.txt` document in results folder.

Report Document:

The ‘results’ folder contains this file named ‘report.txt’. The report document contains the detail of each error word name, its top-10 candidate words with probabilities and the remarks if the actual word exists within the candidates list.
