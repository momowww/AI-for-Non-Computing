
# coding: utf-8

# # Weeks 13-14
# 
# ## Natural Language Processing
# ***

# Read in some packages.

# In[6]:


# Import pandas to read in data
import numpy as np
import pandas as pd

# Import models and evaluation functions
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics
from sklearn import cross_validation

# Import vectorizers to turn text into numeric
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Import plotting
import matplotlib.pylab as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Basic Feature Engineering
# We have examined two ways of dealing with categorical (i.e. text based) data: binarizing/dummy variables and numerical scaling. 
# 
# See the following examples for implementation in sklearn to start:

# In[7]:


data = pd.read_csv("data/categorical.csv")


# In[8]:


data


# ### Binarizing
# Get a list of features you want to binarize, go through each feature and create new features for each level.

# In[5]:


features_to_binarize = ["Gender", "Marital"]

# Go through each feature
for feature in features_to_binarize:
    # Go through each level in this feature (except the last one!)
    for level in data[feature].unique()[0:-1]:
        # Create new feature for this level
        data[feature + "_" + level] = pd.Series(data[feature] == level, dtype=int)
    # Drop original feature
    data = data.drop([feature], 1)


# In[9]:


data


# ### Numeric scaling
# We can also replace text levels with some numeric mapping we create

# In[7]:


data['Satisfaction'] = data['Satisfaction'].replace(['Very Low', 'Low', 'Neutral', 'High', 'Very High'], 
                                                    [-2, -1, 0, 1, 2])


# In[10]:


data


# ## Text classification
# We are going to look at some Amazon reviews and classify them into positive or negative.

# ### Data
# The file `data/books.csv` contains 2,000 Amazon book reviews. The data set contains two features: the first column (contained in quotes) is the review text. The second column is a binary label indicating if the review is positive or negative.
# 
# Let's take a quick look at the file.

# In[9]:


get_ipython().system('head -3 data/books.csv')


# Let's read the data into a pandas data frame. You'll notice two new attributed in `pd.read_csv()` that we've never seen before. The first, `quotechar` is tell us what is being used to "encapsulate" the text fields. Since our review text is surrounding by double quotes, we let pandas know. We use a `\` since the quote is also used to surround the quote. This backslash is known as an escape character. We also let pandas now this.

# In[11]:


data = pd.read_csv("data/books.csv", quotechar="\"", escapechar="\\")


# In[14]:



data.head()


# ### Text as a set of features
# Going from text to numeric data is very easy. Let's take a look at how we can do this. We'll start by separating out our X and Y data.

# In[15]:


X_text = data['review_text']
Y = data['positive']


# In[16]:


# look at the first few lines of X_text
X_text.head()


# Do the same for Y

# In[17]:


Y.head()


# Next, we will turn `X_text` into just `X` -- a numeric representation that we can use in our algorithms or for queries...
# 
# Text preprocessing, tokenizing and filtering of stopwords are all included in CountVectorizer, which builds a dictionary of features and transforms documents to feature vectors. 
# 
# The result of the following is a matrix with each row a file and each column a word. The matrix is sparse because most words only appear a few times. The values are 1 if a word appears in a document and 1 otherwise.

# In[19]:


# Create a vectorizer that will track text as binary features
binary_vectorizer = CountVectorizer(binary=True)

# Let the vectorizer learn what tokens exist in the text data
binary_vectorizer.fit(X_text)

# Turn these tokens into a numeric matrix
X = binary_vectorizer.transform(X_text)


# In[20]:


# Dimensions of X:
X.shape


# There are 2000 documents (each row) and 22,743 words/tokens.
# 
# Can look at some of the words by querying the binary vectorizer:

# In[21]:


# List of the 20 features (words) in column 10,000
features = binary_vectorizer.get_feature_names()
features[10000:10020]


# Spend some time to look at the binary vectoriser.
# 
# Examine the structure of X. Look at some the rows and columns values.

# In[22]:


