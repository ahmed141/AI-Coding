# Naive Bayes Spam/Ham Classifer

### Dataset
Place `train` and `test` folders by extracting `Enron+dataset.zip` in `data` folder
The directory structure of dataset is as follow:  

    train/ 
        spam
        ham  
    
    test/  
        spam
        ham  

## Algorithmic Steps
Following are steps followed to train and test the Bayesian classifier on given data.

    1. Training model [Notebooks `Q01_prob01.ipynb`, `Q01_prob02.ipynb` and `Q01_prob03.ipynb` will be used in this step]
        a. Read corpus and calculate prior probability for spam and ham 
        b. Calculate the likelihood for each word in corpus 
    2. Testing model [[Notebook `Q01.ipynb` will be used for model testing]
        a. Made a function named `‘test_bayesian’`, it takes trained probs and the file name to be classified as spam/ham and returns predicted class name along with probability of it belonging to either class. 
        b. This functions tokenizes entire file and for each word if it is training vocabulary, it multiplies their probabilities in trained model. 

