'''--------------------------------------------'''
#       Code for  PYTHON pattern :
'''--------------------------------------------'''

data = "PYTHON"                 # assign the value
count = 0                       # Initialize the count

for i in data :                 # Performing loop operation 
    count += 1                  # Increment the count
    print (data[0:count])       # Printing the Pattern according to slice 

for i in data :
    count -= 1                  # Decrement the count.
    print(data[0:count])       

# Output :

'''
P
PY
PYT
PYTH
PYTHO
PYTHON
PYTHO
PYTH
PYT
PY
P
'''
#----------------------------------------------------------------