# see the density of 0s and 1s in X
import scipy.sparse as sps
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.spy(X.toarray())
plt.show()


# Look at the sparse matrix above. Notice how some columns are quite dark (i.e. the words appear in almost every file). 
# 
# What are the 5 most common words?

# In[23]:


# your code here
value=X.toarray().sum(axis=0)
re=pd.Series(value)
re.index=features
re.sort_values(ascending=False)[0:5]


# Your answer here

# Write a function that takes the sparse matrix X, and gets the feature list from the vectoriser, and a document index (1 - 2000) and returns a list of the words in the file that corresponds to the index (the list should be obtained from the sparse matrix / bag of words representation NOT from the original data file). 

# In[25]:


# complete the function 
# returns vector of words / features
def getWords(bag_of_words, file_index_row, features_list):
    list_result=[]
    arr=bag_of_words.toarray()
    for i in range(0,22743):
        if(arr[file_index_row][i]==1):
            list_result.append(features_list[i])
        
    
    return list_result


getWords(X, 1, features)


# ### Modeling
# We have a 22743 features, let's use them in some different models.

# In[26]:


# Create a model
logistic_regression = LogisticRegression()

# Use this model and our data to get 5-fold cross validation accuracy
acc = cross_validation.cross_val_score(logistic_regression, X, Y, scoring="accuracy", cv=5)

# Print out the average accuracy rounded to three decimal points
print ("Mean accuracy of our classifier is " + str(round(np.mean(acc), 3)) )


# In[ ]:


Use the above classifier to classify a new example (new review below):


# In[27]:


new_review = [
    'really bad book!',
    'This is a nice book.',
    'This is the best book I had seem.',
    'And the fouth one.',
    'Is this the first document?',
]

Y1=[0,1,1,0,0]
X1_text=new_review
# Create a vectorizer that will track text as binary features
binary_vectorizer1 = CountVectorizer(binary=True)

# Let the vectorizer learn what tokens exist in the text data
binary_vectorizer1.fit(X_text)

# Turn these tokens into a numeric matrix
X1 = binary_vectorizer.transform(X1_text)
# Create a model
logistic_regression1 = LogisticRegression()

# Use this model and our data to get 5-fold cross validation accuracy
acc1 = cross_validation.cross_val_score(logistic_regression1, X1, Y1, scoring="accuracy", cv=2)

# Print out the average AUC rounded to three decimal points
print( "Accuracy for our classifier is " + str(round(np.mean(acc1), 3)) )



# Let's try using full counts instead of a binary representation (i.e. each time a word appears use the raw count value). 

# In[28]:


# Create a vectorizer that will track text as binary features
count_vectorizer = CountVectorizer()

# Let the vectorizer learn what tokens exist in the text data
count_vectorizer.fit(X_text)

# Turn these tokens into a numeric matrix
X = count_vectorizer.transform(X_text)

# Create a model
logistic_regression = LogisticRegression()

# Use this model and our data to get 5-fold cross validation accuracy
acc = cross_validation.cross_val_score(logistic_regression, X, Y, scoring="accuracy", cv=5)

# Print out the average AUC rounded to three decimal points
print( "Accuracy for our classifier is " + str(round(np.mean(acc), 3)) )


# Now try using TF-IDF:

# In[29]:


# Create a vectorizer that will track text as binary features
tfidf_vectorizer = TfidfVectorizer()

# Let the vectorizer learn what tokens exist in the text data
tfidf_vectorizer.fit(X_text)

# Turn these tokens into a numeric matrix
X = tfidf_vectorizer.transform(X_text)

# Create a model
logistic_regression = LogisticRegression()

# Use this model and our data to get 5-fold cross validation AUCs
acc = cross_validation.cross_val_score(logistic_regression, X, Y, scoring="accuracy", cv=5)

# Print out the average AUC rounded to three decimal points
print( "Accuracy for our classifier is " + str(round(np.mean(acc), 3)) )


