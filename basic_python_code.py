# 10 Python Programs for Beginners

1.  # Odd or Even Checker : 

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# Sample Output :
'''     1. Enter a number: 5
           5 is Odd 
        2. Enter a number: 10
            10 is Even '''
#-----------------------------------------------------

2. # Simple Calculator : 

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid operator")

# Sample Output :
'''     1.  Enter first number: 1
            Enter operator (+, -, *, /): +
            Enter second number: 2
            3.0
        2.  Enter first number: 20
            Enter operator (+, -, *, /): -
            Enter second number: 5
            15.0
        3.  Enter first number: 356
            Enter operator (+, -, *, /): *
            Enter second number: 758
            269848.0
        4.  Enter first number: 70
            Enter operator (+, -, *, /): /
            Enter second number: 5
            14.0 
        5.  Enter first number: 5
            Enter operator (+, -, *, /): &
            Enter second number: 4
            Invalid operator '''
#-----------------------------------------------------

3. # Swap Two Variables

n1 = int(input("Enter 1st Number : " ))
n2 = int(input("Enter 2nd Number : " ))

print(f"Before swap: n1 = {n1}, n2 = {n2}")
n1 , n2 = n2, n1
print(f"After swap: n2 = {n1}, n2 = {n2}")

# Sample Output :
''' Enter 1st Number : 10
    Enter 2nd Number : 5
    Before swap: n1 = 10, n2 = 5
    After swap: n2 = 5, n2 = 10 '''
#-----------------------------------------------------

4. # Find the Largest and Smallest Number : 

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

largest = max(n1, n2, n3)
print(f"\nThe largest number is {largest}\n")

smallest = min(n1, n2, n3)
print(f"The smallest number is {smallest}")

# Sample output : 
''' Enter first number: 10
    Enter second number: 50
    Enter third number: 30

    The largest number is 50

    The smallest number is 10 '''
#-----------------------------------------------------

5. # Fibonacci Sequence (Without Recursion) : 

n = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

while count < n:
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2
    count += 1

# Sample output : 
''' How many terms? 5
    0 1 1 2 3 '''
#-----------------------------------------------------

6.  # Prime Number Checker :

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            print(f"{num} is not a Prime Number")
            break
    else:
        print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")

# Sample output : 
''' 1.  Enter a number: 5
        5 is a Prime Number
    2.  Enter a number: 30
        30 is not a Prime Number '''
#-----------------------------------------------------

7.  # Palindrome Checker :

text = input("Enter a string: ")

if text == text[::-1]:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is not a Palindrome")

# Sample output :
''' 1.  Enter a string: Bindu
        'Bindu' is not a Palindrome
    2.  Enter a string: MADAM
        'MADAM' is a Palindrome '''
#-----------------------------------------------------

8.  #   Guess the Number :

import random

number_to_guess = random.randint(20, 50)
guess = int(input("Guess a number between 20 and 50: "))

if guess == number_to_guess:
    print("Congratulations! You guessed right!")
else:
    print(f"Sorry, the number was {number_to_guess}.")

# Sample output :
''' Guess a number between 20 and 50: 35
    Sorry, the number was 46. '''
#-----------------------------------------------------

9.  #  Word Counter :

sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"Number of words: {len(words)}")

# sample output : 
''' Enter a sentence: Who are you ?
    Number of words: 4 '''
#-----------------------------------------------------

10. # Password Strength Checker :

password = input("Enter your password: ")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong password")

else:
    print("Weak password, try again.")

# Sample output :
''' 1.  Enter your password: BinduManoj1131
        Strong password
    2.  Enter your password: BinduManoj
        Weak password, try again. '''

#-----------------------------------------------------

