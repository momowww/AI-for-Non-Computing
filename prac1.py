
# coding: utf-8

# # Introduction to Artificial intelligence for Non Computing 

# ## Practical 1

# This is the first tutorial.
# 
# We introduce the basics of programming in Python and some tools to organise your programs (IPython). We will use Python throughout the course in most of the prac classes. In addition to this tutorial, if you have not had experience in programming, please spend some time learning in the courses or links provided. 

# ### Python Overview

# Python is a programming language that has been growing in popularity in recent years. There are many reasons for this, but it mostly comes down to Python being easy to learn and use as well as the fact that Python has a very active community that develops amazing extensions to Python!
# 
# Python has become one of the most frequently used languages in the world of data science due to the ability to almost instantly apply it to a large number of data science problems. When asking companies in different industries and of various sizes what lanuage they would like their data scientists to know when coming in, they almost all agree that Python is the best choice. 
# 
# Some of you may have had experience in Java. Both share many characteristics given they are both programming languages and many structures and concepts will be familiar. However, there are differences. You may find you prefer python and it may allow you to be more productive, not just because of the provision of many libraries which implement Data Mining algorithms. 
# 
# Some key differences between Python and Java are:
# - Python is dynamically typed while Java is statically typed, this has various implications including you never need to declare variables in Python
# - Python code is more concise (briefer)
# - Python is more compact
# 
# For example, the following program is in Java:
# <br>
# public class HelloWorld
# <br>
# {
# <br>
#     public static void main (String[] args)
#     <br>
#     {
#     <br>
#         System.out.println("Hellold!");
#         <br>
#     }
#     <br>
# }
# <br>
# 
# In Python the equivalent program is 
# <br>
# print("Hello, world!") # Python version 3
# 

# ### Python? IPython? IPython notebooks? What is all of this?

# What is all of this? 
# - Python? 
# - IPython? 
# - IPython notebooks?
# 
# For you, these terms may be confusing? Don't worry its ok... 
# 
# Python is a lanuage. A computer programming language. It is very popular in lots of industries. It has been around for over 30 years. Development of Python started in December 1989 by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands.
# 
# IPython (with an I) is an extension to Python. It was created by scientists for scientists. It is typically used in computer science, machine learning, and physics research. It simply adds some new features to Python.
# Writing code in either of these is generally done in a long text document with a ton of code that can be pretty duanting to a someone new to the world of programming.
# 
# IPython Notebooks (with an I, there is no such thing as a Python notebook) is what we are looking at right now. It is a web browser based way of writing Python code. One of the benefits is that it allows you to write in plain text to create, what should feel like, a notebook. The closest analog here would be to relate an IPython notebook to a typical lab notebook kept by "traditional" researchers. Anyone coming from chemistry or biology will probably understand what I mean.
# We will be using IPython notebooks for the rest of the semester. A majority of your class notes will be presented in this format. This will allow us to both have a place for discussion and instruction, but with the added benefit of allowing us to play with data live! 
# 
# The rest of this document will be broken into two main pieces: an introduction to IPython notebooks (how to use them) and then an introduction to the world of Python programming.

# ### Using IPython Notebooks

# IPython notebooks are made up of cells. There are two basics types of entries in an IPython notebook: text cells, and code cells.
# 
# You can edit a cell by double clicking on it. You can get it back to the display mode by pressing the "Run" button from the toolbar. Try it! To switch between text and code cells, just click a cell and go to "Cell > Cell Type" in the menu bar (or use the toolbar).

# #### Text Cells

