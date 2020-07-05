#### Note: 
The code is written and run in Jupyter Notebook with Python3 in Windows10 environment. I have used numpy 1.14.2 package as well to enhance computation power. All the functions used are defined in ‘Functions_Defs.ipynb’ in code folder.

The code for MED experiments is in `Minimum Edit Distance + WER.ipynb`, and for other distances is in other notebooks for 3 Datasets.

# Algorithms
## Minimum Edit Distance + WER
The `‘MED’` named function is defined that calculates the minimum edit distance between two strings.

```
input: 
    source (string), target (string) 

output: 
    out:  a dict object which contain following items              
    'D': The number of deletions required to convert source to target              
    'I': The number of insertions required to convert source to target              
    'S': The number of substitutions required to convert source to target              
    'MED': The minimum edit distance to convert source to target 
```
This function is used in both ‘word_based’ and ‘char_based’.
### Word Based
This function is defined in `‘word_based’`. Following are details of this function. 
```
input: 
    sentence1 (source string), sentence2 (target string)    

output: 
    out:  
        a dict object which contain following items             
        'total_D':  The number of deletions required to convert sentence1 to sentence2             
        'total_I':  The number of insertions required to convert sentence1 to sentence2             
        'total_S':  The number of substitutions required to convert sentence1 to sentence2             
        'total_MED':  The minimum edit distance to convert sentence1 to sentence2  
        'WER':  The word error rate between sentene1 and sentence2
```
### Char Based
This function is defined in `‘char_based’`. Following are details of this function. 
```
input: 
    sentence1: a string 
    sentence2: a string output: 

out:  
    a dict object which contain following items             
        'total_D':  The number of deletions required to convert sentence1 to sentence2             
        'total_I':  The number of insertions required to convert sentence1 to sentence2             
        'total_S':  The number of substitutions required to convert sentence1 to sentence2             
        'total_MED':  The minimum edit distance to convert sentence1 to sentence2  
        'WER':  The word error rate between sentene1 and sentence2 
```

### Average Word Error Rate: 
 This function is defined in `‘avg_WER’`. Following are details of this function. 
```
input: 
    source_set:  the list of strings containing the source strings 
    target_set:  the list of strings containing the target strings 

output: 
    avg:  the average of Word error rate for whole input set 
```

## Euclidean Distance:
Implemented in `‘euclidean_distance’`. Following are details, 
```
input: 
    str1:  the text string 
    str2:  the text string 
    base:  the base on which vector will be made, char/word 
    measure:  the measure on which the values will be filled in vector, count/freq 

output: the computed distance 
``` 

## Manhattan Distance:
Implemented in `‘manhattan_distance’`. Details are same as Euclidean 
 
## Chebychev Distance:
Implemented in `‘chebychev_distance’`. Details are same as Euclidean 
 
## Cosine Similarity:
Implemented in `‘cosine_similarity’`. Details are same as Euclidean except that now that the output is similarity not distance and for distance I have implemented `‘cosine_distance’` function, the interface is same as above functions. 
 
## Jaccard Similarity:
Implemented in `‘jaccard_similarity’`. Details are same as Euclidean except that now the base can be `‘bigram’` as well and there is no `‘measure’` argument now, and that the output is similarity not distance and for distance I have implemented `‘jaccard_distance’` function, the interface is same as above functions. 
 
## Hamming Distance:  
Implemented in `‘hamming_distance’`. Details of interface are following, input: input1:  string or list of strings input2:  string or list of strings output: the hamming distance 
## Longest Common Subsequence:
Implemented in `‘LCS’`. Details of interface are following, 
```
input: 
    input1:  string or list of strings 
    input2:  string or list of strings 
output: 
    out:  a dict object containing,
        'size': the LCS size
        'sequence': the LCS 
```