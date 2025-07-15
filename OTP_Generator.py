'''🔐 OTP Generator & User Registration Simulation
This project demonstrates a simple OTP (One-Time Password) generator using Python. It includes a mock user registration function that simulates how OTPs could be generated and delivered for user verification in a real-world system.
📜 Features
- Generates numeric OTPs of customizable length.
- Simulates user registration with OTP generation.
- Handles invalid OTP length with proper error messages.
- Includes test cases for both valid and invalid OTP scenarios.'''

import random
import string

def generate_otp(length=6):
    """ Generates a random numeric OTP of a specified length.
    Args : 
        length (int): The desired length of the OTP. Defaults to 6.
    Return : 
        str: The generated OTP.
    """
    if not isinstance(length,int) or length <= 0:
        raise ValueError("OTP length must be Positive number.")
    digits = string.digits # '0123456789'
    otp = ''.join(random.choices(digits, k=length))
    return otp


# ----- How to use it when someone registers ------

def register_user(username, password):
    
    """
        Simulates user registration and generates an OTP.
        In a real application , you'd save the user to a database
        and then send the otp via SMS or E-Mail.
    """
    print(f"Registering user : {username}")
    # In a real scenario, you'd hash the password before saving.
    # and store user details in a database.

# ------ Generate OTP ------

    otp = generate_otp(6) # You can change the length here
    print (f"OTP generated for {username} : {otp}")

    # ------ Important : In a real application , you would now :------

    # 1. Store the OTP temporarily in your database (associated with the user.)
    # along with its expiry time.

    # 2. Send the OTP to the user's registerd mobile number (via SMS gateway.)
    # or E-Mail address (via email service).

    # 3. Prompt the user to enter the OTP for verification.

    print("Please verify your account using the OTP sent to your registered contact.")
    return otp # Returning OTP for demonstration , don't do this in production.

# ------ Example Usage : -------

if __name__ == "__main__":
    print("--- Simulating User Registartion ---")
    generated_otp_for_user1 = register_user("Manoj", "securepassword456")
    print(f"For Manoj , the OTP was : {generated_otp_for_user1}\n")

    generated_otp_for_user2 = register_user("Bindu", "password123")
    print(f"For Bindu , the OTP was : {generated_otp_for_user2}\n")

    # ------ Example of Generating a 4-digit OTP : ------
    
    print("Generating a 4 digit OTP : ")
    short_otp = generate_otp(4)
    print(f"SHORT OTP : {short_otp}")

    # ------ Example of handling an invalid length ------
    try:
        generate_otp(0)
    except ValueError as e:
        print(f"\nError generating OTP : {e}")
    

# result 1 : 

'''
    --- Simulating User Registartion ---
    Registering user : Manoj
    OTP generated for Manoj : 423526
    Please verify your account using the OTP sent to your registered contact.
    For Manoj , the OTP was : 423526

    Registering user : Bindu
    OTP generated for Bindu : 293022
    Please verify your account using the OTP sent to your registered contact.
    For Bindu , the OTP was : 293022

    Generating a 4 digit OTP : 
    SHORT OTP : 3454

    Error generating OTP : OTP lenggth must be Positive number.

'''

# result 2 : 

'''
    --- Simulating User Registartion ---
    Registering user : Manoj
    OTP generated for Manoj : 600094
    Please verify your account using the OTP sent to your registered contact.
    For Manoj , the OTP was : 600094

    Registering user : Bindu
    OTP generated for Bindu : 983833
    Please verify your account using the OTP sent to your registered contact.
    For Bindu , the OTP was : 983833

    Generating a 4 digit OTP : 
    SHORT OTP : 1937

    Error generating OTP : OTP lenggth must be Positive number.      
'''

