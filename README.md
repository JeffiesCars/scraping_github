# Project Goal: 
Create a machine learning model, using sklearn, that predicts the main programming language used in a GitHub repository, based on the text from the repositories README file.

## Programming Language Used for Analysis:  
Python, Jupyter Notebook

## Acquire:

Github collections were scraped at random to obtain repository names along with the text from their README files and the primary programming language used.  

## Preparation:



## Exploration:



## Modeling:



## Conclusion: 
K-Nearest Neighbors worked the best out of all the models with a train accuracy of 67% and a test accuracy 63%. This was with the hyperparameter number of neighbors, equal to 5 (n_neighbors = 5).

The model can be improved by adding more repositories in order to get a more representative sample of GitHub repos.  Scaling the list of repos should lead to logarithmic improvements in the model, meaning it should get ever diminishing returns until it peaks at a certain value and never passing it.