# Let's start a new cell and add a little bit more text.
# 
# You can do text formatting. For example, you can use asterisks or underscores to emphasize things. Double asterisks are used to make things bold.
# 
# If you know what LaTeX is, you can write directly in LaTeX by wrapping it in dollar signs, $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Learning $\LaTeX$ is great for typesetting math formulas.
# 
# Creating a bulleted list is pretty easy:
# - One
# - Two
# - Three
# 
# It is also very easy to make a numbered list:
# 1. One
# 1. Two
# 1. Three
# 
# For a numbered list, start with 1. followed by a space, then it starts numbering for you. Start each line with some number (any number) and a period, then a space. Tab to indent to get subnumbering.
# 
# This covers almost all of the text formatting you will need to learn. If you are ever stuck, just Google "Markdown syntax" since the language the formatting is done in is called Markdown.

# #### Code Cells

# Now, we will see a "code" cell. Here, we simply type any Python code and then click "Run". When we run a cell, the code in it is executed and remembered for as long as we keep this window open - this means if you create a variable in a code cell you can refer to the variable by its name in other subsequent cells. Code cells will always start with "In [ ]:". Code cells are the default for any new cell.

# In[4]:


x = 5 + 10


# In[7]:


print (x)


# You can include more complex expressions or programs in a cell as well:

# In[9]:


x = 5 + 1
print ("The value of x is " + str(x) + ".")
print ("Output: Hi! This is a cell. Press the ▶| button above to run it")


# Instead of clicking "Play" button, you can run a cell with Ctrl + Enter or Shift + Enter. 
# <br>
# Experiment with both of those to see what the difference is.

# ### Python

# Let us now examine some of the key elements of Python

# #### Variables and data types

# Variables are used to store data. This data can be of a variety of types. Integer numbers, floating (decimal numbers), lists, strings, etc. Let's take a look at some of these:

# In[8]:


some_integer = 5
some_float = 7.1
some_list = [1, 2, 3, 4]
some_string = "Rob"


# We can print out these variables.

# In[9]:


print (some_integer)
print (some_float)
print (some_list)
print (some_string)


# What if I want to print some text and then some numbers? One easy way to do this is to realize that printing will always want string data. If you have data that is not a string (like an integer or float), you can convert it to a string.

# print ("My integer was " + str(some_integer) + ".")

# It is always a good practice to convert everything to a string when printing it out such as by using the function str().
# 
# Now we look at some basic maths.

# In[12]:


some_integer + some_float


# We can store this as a new variable to use later,

# In[15]:


my_sum = some_integer + some_float


# In[17]:


print (my_sum)


# What about that list we had? What does that mean? A list is exactly what it sounds like. It's a way to keep a collection of things in order. We can check to see how long our list is,

# In[19]:


print( len(some_list) )


# This looks good. Our list contained the numbers 1 through 4. What if we want a particular item from the list? How do we look at just the first item? To do a lookup, we use square brackets. Notice that when we created the list originally, we also used square brackets!

# In[20]:


print( some_list[1] )


# That's the second item, not the first! In Python (and almost every other language), counting start at zero! To get the first item we should look in the 0th space,

# In[22]:


print( some_list[0] )


# Adding things to the list is done using the append method,

# In[23]:


some_list.append(5)


# In[24]:


print (some_list)


# In[ ]:


# Play around here!
# By the way, the pound (hash) symbol here is used to indicate a comment in code.


# #### Functions

# We have already used these twice! Functions allow us to do predefined operations. Functions are usually some sensible English word ending in open-and-close parentheses. One example is the s

# In[25]:


str(5.124)


# We also used the append() function to add stuff to a list.
# 
# If we knew we had to do some operation many times, and wanted to save a bit of time, we could define our own function. For example, consider having to calculate the area of a circle.

# In[26]:


def area_of_a_circle(radius):
    area = 3.14 * radius * radius
    return area


# In[28]:


circle_area = area_of_a_circle(5)
print( circle_area )


# This function was helpfully named "area_of_a_circle", it takes one argument that we will call radius. It then uses this radius to get the area and then returns it. Now, whenever I want to get the area of some circle, I simply call area_of_a_circle() and place the radius in the middle of the parentheses.
# 
# Python has many functions, but we will be writing our own very often.

