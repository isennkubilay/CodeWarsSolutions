#!/usr/bin/env python
# coding: utf-8

# ## Valid Parentheses
# 
# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# 
# Examples:
# 
# `"()"              =>  true`
# 
# `")(()))"          =>  false`
# 
# `"("               =>  false`
# 
# `"(())((()())())"  =>  true`
# 
# 

# In[13]:


def isValidParent(strr):
    n = 0
    for i in range(len(strr)):
        if strr[i] == "(":
            n+=1
        if strr[i] == ")":
            n-=1
        if n<0:
            return False
    return n == 0


# In[14]:


isValidParent("(())((()())())")


# ---

# ## Moving Zeros To The End
# 
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# 
# Example:
# 
# `move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]`
# 
# 

# In[1]:


def move_zeros(array):
    new = []
    zeros = []    
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: 
                new.append(array[i])
        else:
            new.append(array[i])
    
    return new + zeros


# In[2]:


move_zeros([1, None, 2, 1, 0, False, 0])


# ---

# ## Memoized Fibonacci
# 
# `def fibonacci(n):`
# 
#         if n in [0, 1]:
# 
#             return n
#         
#         return fibonacci(n - 1) + fibonacci(n - 2)
# 
# 
# This algorithm serves welll its educative purpose but it's tremendously inefficient, not only because of recursion, but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).
# 
# This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars you will most likely get a code timeout before any answers.
# 
# For this particular Kata we want to implement the memoization solution. This will be cool because it will let us keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an answer very rapidly.
# 
# The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached number.
# 
# Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies of tree recursion Can you make it so the memoization cache is private to this function?
#     
# 
# 
# 
# 

# In[33]:


memo = {}
def fibonacci(n):
    if n in [0, 1]:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


# In[35]:


fibonacci(100)


# ---

# ## Human Readable Time
# 
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# 
#  - HH = hours, padded to 2 digits, range: 00 - 99
#  - MM = minutes, padded to 2 digits, range: 00 - 59
#  - SS = seconds, padded to 2 digits, range: 00 - 59
# 
# The maximum time never exceeds 359999 (99:59:59)
# 
# Example:
# 
# (60) --> "00:01:00"

# In[3]:


def make_readable(seconds):
    hours = int(seconds/3600)
    minutes = int(seconds%3600/60)
    secs = seconds%3600%60
    return f"{hours:02}:{minutes:02}:{secs:02}"


# In[2]:


make_readable(86399)


# ---

# ## Rot13
# 
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# 
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# 
# Please note that using encode is considered cheating.
# 
# Examples:
# 
# "test" --> "grfg"
# 
# 
# 

# In[39]:


import string
from codecs import encode as _dont_use_this_

def rot13(message):
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out=""
    for char in message:
        if char in abc:
            out+=abc[abc.index(char)+13]
        else:
            out+=char
    return out


# In[40]:


rot13("KUBİLAY")


# In[41]:


rot13("XHOİYNL")


# ---

# ## Not very secure
# 
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
# 
# The string has the following conditions to be alphanumeric:
# 
# - At least one character ("" is not valid)
# - Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# - No whitespaces / underscore
# 
# 
# 

# In[ ]:


def alphanumeric(string):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    for i in string:
        if i not in abc and i.lower() not in abc and i not in num:
            return False
    return True


# In[32]:


alphanumeric("hello world_")


# ---

# In[ ]:




