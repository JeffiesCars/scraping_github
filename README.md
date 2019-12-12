# Project Goal: 
Create a machine learning model, using sklearn, that predicts the main programming language used in a GitHub repository, based on the text from the repositories README file.

## Programming Language Used for Analysis:  
Python, Jupyter Notebook

## Data Dictionary

   - **Language:** Programming language used for repositort project

   - **README Content:** Description of each repository containing keywords used to make predictions

   - **Normalized:** README content normalized removing any uppercased characters, special characters, non-alpha characters, and alpha strings with 2 or less characters

   - **Stemmed:** README content reducing each word to its root stem 

   - **Lemmatized:** README content reducing each word to its root word

   - **Cleaned:** README content that has been lemmatized and then removes any stopwords

## Acquire:
Github collections were scraped at random to obtain repository names along with the text from their README files and the primary programming language used.  

## Preparation:
We created a prepare.py file with several functions in it to clean up our data. 
- Our 'basic clean' function removed non-ASCII characters, strips whitespace and replaces newline characters with a space.
- Our 'normalize' function converts to all letters to lowercase, normalizes the unicode characters, removes any non-alpha or whitespace characters and removes any alpha strings with 2 characters or less.
- Our 'tokenize' function breakes down the text into discrete units.
- Our 'stem' function takes in a string and returns the root stem of each word. 
- Our 'lemmatize' function takes in text and returns the root word of every word.
- Our 'remove_stopwords' function removes any articles, prepositions and conjunctions in the text. 

## Exploration:
We broke down each README file into single words to then explore the length of each repo and search for most common words used in each language. We used various graphs and word clouds to visualize our data. We also broke the data into bigrams and ngrams (3) to see what words are most commonly used together.
Then we used the TF, IDF, TF-IDF in order to create features for modeling.

## Modeling:
We used 8 different models, Logistic Regression, Decision Tree, Random Forest, Support Vector Machine, K-Nearest Neighbors, AdaBoost, Bagging and Stochastic Gradient Descent.

## Conclusion: 
K-Nearest Neighbors worked the best out of all the models with a train accuracy of 67% and a test accuracy 63%. This was with the hyperparameter number of neighbors, equal to 5 (n_neighbors = 5).

The model can be improved by adding more repositories in order to get a more representative sample of GitHub repos.  Scaling the list of repos should lead to logarithmic improvements in the model, meaning it should get ever diminishing returns until it peaks at a certain value and never passing it.
