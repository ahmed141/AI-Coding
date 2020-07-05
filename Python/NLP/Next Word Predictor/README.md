# New Word Prediction System
 Word prediction is an intelligent word processing feature that can alleviate writing breakdowns by reducing the number of keystrokes necessary for typing words. 
 
Steps: 

    1) Collect a big Urdu corpus (at least 100K tokens, the larger the better) from the internet. Clean the corpus by removing punctuations (including Unicode punctuations). Add start (<s>) and end (</s>) of sentence marker wherever needed. 
    2) Calculate unigram, bigram and trigram probabilities of the corpus. 
    3) Use these probabilities to suggest world while typing

Evaluaion:

Because the goal of word prediction systems is to reduce the number of keystrokes, the primary evaluation for word prediction is keystroke savings. Keystroke savings (KS) measures the percentage reduction in keys pressed compared to letter-by-letter text entry. 

## Step 01: Corpus collection
I have collected and cleaned 23 blogs and 9 novels of urdu. All of them are saved in ‘data’ folder with original text, the naming convention for original docs is blog*.urdu  or novel*.urdu. Then I have cleaned combined and cleaned and then separated it into train and test files by writing python code. The code files that helped throughout this process are: 

    - dataprep_01.ipynb 
    - dataprep_02.ipynb 
    - dataprep_03.ipynb 
    - dataprep_04.ipynb 
    - dataprep_05.ipynb 

The ‘data_stats.ipynb’ is not very useful because it was only used to look at the out-coming files and their stats. The train and test distribution is 80% and 20% of overall corpus and test set is created by taking every 5th sentence from the corpus collection, so that it is good mix.  
The final data files that will be used in next processes/steps are: 

    - uniallsentences_train.urdu to calculate unigram probabilities
    - allsentences_train.urdu to calculate bigram probabilities 
    - triallsentences_train.urdu to calculate trigram probabilities 

## Step-02: Calculate unigram/bigram/trigram probabilities 
The functions to calculate the unigram, bigram and trigram are defined in `‘allFunctons.ipynb’` code file, and their names are `‘calculate_unigram_probs’`, `‘calculate_bigram_probs’` and `‘calculate_trigram_probs’`. To eliminate the penalty of computing probabilities every time I run code, I have saved them in `‘unigram_prob1.0.npz’`, `‘bigram_prob1.0.pkl’` and `‘trigram_prob1.0.pkl’` in `‘data’` folder so that I can use them later. 

## Step-03: Implement Word Prediction 
### Uni-Gram:  
I have defined used the `‘suggest_words_unigram’` function in `‘unigram.ipynb’`. This function takes: 
```
 prob_keys: Tokens in numpy array  
 prob_values: Probabilities associated to tokens in numypy array  
 word_: Word that is being typed in string  
 n:  Number of top prediction to return in integer type and this function return the list of top ‘n’ predictions. 
 ```
### Bi-Gram:  
I have defined used the `‘suggest_words_bigram’` function in ‘bigram.ipynb’. This function takes:  
```
bigram_probs: It is dict contains the probabilities of each bigram from training corpus  
word_:  Word that is being typed in string  
n:  Number of top prediction to return in integer type and this function return the list of top ‘n’ predictions 
```

### Tri-Gram:  
I have defined used the `‘suggest_words_trigram’` function in ‘trigram.ipynb’. This function takes:  
```
trigram_probs: It is dict contains the probabilities of each trigram from training corpus  
word_:  Word that is being typed in string  
n:  Number of top prediction to return in integer type and this function return the list of top ‘n’ predictions  
```