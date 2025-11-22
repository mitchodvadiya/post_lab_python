import re

# Function to validate PAN card number
def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern, pan):
        return True
    return False

# Function to validate Email ID
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

#  Combined Program 
print("=== PAN & Email Validation Program ===")

# PAN Validation
pan_number = input("Enter PAN card number: ")
if validate_pan(pan_number):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")

# Email Validation
email_id = input("Enter Email ID: ")
if validate_email(email_id):
    print("Valid Email ID.")
else:
    print("Invalid Email ID.")
