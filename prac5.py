
# coding: utf-8

# # Dealing with data
# 

# ## 1. The command line (Optional*)
# 
# PLEASE NOTE: TO RUN UNIX COMMANDS YOU SHOULD SELECT CORRECT OPTIONS WHEN INSTALLING GIT.
# 
# The command line is a text oriented way to perform operations with your operating system (looking at files, copying or creating folders, starting programs, etc). 
# 
# It can give you more control and provide a way to "look under the hood". In many cases, such as dealing with raw data files, the command line is faster. 
# 
# You should be familiar with the terminal or command line as well as some basic unix ("Bash") commands.
# 
# ![Terminal](images/terminal.png)
# 
# Note: MS Windows provides a different set of command line commands from Unix. Apple computers include the full set of Unix commands as the operating system is more closely based on Unix. Linux is an implementation of Unix. When you installed the Anaconda distribution you had the option to install the Unix commands onto your system as well. 

# ### 1.1. File system 
# To navigate the folder structure of the machine you are on you will typically use commands such as `ls` (list) and `cd` (change directory). You can make a directory with `mkdir` or move (`mv`) and copy (`cp`) files. To delete a file you can `rm` (remove) it. To print the contents of a file you can `cat` (concatenate) it to the screen.
# 
# Many commands have options you can set when running them. For example to get a listing of files as a vertical list you can pass the `-l` (list) flag, e.g. '`ls -l`'. During the normal course of using the command line, you will learn the most useful flags. The `-r` option is for recursive version of commands so that you can for example delete subfolders when you delete a directory with `rm -r` (be very careful with this command!).
# 
# If you want to see all possible options you can always read the `man` (manual) page for a command, e.g. '`man ls`'. When you are done reading the `man` page, you can exit by hitting `q` to quit.

# You can use shell commands in IPython notebooks by prefixing the line with an exclamation point!

# In[1]:


get_ipython().system('ls')


# In[2]:


get_ipython().system('mkdir test')


# In[3]:


get_ipython().system('ls -l')


# In[4]:


get_ipython().system('ls -l images/')


# In[5]:


get_ipython().system('cp images/terminal.png test/some_picture.png')


# In[6]:


get_ipython().system('ls test/')


# In[7]:


get_ipython().system("rm test/ # you can't delete a folder using `rm`!")


# In[8]:


# WARNING THIS WILL NOT CONFIRM!
get_ipython().system('rm -rf test/')


# In[9]:


get_ipython().system('ls -l')


# ### 1.2. Data manipulation and exploration
# Virtually anything you want to do with a data file can be done at the command line. There are dozens of commands that can be used together to almost anything you would think of! 
# 
# Lets take a look at the the file `data/users.csv`.

# Before we do anything, lets take a look at the first few lines of the file to get an idea of what's in it.

# In[10]:


get_ipython().system('head data/users.csv')


# Maybe we want to see a few more lines of the file,

# In[11]:


get_ipython().system('head -15 data/users.csv')


# How about the last few lines of the file?

# In[12]:


get_ipython().system('tail data/users.csv')


# We can count how many lines are in the file by using `wc` (a word counting tool) with the `-l` flag to count lines,

# In[13]:


get_ipython().system('wc -l data/users.csv')


# It looks like there are three columns in this file, lets take a look at the first one alone. Here, we can `cut` the field (`-f`) we want as long as we give the proper delimeter (`-d` defaults to tab).

# In[14]:


get_ipython().system("cut -f1 -d',' data/users.csv")


# That's a lot of output. Let's combine the `cut` command with the `head` command by _piping_ the output of one command into another one,

# In[15]:


get_ipython().system("cut -f1 -d',' data/users.csv | head")


# We can use pipes (`|`) to string together many commands to create very powerful one liners. For example, lets get the number of unique users in the first column. We will get all values from the first column, sort them, find all unique values, and then count the number of lines,

# In[16]:


get_ipython().system("cut -f1 -d',' data/users.csv | sort | uniq | wc -l")


# Or, we can get a list of the top-10 most frequently occuring users. If we give `uniq` the `-c` flag, it will return the number of times each value occurs. Since these counts are the first entry in each new line, we can tell `sort` to expect numbers (`-n`) and to give us the results in reverse (`-r`) order. Note, that when you want to use two or more single letter flags, you can just place them one after another.

# In[ ]:


get_ipython().system("cut -f1 -d',' data/users.csv | sort | uniq -c | sort -nr | head")


# After some exploration we decide we want to keep only part of our data and bring it into a new file. Let's find all the records that have a negative value in the second and third columns and put these results in a file called `data/negative_users.csv`. Searching through files can be done using _[regular expressions](http://www.robelle.com/smugbook/regexpr.html#expression)_ with a tool called `grep` (Global Regular Expression Printer). You can direct output into a file using a `>`.

# In[ ]:


get_ipython().system("grep '.*,-.*,-.*' data/users.csv > data/negative_users.csv")


# We can check the data folder to see if our new file is in there,

# In[ ]:


get_ipython().system('ls -l data')