# #### Loops

# We will be doing a lot of repetative things in Python. This doesn't mean we need to do a ton of copy and pasting, though. We can use loops to make this easy. For example, if we wanted to square each

# In[30]:


for number in [1, 2, 3, 4, 5]:
    print (number * number)


# The range function makes this even easier,

# In[31]:


for number in range(5):
    print (number * number)


# Not exactly the same... the range function will start from 0 and go to the last number minus one. We can fix this by telling it to start at 1:

# In[33]:


for number in range(1, 6):
    print (number * number)


# We aren't limited to this, let's bring in another list:

# In[38]:


names = ["Robert", "John", "Sarah", "Qian", "Ahmad"]
ages = [26, 31, 29, 24, 30]

for i in range(len(names)):
    print (str(names[i]) + " is " + str(ages[i]) + " years old.")


# #### Conditionals

# Sometimes we want to check something before deciding what to do next. For example,

# In[39]:


def is_best_prof(name):
    if name == "Adam":
        return "Yes!"
    else:
        return "No!"


# In[42]:


print (is_best_prof("Adam"))


# In[44]:


print (is_best_prof("John"))


# #### Packages

# Python has a ton of packages that make doing complicated stuff very easy. We won't discuss how to install packages, or give a detailed list of what packages exist, but we will give a brief description about how they are used. An easy way to think of why package are useful is by thinking: "Python packages give us access to MANY functions!"
# 
# In this class we will use four packages very frequently: pandas, sklearn, matplotlib, and numpy:
# 
# - pandas is a data manipulation package. It let's you store data in data frames. More on this next class.
# - sklearn is a machine learning and data science package. It let's you do fairly complicated machine learning tasks, such as running regressions and building classification models with only a few lines of code!
# - matplotlib let's you make nice looking plots.
# - numpy (pronounced num-pie) is used for doing "math stuff" such as complex math operations (e.g., square roots, exponents, logs) and give you complex matrix operation abilities.
# If it's confusing as to why this is useful, don't worry. As we use them throughout the semester, their usefulness will become apparent.
# 
# To make the contents of a package useful, you need to import it:

# In[48]:


import pandas
import sklearn
import matplotlib
import numpy


# We can now use some package specific things. For example, numpy has a function called sqrt() which will give us the square root of a numpy. Since it is part of numpy, we need to tell Python that's where it is by using a dot.

# In[49]:


numpy.sqrt(25)


# You may have noticed that earlier, when we added stuff to our list, we used .append(). This is very similar! Here, we told Python that numpy had a function called sqrt() that we would like to use. Earlier, we told Python that our list (and all lists!) had a function called append() that we would like to use.
# 
# That's all we say about packages for now. Soon, we will be using packages in every class. With practice, you will understand why they are so great!

# ### Tips for Writing Code in IPython Notebooks

# IPython notebooks make writing Python code easy and neat.

# #### Auto complete

# One of the most useful things about IPython notebook is its tab completion.
# 
# Try this: click just after numpy. in the cell below and press Tab several times, slowly to view candidate functions you might want to call

# In[ ]:


# im 


# In[ ]:


numpy.  


# #### Organisation

# We typically read IPython notebooks from top to bottom. This means that if a cell relies on a variable or function that was created earlier in the notebook, you must run the corresponding cell to make that information available! For example, if I set the variable  age equal to 26 in the next cell,

# In[53]:


age = 26


# but don't run it, it will not be available in the next cell:

# In[55]:


print ("I am " + str(age) + " years old!")


# Now, this does not mean you have to run everything from top to bottom. You could define age later in the notebook, and then scroll up and run any other cells that require it. However, this is bad practice. How is someone supposed to know to scroll down first!? The IPython notebook will always remember the cells in the order you run them. This means you can overwrite variables!

# In[57]:


gender = "male"


# In[58]:


print (gender)


# In[1]:


gender = "female"


# In[62]:


print (gender)


# This can get confusing. Notice that the number in the "In [#]:" statement will always increase by one for every cell you run. This will make keeping track of everything a little easier. But it is recommended to always recommend organizing from top to bottom.

# #### Saving

# There is an autosave feature and you can also use the save button in the menu or toolbar.

# ### Further Information - Use these links to find tutorials and other information to help you code

# The resources here are endless; but people learn things in different ways. Some people prefer books, others like being taught through lessons, and others just learn by doing. I, unfortunately, learn by doing which means that I'm not an expert on which resources are the best.
# 
# - <a href="http://www.icourse163.org">icourse163.org</a> has python courses.
# - <a href="https://www.codecademy.com/learn/python">Codecademy's Python Course</a> will give you a great foundation for Python.
# - The online book, <a href="http://www.diveintopython.net/toc/index.html"> Diving into Python</a>, has proven to be useful for many people. 
# - ...
# - Personally, I try to think of a cool project I want to work on and I just try to do it. For example, trying to build a simple interactive text game can be fun. Since you are just jumping in and doing Python, this will lead to a ton of furious searching online. This is normal. This is actually how professional programmers work every day... <a href="http://stackoverflow.com">Stackoverflow.com</a> for instance has an answer to any programming question you can imagine!
# 
# Feel free to find other sources of information that are helpful for you (about Python or programming)

# ### Coding Questions

# To master your new found knowledge of Python, you should try these hands-on examples. 

# 1\. Create a list of 5 fruits (make sure to include an apple).

# In[3]:


my_list = ["watermelon", "pear", "apple", "grape","orange"]
my_list


# 2\. Go through each fruit and check if it is an apple. If it is, print out "I found it!". If it's not an apple, do nothing.

# In[4]:


for  fruit in my_list :
    if (fruit == "apple"):
        print ("found it!")


# 3\. Add two new fruits to your list.

# In[5]:


my_list.append("bannana")
my_list.append("kiwi")
my_list


# 4\. Create a new empty list. Go through your list of fruits, and for each one, add an entry to the new list that tells us how many letters each fruit name is.

# In[6]:


for  fruit in my_list :
    print ("{:s} has {:d} letters".format(fruit,len(fruit)))


# 5\. Make a function called half_squared that takes a list and returns a new list where each element of the original is squared and then divided in half.

# In[35]:


def half_squared(input_list):
    output_list = [] # What should we do?
    for element in input_list:
        output_list.append((element*element)/2)
    return output_list


# In[36]:


## test the function
half_squared([3,3]) == [4.5,4.5]


# 6\.   Read the following program:

# In[1]:


a = int(input("input first number: "))
b = int(input("input second number: "))
if(a > b):
    print(a)
else:
    print(b)


# What does the following program print? And you can input two number in the program to verify your answer. What does the program do???

# Now practice writing a program that takes as input some students scores and then outputs a grade (A, B, C). 
# 
# If scores >=90 points are represented by A, 60-89 points are represented by B, and 60 points or less are indicated by C.
# 
# If the input student score is less than 0 greater than 100, make an error message for the user.
# 
# You can look at the following links to see how other people have writen similar programs: https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/live?lessonId=1051260552&courseId=1004987028

# In[2]:


score = int(input('input score:\n'))
if score >= 0 and score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'
    print ('%d belong to %s' % (score,grade))
else:
    print("The score you entered is wrong.Please re-enter.")


# 7\. Read the following program 

# In[7]:


def exchange(a,b):
    c = a
    a = b
    b = c
    return a,b


# This program is an example of writing a function,it takes two variables a and b in that order and returns them as a tuple in reversed order (b,a). 
# 
# Once a function is declared it can be used in other code:

# In[8]:


exchange(10,20)


# Python code can be writen very concisely, for example the following is an alternative way to write the same program:

# In[3]:


def exchange(a,b):
    a,b=b,a
    return a,b


# In[4]:


exchange(10,20)


# Now using what we just learned try to write a program to take 3 numbers as input and sort them from large to small.
# 
# For example  $revSort(12, 4, 32)$ will return (32, 12, 4)

# In[5]:


n1 = 12
n2 = 4
n3 = 32
   
def swap(p1,p2):
    return p2,p1
     
if n1 < n2 : n1,n2 = swap(n1,n2)
if n1 < n3 : n1,n3 = swap(n1,n3)
if n2 < n3 : n2,n3 = swap(n2,n3)
            
print (n1,n2,n3)


# 8\.Read the following program

# In[30]:


list1 = [1,2,3]
list2 = [4,5,6]
array = [list1,list2]


# In[31]:


array


# we have created a two-dimensional array through the above progrem,can you traverse this two-dimensional array?
# For example $arrs = [[1,2,3],[4,5,6]]$ will return 1 2 3 4 5 6

# In[ ]:


num_list = [[1,2,3],[4,5,6]]
for i in num_list:
    for j in i:
        print(j)


# 9\. Read the following program

# In[32]:


a = [1,2,3,4]
def f(x):
    return x*2  #it is means 1*2 2*2 3*2 4*2
for i in map(f,a):
    print(i)


# In[33]:


a = [1,2,3,4]
def f(x):
    return x**2  #it is means 1^2 2^2 3^2 4^2
for i in map(f,a):
    print(i)


# look at above program,it will be userful for your to writing a program.it's a good program to explaination the map function

# Observe the following phenomenon: calulate the cube of some number (e.g., 1, 8, 17) , the sum of all digits in this cube equals to the number itself.（the max num is 100,and you should use the map function from above）
# - 1^3 = 1
# - 8^3  = 512  ->   5+1+2=8
# - 17^3 = 4913 ->   4+9+1+3=17

# In[5]:


for i in range(1,100):
    if i ==sum(map(int,str(pow(i,3)))):
        print(i)


# 10\. Read the following program

# In[11]:


import random
x = random.randint(3,9)
print(x)


# In[12]:


import random
x = random.randint(3,9)
print(x)


# In[2]:


import random
x = random.uniform(3,8)
print(x)


# they are the same code but you can get different result by using the random module

# Use the random module to generate two random integers x, y (1-10) and print them value, then exchange them value each other,and print them.

# In[2]:


import random

def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = random.randint(1,10)
    y = random.randint(1,10)
    print ('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print ('x = %d,y = %d' % (x,y))


# 11\. Read the following program

# In[5]:


print("   *   ")


# we can print space use the print function

# Please look at the following rules, code output,you can just use the print() without othething,but we will give the loop nesting code to print the diamond.

# In[4]:


#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *


# In[3]:


print("   *")
print("  ***")
print(" *****")
print("*******")
print(" *****")
print("  ***")
print("   *")


# 12\. Read the following program
# 

# Please read following program,and find some rules.
# - 123456
# - 23456
# - 3456
# - 456
# - 56
# - 6

# In[5]:


for i in range(1,7):
    for j in range(i,7):
        print(j,end="")
    print()


# Please look at the following rules, Using for loop nested output.
# - 123456
# - 234561
# - 345612
# - 456123
# - 561234
# - 612345

# In[4]:


for i in range(1,7):
    for j in range(i,7):
        print(j,end="")
    for l in range(1,i-1+1):
        print(l,end="")

    print()


# 13\. Read the following program

# In[10]:


#title()
players = "charles"
print(players.title())


# In[11]:


# Slice
players = ['charles','martina','michael','florence','eli']
print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-3:-1])


# use the for loop to slice the list ,and The first letter of the output list is capitalized. $players = ['charles','martina','michael','florence','eli']$    For example Charles Martina ...

# In[12]:


players = ['charles','martina','michael','florence','eli']
for player in players[:3]:
    print(player.title())