# Use the tfidf classifier to classify some online book reviews from here: https://www.amazon.com/
# 
# Hint: You can copy and paste a review from the online site into a multiline string literal with 3 quotes: 
# ```
# """
# copied and pasted
# multiline
# string...
# """
# ```

# In[30]:


# your code here
review = [
    'This is a great book with great helpful tips.I bought one for myself and a couple others for gifts highly recommend.Thanks again Rich for all that you do to help us with tech.If you’re ever in the Pomona area you got a free lunch coming your way',
    'If you are using an iPhone for the first time, maybe. But not worth it for a seasone iPhone user.',
    'Great book! I love all the tips and a very easy read.',
    'I bought this book for the tips but when I followed the instructions for the tip that was most important to me, it was a bust. What was supposed to be shown on the screen, was not there. Perhaps because my phone is a 5S. It has to go back if it does me no good. Had high hopes but was disappointed.',
    'Just received my iPhone XR, this book helped me quite a bit, I learned a lot from it. The tip are very good and will use this as a reference.',
    'Best book ever. I am not real literate with my Apple phone and it is very easy to use. Highly recommended to all.',
    'This is Perfect! So much good information.I gave up the Blackberry and started with the iPhone4 then 5,6,7P and 8P and I’m still learning new things with this book. Great Gift!',
    'It is a fun read - easy to understand - I use it to try to learn something new one chapter at a time so I do not get overloaded with too much information'
]
X2_text=review
Y2=[1,0,1,0,1,1,1,1]
# Create a vectorizer that will track text as binary features
tfidf_vectorizer2 = TfidfVectorizer()

# Let the vectorizer learn what tokens exist in the text data
tfidf_vectorizer2.fit(X2_text)

# Turn these tokens into a numeric matrix
X2 = tfidf_vectorizer2.transform(X2_text)
#print(X2)
logistic_regression2 = LogisticRegression()

# Use this model and our data to get 5-fold cross validation accuracy
acc2 = cross_validation.cross_val_score(logistic_regression2, X2, Y2, scoring="accuracy", cv=2)

# Print out the average AUC rounded to three decimal points
print( "Accuracy for our classifier is " + str(round(np.mean(acc2), 3)) )


# ### Extending the implementation
# #### Features
# Tfidf is looking pretty good! How about adding n-grams? Stop words? Lowercase transforming?
# 
# We saw that the most common words include "the" and others above - start by making these stop words.
# 
# N-grams are conjunctions of words (e.g. a 2-gram adds all sequences of 2 words)
# 
# 
# Look at the docs: `CountVectorizer()` and `TfidfVectorizer()` can be modified to handle all of these things. Work in groups and try a few different combinations of these settings for anything you want: binary counts, numeric counts, tf-idf counts. Here is how you would use these settings:
# 
# - "`ngram_range=(1,2)`": would include unigrams and bigrams (ie including combinations of words in sequence)
# - "`stop_words="english"`": would use a standard set of English stop words
# - "`lowercase=False`": would turn off lowercase transformation (it is actually on by default)!
# 
# You can use some of these like this:
# 
# `tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=False)`
# 
# #### Models
# Next swap out the line creating a logistic regression with one making a naive Bayes or support vector machines (SVM). SVM have been shown to be very effective in text classification. Naive Bayes has been used a lot also.
# 
# For example see: http://www.cs.cornell.edu/home/llee/papers/sentiment.pdf
# 

# In[31]:


# Try different features, models, or both!
# What is the highest accuracy you can get?
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=False)

# Let the vectorizer learn what tokens exist in the text data
tfidf_vectorizer.fit(X_text)

# Turn these tokens into a numeric matrix
X = tfidf_vectorizer.transform(X_text)
#print(X)
# Create a model
logistic_regression = LogisticRegression()

# Use this model and our data to get 5-fold cross validation AUCs
acc = cross_validation.cross_val_score(logistic_regression, X, Y, scoring="accuracy", cv=5)

# Print out the average AUC rounded to three decimal points
print( "Accuracy for our classifier is " + str(round(np.mean(acc), 3)) )

