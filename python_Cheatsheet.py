'''----------------------------------'''        
        # Python Cheat Sheet
'''----------------------------------'''

1. # Basics :

print("Hai Developer")          # Print the output
x = 11                          # Variable Assignment
print(type(x))                  # Get the type of variable. Ex : <class 'int'>
input("Enter any value : ")     # Take the user input.

#----------------------------------------------------------------------------------

2. # Data Types :

my_list = [1,2,3,4]              # List
my_tuple = (1,2,3,4)             # Tuple
my_set = {1,2,3,4}               # Set
my_dict = {"key" : "value"}      # Dictionary.
print(my_list,my_tuple,my_set,my_dict )

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
    print(i, end="\t")

print()

while x >= 1:               # while loop
    x -= 1
    print(x , end="\t")

#----------------------------------------------------------------------------------

5. # Functions : 

def greet(name):                # Defining Function
    return f"Hello, {name}"

greet("BMTechhy")               # Calling Function.

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

#----------------------------------------------------------------------------------

8. # File Operation :

with open("Python Libraries.txt", "r") as f :       # Open a file
    content = f.read()                  # Read file Content
    print(content)

with open("file1.txt", "w") as f :       # Write to a file.
    f.write("Hello , Developer...!")                    
#----------------------------------------------------------------------------------