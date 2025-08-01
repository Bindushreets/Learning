# Python Projects with partial() :

''' 
    Partial functions 'lock in' some arguments,
        so don't repeat yourself every time.
        It's like creating a custom version of a function with minimal effort.
'''
# Advantages of Partial Functions : 

'''
1. Reusability :
        With partial(), I can reuse existing functions but 'lock in' some of the arguments,
            creating specialized versions.
            No need to retype code or redefine functions every time — 
                just call the partial function with the remaining parameters.

2. Code Simplification :
        How many times have you had to pass the same arguments around?
            partial() eliminates that.
            We can fix certain values in one place, which makes future calls simpler and cleaner.

3. Readability :
        By locking in arguments, the function calls become more readable.
            It's immediately clear what the function does and which arguments are "preset" — 
                reducing the cognitive load for anyone reading the code.

4. Customization :
        It's incredibly easy to customize a general-purpose function.
            I just set the fixed arguments once and get a tailored version of that function.
                It's like building a custom tool for your project with minimal effort.

5. Modularity :
    partial() helps break down complex functions into smaller, reusable components.
        Instead of repeating logic, I can focus on specific tasks,
            creating modular chunks of code that are easy to maintain.
'''
#------------------------------------------------------------------------------------------------------

''' Syntax :

from functools import partial

# Define a regular function
def func(arg1, arg2, arg3):
    # Do something
    pass

# Create a partial function by fixing some arguments
partial_func = partial(func, fixed_arg1, fixed_arg2)

# Now call it with the remaining arguments
result = partial_func(arg3) '''

#-----------------------------------------------------------------------------------------------

1. #    My BMI Calculator :

'''
    I was tracking my weight over time and 
        retyping my height every time I calculated my BMI.
        
    So I used 'functools.partial' to 'lock in' my height once,
        and just pass in the changing weight : 
'''
from functools import partial

def calculate_bmi(height: float, weight: float) -> str:
    bmi = weight / (height ** 2)
    return f"Body Mass Index BMI = {bmi:.2f}"

# Set my height once and reuse the function
bmi_for_my_height = partial(calculate_bmi, height=5.7)

# Track weight changes over time
print(bmi_for_my_height(weight=75))  
print(bmi_for_my_height(weight=73))  

'''
    Output :
            Body Mass Index BMI = 2.31
            Body Mass Index BMI = 2.25
'''
#------------------------------------------------------------------------------------------------

2. # Weather Report with City Locked In :

from functools import partial

def weather_report(city: str, temp: int, rain: bool) -> str:
    return f"""Temperature in {city} is {temp}ºC.
It is {'raining' if rain else 'not raining'}."""

# Regular usage
print(weather_report('Bengaluru', 17, True))

# Lock in the city as 'Mysore'
madrid_weather_report = partial(weather_report, city="Mysore")

# Now just update the weather
print(madrid_weather_report(temp=24, rain=False))

'''
    Output :
            Temperature in Bengaluru is 17ºC.
            It is raining.
            Temperature in Mysore is 24ºC.
            It is not raining.
'''
#-----------------------------------------------------------------------------------------------

# Partial Functions vs. Lambda :
'''
    Both allow us to create smaller, more specialized functions,
        but they each have their strengths.
    
    1.  Partial Functions :
            What it does : Pre-fills arguments for an existing function.
            Syntax : partial(existing_func, fixed_args)
                -> Pros :
                    1.  Tied to an existing function — keeping code structured and readable.
                    2.  Great for reusing and simplifying existing functions.
                    3.  More explicit and easier to read, especially in larger projects.
                -> Cons :
                    Slight overhead due to function wrapping.
    
    2.  Lambda Functions:
            What it does : Creates anonymous, inline functions.
            Syntax : lambda args : expression
                -> Pros :
                    1.  Super lightweight and flexible for quick, one-off functions.
                    2.  Excellent for short-term, ad-hoc operations.
                -> Cons :
                    Can get messy and hard to read when functions grow in complexity.
    So, which to use?
        partial() : We canuse it when we want to reuse existing functions with certain arguments fixed,
            especially when readability and structure matter.
        lambda : We can turn to lambdas for quick, inline tasks
            when we don't need a full function definition.
'''

# Ex: using partial()

from functools import partial

def power(base, exponent):
    return base ** exponent

# Regular function call for squaring
print(power(2, 2))

# Using partial to create a new function for squaring
square = partial(power, exponent=2)
print(square(2))
print(square(5))

'''
    Output : 
            4
            4
            25
'''

# Ex: using Lambda () :

# Using a lambda function to square a number
square = lambda base: base ** 2
print(square(2))

'''
    Output :
            4
'''
#--------------------------------------------------------------------------------------------------------