# ## 2. Using Python, IPython, and Pandas
# The command line is great for a first step in data exploration. However, to do some more in depth operations you will generally want to move to a language and environment better suited for involved data manipulation. Here, we will discuss the use of Python as a data crunching tool.
# |
# In this section we will only discuss the use of `pandas` to explore data with data frames. You can also explore data line by line by "streaming" it; but that is beyond this class. Streaming in data is very useful for highly unstructured data. If you are interested in this, feel free to ask about it on the class forums!

# ### 2.1. Example one: User exploration

# For structured data like we have here, we will use `pandas`.

# In[3]:


# Read in data/users.csv using Pandas
import pandas as pd
users = pd.read_csv("data/users.csv")


# In[4]:


# Take a look at the Panda's DataFrame
users.head()


# In[ ]:


# Add another column to this DataFrame
users['sum'] = users['variable1'] + users['variable2']
users.head()


# Python and Pandas allow us to do complex tasks very easily, such as plotting.
# 
# Let's visualize the relationship between variable1 vs. variable2 in these data with a scatterplot.

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.scatter(users['variable1'], users['variable2'])


# We can update our DataFrame given the new information we discovered.

# In[ ]:


users.columns = ['user', 'feature1', 'feature2', 'sum']
users.head()


# ### 2.2. Example 2: Survey responses
# Let's read in an edited version of your survey responses. Since the data is very well structured (it's a nicely formatted .csv file) we will simply use `pandas`. This file is located in the `data/` folder.

# In[ ]:


survey = pd.read_csv('data/survey.csv')


# Now that we have the data, let's take a look at what we have.

# In[ ]:


survey.head()


# We have a lot of data here. How can we start to make sense of it? Using the pandas `describe()` method, we can get a summary of the numeric features.

# In[ ]:


survey.describe()


# You might find it easier to flip the data frame,

# In[ ]:


survey.describe().transpose()


# Do we have other features that weren't listed here? Some that aren't numeric? Let's take a look.

# In[ ]:


survey.columns


# There are more fields here than we saw in our description. If we go back and look at the head of the data, we will see a few fields are Yes/No. Let's turn these into 0's and 1's.

# In[ ]:


for field in ['regression', 'database', 'cloud', 'api']:
    survey[field] = (survey[field] == "Yes").astype('int')


# In[ ]:


survey.describe().transpose()


# We have already seen how to get scatter plots in the previous example. Let's look at a histogram here.

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.hist(survey['terminal'], bins=range(1, 11))
plt.ylabel('Count')
plt.xlabel('Rank')
plt.show()


# Let's look at one more type of plot. A very simple line graph. Maybe we are curious about the trend of experience given the timestamp a student submitted their survey. In our data, we have a `timestamp` field as well as all of the experience reports. Let's put a few on a graph and take a look.

# In[ ]:


plt.plot(survey['timestamp'], survey['terminal'], label="Terminal")
plt.plot(survey['timestamp'], survey['business'], label="Business")
plt.plot(survey['timestamp'], survey['machinelearning'], label="Machine Learning")
plt.ylabel("Experience")
plt.xlabel("Time Submitted")
plt.legend()
plt.show()


# ## 3. Getting data from the internet

# This section looks at obtaining data are loading it into Python.

# ### 3.1. Excercise: Downloading the Iris dataset

# One of the most famous datasets in Machine Learning is the Iris dataset. We looked at it in lectures, it is referred to in the text book, it is used in many publications. 
# 
# First lets download it from the UCI Machine Learning repository: http://mlearn.ics.uci.edu/MLRepository.html

# We make use of urllib. It is a python library that is part of the base package - it is for downloading urls. 
# 
# Read the doc! 
# https://docs.python.org/3/library/urllib.html#module-urllib

# In[20]:


import urllib.request
import pandas as pd
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = urllib.request.urlopen(url)
data = response.read()      # a raw bits 'bytes' object
text = data.decode('utf-8') # use the utf-8 string format to create a string 'str' object 
iris_df=pd.read_csv(url, names=("sepal length","sepal width","petal length","petal width","class")) # Panda object


# #### Take a look at the file contents

# In[21]:


text


# ### 3.2. Decision Tree Learning with sklearn

# In[22]:


iris_df[:].head()


# Please refer to the Panda documentation during this practical.
# 
# read csv method doc: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
# 
# Some information on merging and combining data frames is at the following link: https://pandas.pydata.org/pandas-docs/stable/merging.html

# In[23]:


import matplotlib.pyplot as plt
x = iris_df["sepal length"]
y = iris_df["sepal width"]
iris_df["class"]
colors = {'Iris-setosa':'red', 'Iris-virginica':'blue', 'Iris-versicolor':'green'}

plt.scatter(x, y, c = iris_df["class"].apply(lambda x: colors[x]))

#labels
plt.xlabel('sepal length')
plt.ylabel('sepal width')


plt.show()


# Produce a 3-D plot using matplotlib. 
# 
# You should refer to the matplotlib documentation for 3d plotting - see https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
# 
# ![Iris](images/iris.png)
# 

# In[24]:


## put your plotting code here
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = iris_df["sepal length"]
y = iris_df["petal length"]
z = iris_df["petal width"]
classes = iris_df["class"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = {'Iris-setosa':'red', 'Iris-virginica':'blue', 'Iris-versicolor':'green'}

for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i], c=colors[classes[i]])

#labels
ax.set_xlabel('sepal length')
ax.set_ylabel('petal length')
ax.set_zlabel('petal width')

plt.show()


# The plot shows the values of two attributes of Iris and indicates the flower class by color.
# 
# Now we learn a decision tree to classify the iris dataset.
# 
# Please read the documentation for Decision Trees in sklearn http://scikit-learn.org/stable/modules/tree.html#tree-classification

# In[25]:


from sklearn import tree

attributes = iris_df[["sepal length","sepal width","petal length","petal width"]]
target = iris_df[["class"]]

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(attributes,target)


# We can use the decision tree for prediction.
# 
# First lets predict the values of a feature vector containing [1,1,1,1]:

# In[26]:


clf.predict([[1,1,1,1]])


# Okay was predicted to be versicolor.

# Now try predicting the values of the whole dataset that was used for learning the decision tree and compare with original training data:

# In[27]:


prediction = clf.predict(attributes)
prediction_df = pd.DataFrame({"prediction": prediction})
prediction_df.head()

# create a result that contains the training data classes and the prediction result
# use the pandas function concat to join the data frames - note the axis parameter means to join columns
training_result = pd.concat([prediction_df, target], axis=1)
training_result.head()


# How can we work out the percentage of correctly classified examples - that is where prediction is equal to the target class in Python?

# In[28]:


# write the code to calculate the misclassifications here...
# calculate the proportion of records where the predicted class is not equal to the actual class
num_rows = training_result['prediction'].count()
# note vectorized operation to compare prediction with class also sum((true,false,true)) equals 2
num_incorrect =  num_rows - sum(training_result['prediction'] == training_result['class']) 
percentage = num_incorrect /  num_rows
percentage


# #### Training data

# You will have noticed there was a very high correspondance between the target and the classification by the decision tree which is not surprising given the decision tree was learned from this information.
# 
# What if we don't use all of the training data for learning the decision model?
# 
# In the following we use every second line in the original data file to learn the decision tree that is based on only half the data (the example uses every second row to learn the decision tree):

# In[ ]:


attributes_training = attributes[attributes.index % 2 != 0]  # Use very 2rd row, exclude every second element starting from 0 
                                                            #(note: % is the modulo operator)
target_training = target[target.index % 2 != 0] # every second row

# learn the decision tree
clf2 = tree.DecisionTreeClassifier(criterion='entropy')
clf2 = clf.fit(attributes_training,target_training)


# Now lets use this model for prediction

# In[29]:


attributes_test = attributes[attributes.index % 2 != 1]  # Use very 2rd row, exclude every second element starting from 0 
                                                            #(note: % is the modulo operator)

prediction = clf.predict(attributes_test)
prediction_df_1 = pd.DataFrame({"prediction": prediction})
prediction_df_1.head()



# To evaluate how good the decision tree is at making predictions on "new", unseen data (that is unseen during the process of constructing the model) compare the actual value of the target (ie the one in the file) with decision tree predictions.

# In[30]:


actual_class_test = target[target.index % 2 != 1] 
actual_class_test.index=range(75)

training_result = pd.concat([prediction_df_1, actual_class_test], axis=1)

training_result


# Looking at the above you can quickly observe the results of the prediction differ from the original dataset. 
# 
# Use your method to calculate the misclassification percentage to evaluate the decision tree classifier

# In[31]:


num_rows = training_result['prediction'].count()
# note vectorized operation to compare prediction with class also sum((true,false,true)) equals 2
num_incorrect =  num_rows - sum(training_result['prediction'] == training_result['class']) 
percentage = (num_incorrect /  num_rows )*100
print ("Error rate = {:f} percent".format(percentage))


# ## 4. Exercise

# Now download another dataset from the UCI Machine Learning Repository and perform a similar analysis.
# 
# Make sure to choose one the classification problems: https://archive.ics.uci.edu/ml/datasets.html?format=&task=cla&att=&area=&numAtt=&numIns=100to1000&type=&sort=nameUp&view=table
# 
# It would be a good idea to have a look also at the dataset in your browser to find one using csv format :-)
# 
# 1. First perform some initial examinations of the data using head etc
# 1. Then generate summary statistics
# 1. Next generate some plots to visualise the data
# 1. Then learn a decision tree classifier 

# In[2]:


# You can put your code here and try to make it easy for another person to read.
# For the final version you probably don't need more than one cells for each of the 
# points 1-4 above. Make sure to delete  empty cells when you are finished using the little 
# sissors icon at the top


# ## 5. Going forward
# Spend some time to go over the work in this and the previous tutorial to become confortable with the material. Also don't worry too much if you are not quite comfortable with parts 3 and 4. Programming in Python, and programming generally, requires frequent consulting of docs and searching online especially when you are starting out with a new tool.
