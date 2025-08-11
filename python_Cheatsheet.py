'''----------------------------------'''        
        # Python Cheat Sheet
'''----------------------------------'''

1. # Basics :

print("Hai Developer")          # Print the output
x = 11                          # Variable Assignment
print(type(x))                  # Get the type of variable. Ex : <class 'int'>
input("Enter any value : ")     # Take the user input.

# Comment                       # Single Line Comment
''' Multi Line Comment '''      # Multi Line Comment for Documentation Purpose.

#----------------------------------------------------------------------------------------------

2. # Data Types :

my_list = [1,2,3,4]                         # List
my_tuple = (1,2,3,4)                        # Tuple
my_set = {1,2,3,4}                          # Set
my_dict = {"key" : "value"}                 # Dictionary.
print(my_list,my_tuple,my_set,my_dict )

2.1 # Data Structures :

2.1.a # List :

my_list = [1,2,3,4,5]                       # List(Array)      
my_list[0]                                  # Access List Item
my_list[1:4]                                # List Slicing
my_list.append(6)                           # Add Item to List
my_list.remove(3)                           # Remove Item from List.

2.1.b # Dictionary :

my_dict = {"Key1" : "Value1", "Key2" : "Value2"}    # Dictionary (HashMap)
my_dict["Key1"]                                     # Access Dictionary Value
my_dict["key3"] = "Value3"                          # Add Key-Value Pair.

2.1.c # String Manipulation :

full_name = "Python" + " " + "Developer"         # Concatination
len('Python Developer')                          # Find String Length
"Python".upper()                                 # Convert to UpperCase
"Developer".lower()                              # Convert to LowerCase
"python developer".capitalize()                  # Convert each word of first letter to UpperCase.
"Hai Developer..!"[4:14]                         # SubString
"Hai Developer..!".find("Developer")             # Find SubString
"Hai Developer..!".replace("Hai", "Python")      # Replace subString
"Hai Developer..!".split(" ")                    # Split String.

#----------------------------------------------------------------------------------

3. # Conditions :

if x > 5 :                                      # if Condition
    print(" The value is Greater than 5 ")
elif x == 5 :                                   # else if Condition 
    print(" The value is Equals to 5 ")         
else :                                          # else Condition.
    print(" The value is Less than 5 " )

#----------------------------------------------------------------------------------

4. # Loops :

for i in range(10):         # for loop 
    if i == 6 :
        break               # Break Statement

    elif i == 3 :
        continue            # Continue Statement

    print(i, end="\t")

print()

while x >= 1:               # while loop
    x -= 1
    print(x , end="\t")

#----------------------------------------------------------------------------------

5. # Functions : 

def greet(name):                # Defining Function
    return f"Hello, {name}"

greet("BMTechhy")               # Calling Function

def add(a,b):
    return a + b

add = lambda a, b : a + b       # Lambda Function.

#----------------------------------------------------------------------------------

6. # Classes :

class Person:                       # Define Class

    def __init__(self , name):      # Define Constructor
        self.name = name
    
    def greet(self):                # Define Method
        return f"Hai, {self.name}"
    
p = Person("Manoj")                 # Create Object
p.greet()                           # Call Method.

#----------------------------------------------------------------------------------

7. # Error Handling :

try :                                   # try Block
    1/0

except ZeroDivisionError:               # Handle Exception
    print("Can not Divide by Zero.")

finally:                                # Always Execute.
    print("Task is Done...!")

#---------------------------------------------------------------------------------------

8. # File Operation :

with open("Python Libraries.txt", "r") as f :       # Open a file
    content = f.read()                              # Read file Content
    lines = f.readlines()                           # Read Line by Line
    print(lines)

with open("file1.txt", "w") as f1 :                 # Write to a file
    f1.write("Hello , Developer...!")

f1.close()                                          # Close a file.

#-----------------------------------------------------------------------------------------

9. # List Comprehension :

[x**2 for x in range (5)]                           # Basic List Comprehension
[x for x in range(10) if x % 2 == 0]                # List Comprehension with Condition.

#-------------------------------------------------------------------------------------------

10. # Working with Libraries :

import math                                         # Importing a Library
from math import sqrt                               # From math import sqrt
math.sqrt(25)                                       # Using a Library Function
# pip install pandas                                # Install a Library (using pip).

#---------------------------------------------------------------------------------------------

11. # NumPy for Numerical Operation :

import numpy as np                                  # Import Numpy
arr = np.array([1,2,3,4,5])                         # Create Numpy Array
arr.reshape(5, 1)                                   # Array Reshaping
arr + 10, arr * 2                                   # Array Operations
arr[1:4]                                            # Array Slicing
np.mean(arr),np.median(arr),np.std(arr)             # Array Statistics.

#---------------------------------------------------------------------------------------------

12. # Pandas for Data Handling :

import pandas as pd                                  # Import Pandas
pd.DataFrame({"Role" : ["Developer", "Tester"],      # Create DataFrame
              "Skill" : ["Python", "MySQL"], 
              "Age" : [33, 30]
              })

df = pd.read_csv("file.csv")                          # Read Csv File
df.head()                                             # View Data
df.describe()                                         # Basic Satistics
df[df["Age"] > 30]                                    # Filter Data
df.groupby("Age").mean()                              # Group the Data.

#-----------------------------------------------------------------------------------------------

13. # Matplotlib for Plottiing :

import matplotlib.pyplot as plt                       # Import Matplotlib
plt.plot([1,2,3],[4,5,6]);plt.show()                  # Simple Plot
plt.bar([1,2,3],[4,5,6]);plt.show()                   # Bar Plot
plt.hist([1,2,2,3,4,5]);plt.show()                    # Histogram
plt.scatter([1,2,3],[4,5,6]);plt.show()               # Scatter Plot.

#-----------------------------------------------------------------------------------------------

14. # Different Ways To Use F-Strings in Python :

14.1 # Print or store strings with variables and expressions :

num = 5
print("Square of", num, "is", num*num) # Square of 5 is 25

# OR

num = 5
print(f"Square of {num} is {num * num}") # Square of 5 is 25

14.2 # Print Better Floats with F-Strings :

temperature = 3.2000056
print(f"Temperature is {temperature} Celcius") # Temperature is 3.2000056 Celcius
print(f"Temperature is {temperature: .2f} Celcius") # Temperature is  3.20 Celcius
print(f"Temperature is {temperature: .3f} Celcius") # Temperature is  3.200 Celcius

14.3 # Create tables The Better way :

items = ["Samosa","Kachori","Dhokla","Gulab Jamun"]
quantities = [53,35,100,50]

for item, quantity in zip(items, quantities):
    print(f"| {item:15} | {quantity: >10} |") # >10 tells Python to print the strings right justified
'''
Output :
        | Samosa          |         53 |
        | Kachori         |         35 |
        | Dhokla          |        100 |
        | Gulab Jamun     |         50 |
'''
# OR

print(f"| {'Items':15} | {'Quantities':10} |")
print(f"| {'-' * 15} | {'-' * 10} |")
for item, quantity in zip(items, quantities):
    print(f"| {item:15} | {quantity: >10} |")

'''
Output :
        | Items           | Quantities |
        | --------------- | ---------- |
        | Samosa          |         53 |
        | Kachori         |         35 |
        | Dhokla          |        100 |
        | Gulab Jamun     |         50 |
'''
#-----------------------------------------------------------------------------------------------

