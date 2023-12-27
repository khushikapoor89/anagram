#!/usr/bin/env python
# coding: utf-8

# In[1]:


x="boat"
y=list(x)
print(y)


# In[2]:


def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(y,0,2)


# In[3]:


str=" "
d=str.join(y)
print(d)


# In[4]:


X=input("enter a word=")
Y=list(X)
print(Y)
def swap(list,pos1,pos4):
    list[pos1],list[pos4]=list[pos4],list[pos1]
    return list
swap(Y,1,4)
str=" "
d=str.join(Y)
print(d)


# In[9]:


X=input("enter a word=")
Y=list(X)
print(Y)
def swap(list,pos1,pos2,pos3):
    list[pos1],list[pos2],list[pos3]=list[pos3],list[pos1],list[pos2]
    return list
swap(Y,1,3,5)
str=" "
d=str.join(Y)
print(d)


# In[39]:


#write a program to check whether the two given words are anagram or not .ensure that the words are prompt.
X=input("first word name=")
Y=input("second word name=")
a=X.lower()
b=Y.lower()
if sorted(a)==sorted(b):
    print("X and Y are anagrams.")
else:
    print(" X and Y are not anagrams.")


# In[7]:


#write a program to remove any duplicate elements in a array
import array
from array import*
arr1=array('i',[1,2,3,2,4])
final_array=[]
for x in arr1:
    if x not in final_array:
        final_array.append(x)
print(arr1)
print("after removing duplicate number=",final_array)


# In[12]:


def find_alphabet(word, char):
    if char in word:
        print("The character ",char," is present in the word.")
    else:
        print("The character" ,char, "is not present in the word.")
word = input("Enter a word: ")
alphabet_to_find = input("Enter a character to find: ")
find_alphabet(word, alphabet_to_find)


# In[ ]:




