
# coding: utf-8

# # Introduction to Artificial Intelligence for Non Computing

# ## Practical 4 (weeks 7 - 8)

# #### Theory Questions

# 1\.Symbolize the following proposition and discuss the truth.
# 1. Everyone has black hair.
# 2. Some people boarded the moon.
# 3. No one has boarded Jupiter
# 4. Students studying in the US are not necessarily Asians.

# Suppose M(x）：x is human
# 1.suppose F(x):x is black hair
# ∨x(M(x)→F(x))
# suppose a is red hair, M(a) is true, F(a) is faulse. M(a)→F(a) is faulse. So the proposition is faulse.
# 2. suppose G(x): x boarded the moon
# Exist x(M(x)∧G(x))
# suppose a boarded the moon, M(x)∧G(x) is true. Proposition is true.
# 3. suppose H(x) has boarded Jupiter
# Exist x(M(x)∧H(x))
# suppose a boarded the Jupiter, proposition is true.
# 4.F(x) is students studying in the US G(x) : x is Asian
# Allx(F(x)→G(x))
# proposition is true.
# 
# ***

# 2\.Judge the following formula, which is tautology? What is the contradiction?
# 1. ∀xF(x)⇒(∃x∃yG(x,y))⇒∀xF(x))
# 2. ￢( ∀xF(x)⇒∃yG(y))∧∃yG(y)
# 3. ∀x(F(x)⇒G(y))

# 1 is tautology. 2 is contradiction.
# ***

# 3\.Which of the following are correct?
# 1. False |=True.
# 2. (A ∧ B) |= (A ⇔ B).
# 3. (A ∧ B) ⇒ C |= (A ⇒ C) ∨ (B ⇒ C).
# 4. (A ∨ B) ∧ (￢C ∨￢D ∨ E) |= (A ∨ B).
# 5. (A ∨ B) ∧ (￢C ∨￢D ∨ E) |= (A ∨ B) ∧ (￢D ∨ E).

# 1,2，3 are correct.
# 
# ***

# 4\.Conjunctive normal form.link:https://baike.baidu.com/item/%E5%90%88%E5%8F%96%E8%8C%83%E5%BC%8F/2459360
# 1. Obtaining conjunctive paradigm: P∧(Q⇒R)⇒S
# #### Basic steps to find a conjunctive normal form.
# 1. Cut redundant connectives，Reserved {∨，∧，￢}
# 2. Move or remove the negation ~
# 3. distribution rates

# P∧(Q⇒R)⇒S ↔ P∧(￢Q∨R)⇒S ↔  ￢(P∧(￢Q∨R))∨S ↔ (￢P∧(￢￢Q∨R))∨S
# ↔ (￢P∧(Q∨R))∨S ↔ (￢P∨S)∧(Q∨R∨S)
# conjunctive normal form are ￢P∨S, Q∨R∨S 
# 
# ***

# 5\.Arithmetic assertions can be written in first-order logic with the predicate symbol <,the function symbols + and ×, and the constant symbols 0 and 1. Additional   predicates can also be defined with biconditionals.(Chapter 8.20)
# 1. Represent the property “x is an even number.”
# 2. Represent the property “x is prime.”
# 3. Goldbach’s conjecture is the conjecture (unproven as yet) that every even number is equal to the sum of two primes. Represent this conjecture as a logical sentence.
# 

# F(x): x is an even number G(x):x is prime
# ∀xF(x)⇒(∃x∃yG(x,y))
# 
# ***

# ### Programming Excercises

# 1\Please download the Pacman project from github,.there are two question need you to write about minimax algorithms and expectimax algorithms,then you will find one pdf,it's useful for you to solve the questions. named:prac4.pdf
# - this project named:prac4_alpha beta pruning_expectimax _algorithms_Multi-Agent Pacman

# 2\.Alpha Beta pruning on a Minimax tree.This is the tree we are working with tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
# (You can choose to do this question or not)
# - where
# - input is a list from input tree, see example in this file.
# - start is the root node number.  So, either 0 or 1 (0 if root is MAX, 1 if root is MIN)
# - upper is the upper limit for beta.  Set this to something higher than any value in your tree
# - lower is the lower limit for beta.  Set this to something less than any value in your tree
# - The function returns the root alpha and beta values, as well as the result, and the number of 'prunings' that took place.
# 

# In[ ]:


## write your answer here!

