#!/usr/bin/env python
# coding: utf-8

#  # <center>Midterm Exam &ndash; DATA 3401 (Spring 2023)</center>
# 
# ## Start Date: 3/27
# ## Due Date for Exercises 1 and 2:    3/27 (at 2:15pm))
# ## Due Date: for Exercises 3, 4 and 5:     23/29 (at 12:59pm))
# 
# ## Midterm Rules
# 
# This midterm exam is essentially like a short-term lab. Please work the exercises below **on your own**.   
# 
# **You should push your answer for Exercises 1 and 2 by the end of Monday's class, 3/27, at 2:15 pm in your GitHub repo for this class as **Midterm-part1** in the **Exam** folder. The rest of the exam is a take-home exam, and you have time up to Wednesday, 3/29, at 12:59. When you have completed the take-home exam, you should again push your completed jupyter notebook to your GitHub repo for this class as **Midterm-part2** in the **Exam** folder.
# 
# 
# You may not discuss the problems with **anyone else**, including persons on an online internet forum. Consulting an outside source like this will be considered an academic integrity violation.
# 
# You may use all class resources including previous labs and lectures, and anything posted on the course webpage.
# 
# You may not use any function that trivializes a problem. For example, if I ask you to write a `max` function that computes the maximum entry in a list, you are not allowed to use the pre-defined Python function `max`; you must write your own.

# ## Exercise 1
# 1. Write a script or function that asks the user to input 3 numbers (floats or ints), and output the product of the 3 numbers.
#     1. You may use the `input()` function to take user input, or you may write a function with 3 input arguments without using `input()`
# 1. Your code should display an error message if one of the inputs is not a number.
# 1. Test your code on the following inputs:  
#     1. (5, -10, 20.0)
#     1. (1, "blah", 5)

# In[17]:


num1 = 5
num2 = -10
num3 = 20.0
product = num1 * num2 * num3
print(f"The product of {num1}, {num2}, and {num3} is: {product}")
except ValueError as e:
    print ("Error:",e)


# In[42]:


try: 
    num1 = float (1)
    num2 = float ("blah")
    num3 = 5
    product = num1 * num2 * num3 
    print(f"The product of {num1}, {num2}, and {num3} is: {product}")

except ValueError as e:
    print ("Error:",e)


# ## Exercise 2
# 1. Write a function which takes a list as input and outputs the largest **integer** entry. If there is none, return `None`.
# 1. Test your function on the following lists
#     1. \[ 1, 9, 10.2, 6, -2\]
#     1. \[1.2, 3/4, "Hello World"\]

# In[35]:


def find_largest_number(numbers):
    largest_number = None
    for num in numbers:
        if isinstance(num, (int, float)) and (largest_number is None or num > largest_number):
            largest_number = num
    return largest_number

numbers = [ 1, 9, 10.2, 6, -2]
largest_number = find_largest_number(numbers)

if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty or contains no valid numbers.")


# In[40]:


def find_largest_integer(lst):
    largest_integer = None
    for item in lst:
        if isinstance(item, int) and (largest_integer is None or item > largest_integer):
            largest_integer = item
    return largest_integer


# In[41]:


lst2 = [1.2, 3/4, "Hello World"]
print(find_largest_integer(lst2))


# ## Exercise 3
# Suppose the first element of a sequence is $a_0 = 1$, the second element is $a_1 = 3$, and for every $i>1$, the $i$--th element of the sequence is defined by the recursive relation $a_i = \frac{(a_{i-1}-a_{i-2})^2}{3}$. (So $a_2 = 4/3$)
# 1. Write a function which outputs the $n$--th element of this sequence for a given positive integer $n$
# 2. Test your function for $n = 1, 5, 10, 15,$ and $20$

# In[53]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(2))


# In[54]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(1))


# In[55]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(5))


# In[56]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(10))


# In[57]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(15))


# In[58]:


def sequence_element(i):
    if i == 0:
        return 1
    elif i ==1:
        return 3
    else:
        return ((sequence_element(i-1)**2-sequence_element(i-2)**2) /3)
print (sequence_element(20))


# ## Exercise 4
# 1. Write a function that takes in a list of tuples, each of which contains three parts: `name, month, day` corresponding to a person's birthday, for example `('Tony Stark', 'March', 14)`. Your function should output `True` if any two people have the same birthday, and `False` if no two people have the same birthday.
# 1. Test your function on the set of people `[('Thor', 'August',10), ('Phil Coulson','July',8),('T\'Challa','November',29),('Peter Parker','August',10), ('Tony Stark', 'March', 14)]`
# 1. Create your own list of people with all distinct birthdays and test your function on your list.

# In[67]:


def same_birthday(birthdays):
    dates = set()
    for bday in birthdays:
        date = bday[1] + ' ' + str(bday[2])
        if date in dates:
            return True
        else:
            dates.add(date)
    return False


# In[68]:


birthdays= [('Thor', 'August',10), ('Phil Coulson','July',8), ('T\'Challa','November',29), ('Peter Parker','August',10), ('Tony Stark', 'March', 14)]
result = same_birthday(birthdays)
print (result)


# In[69]:


birthdays = [('Insh', 'December', 25), ('Beza', 'December',26), ('Emnet', 'November', 28), ('Efrata', 'August', '15'), ('Beza', 'August', '11'), ('Yemi', 'March', '24')]
result = same_birthday(birthdays)
print (result)


# ## Exercise 5
# For this exercise, you are *not* allowed to use the `.replace()` function or a similar single string command to complete the exercise. For example, you could make a list of the input string and then use list manipulations to complete the task.
# 
# 1. Write a function or script that takes in two strings, and returns the first string minus all instances of the second string. You may assume the second string is a single character.  For example, an input of "Hello World" where "l" is removed should result in "Heo Word".
# 1. Test your function by specifying "i" to be removed from "Supercalifragilisticexpialidocious"
# 
# Bonus: Modify your function to allow the second string to be more than one characer. Test your new function by specifying "data" to be removed from "data 3401 introduction to python for data science". (This should result in ' 3401 introduction to python for  science'
# 
# **Example:** if your function is called `replace_string(str1,str2)`, then for part 2 you should print `replace_string('Supercalifragilisticexpialidocious','i')` and for the bonus you should print `replace_string('data 3401 introduction to python for data science','data')`

# In[70]:


def remove_char(input_str, char):
    output_str = ''
    for i in input_str:
        if i !=char:
            output_str += i
    return output_str


# In[71]:


input_str = 'Supercalifragilisticexpialidocious'
char_to_remove = 'i'
output_str = remove_char(input_str, char_to_remove)
print(output_str)


# In[ ]:




