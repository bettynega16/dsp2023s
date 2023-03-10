#!/usr/bin/env python
# coding: utf-8
Branches 
1. single-line python input and string manipulation (only part B)
# In[6]:


def dummy(i):
    j = 0 if i == 0 else 1 if i == 1 else 2 if i == 2 else 'j is not in [0,1,2]'
    return j


# Looping

# In[11]:


#1
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Fdegrees = [-20, -15, -5, 0, 10, 15, 30, 35, 40]

for i in range(len(Cdegrees)):
    F = (9/5) * Cdegrees[i] + 32
    print("{:.2f} degrees Celsius = {:.2f} degrees Fahrenheit".format(Cdegrees[i], F))


# In[13]:


#A
def convert_temp(temps, direction):
    """
    Converts the input temperature vector from Fahrenheit to Celsius if the
    input string is 'F2C', otherwise converts the input temperature vector from
    Celsius to Fahrenheit if the input string is 'C2F', otherwise outputs an
    error message and aborts the program.
    
    Args:
        temps (list): Input temperature vector
        direction (str): Conversion direction ('F2C' or 'C2F')
    
    Returns:
        list: Converted temperature vector
    """
    if direction == 'F2C':
        converted_temps = [(t - 32) * 5/9 for t in temps]
        return converted_temps
    elif direction == 'C2F':
        converted_temps = [(t * 9/5) + 32 for t in temps]
        return converted_temps
    else:
        print("Invalid direction. Please specify either 'F2C' or 'C2F'.")
        return 


# In[14]:


print("Invalid direction. Please specify either 'F2C' or 'C2F'.")


# In[15]:


#Anumber2
def convertTempWhile(temps, direction):
    # Initialize converted_temps list to store the converted temperatures
    converted_temps = []

    # Loop over each temperature in the input vector using a while loop
    i = 0
    while i < len(temps):
        # Convert the temperature based on the input direction
        if direction == 'C2F':
            converted_temp = (temps[i] * 9/5) + 32
        elif direction == 'F2C':
            converted_temp = (temps[i] - 32) * 5/9
        else:
            # If the direction is not valid, print an error message and return None
            print("Error: Invalid direction specified")
            return None
        
        # Add the converted temperature to the list
        converted_temps.append(converted_temp)
        
        # Increment the loop counter
        i += 1

    # Return the list of converted temperatures
    return converted_temps


# In[16]:


temps = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
direction = 'C2F'
converted_temps = convertTempWhile(temps, direction)
if converted_temps is not None:
    for i in range(len(temps)):
        print("{:.2f} degrees {} = {:.2f} degrees {}".format(
            temps[i],
            'Celsius' if direction == 'C2F' else 'Fahrenheit',
            converted_temps[i],
            'Fahrenheit' if direction == 'C2F' else 'Celsius'))


# In[19]:


#B
def convertTempFor(temps, direction):
    # Initialize converted_temps list to store the converted temperatures
    converted_temps = []
    
    # Loop over each temperature in the input vector using a for loop
    for temp in temps:
        # Convert the temperature based on the input direction
        if direction == 'C2F':
            converted_temp = (temp * 9/5) + 32
        elif direction == 'F2C':
            converted_temp = (temp - 32) * 5/9
        else:
            # If the direction is not valid, print an error message and return None
            print("Error: Invalid direction specified")
            return None
        
        # Add the converted temperature to the list
        converted_temps.append(converted_temp)

    # Return the list of converted temperatures
    return converted_temps


# In[20]:


temps = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
direction = 'C2F'
converted_temps = convertTempFor(temps, direction)
if converted_temps is not None:
    for i in range(len(temps)):
        print("{:.2f} degrees {} = {:.2f} degrees {}".format(
            temps[i],
            'Celsius' if direction == 'C2F' else 'Fahrenheit',
            converted_temps[i],
            'Fahrenheit' if direction == 'C2F' else 'Celsius'))


# In[21]:


#C
import numpy as np

def convertTempVec(temps, direction):
    # Convert the input list to a NumPy array
    temps = np.array(temps)
    
    # Convert the temperatures based on the input direction using vectorized operations
    if direction == 'C2F':
        converted_temps = (temps * 9/5) + 32
    elif direction == 'F2C':
        converted_temps = (temps - 32) * 5/9
    else:
        # If the direction is not valid, print an error message and return None
        print("Error: Invalid direction specified")
        return None
        
    # Return the list of converted temperatures as a NumPy array
    return converted_temps


# In[22]:


temps = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
direction = 'C2F'
converted_temps = convertTempVec(temps, direction)
if converted_temps is not None:
    for i in range(len(temps)):
        print("{:.2f} degrees {} = {:.2f} degrees {}".format(
            temps[i],
            'Celsius' if direction == 'C2F' else 'Fahrenheit',
            converted_temps[i],
            'Fahrenheit' if direction == 'C2F' else 'Celsius'))


# 2. Modifiying the index pf a for-loop

# In[23]:


numbers= list(range(10))
print(numbers)


# In[24]:


for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del{}'.format(n,i),numbers)


# In[ ]:


#it pust del has 5,4,3 and removes them from the list.


# 3. Impact of machine precision on numerical computation 

# In[26]:


eps = 1.0
while 1.0 != 1.0 + eps:
    print ('...............', eps)
    eps /= 2.0
print ('final eps:', eps)


# In[ ]:


#find the smallest value of eps that can be added to 1.0 such that the result is different from 1.0. It starts with eps set to 1.0 and divides it by 2 in each iteration of the while loop until 1.0 + eps is not equal to 1.0 anymore.

#The reason why 1.0 != 1.0 + eps can be False is also due to the way floating-point numbers are represented in a computer. 


# 4.  Impact of round-off errors on numerical computations 

# In[27]:


from math import sqrt
for n in range(1, 60):
    r_org = 2.0
    r = r_org
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print ('With {} times sqrt and then {} times **2, the number {} becomes: {:.16f}'.format(n,n,r_org,r))


# In[ ]:


#for each value of n between 1 and 59, the program calculates the result of repeatedly taking the square root of an initial value (r_org = 2.0) n times, followed by repeatedly squaring the resulting value n times. The program then prints out the original value of r_org and the final result.


# 6. String concatenation using for-loop (only python section)

# In[28]:


q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
letters = ""

for sublist in q:
    for letter in sublist:
        letters += letter

print(letters)


# In[ ]:




