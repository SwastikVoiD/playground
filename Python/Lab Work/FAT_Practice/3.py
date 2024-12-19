import re

def find_numbers_and_positions(input_text):
    # Use regex to find all numbers in the string
    numbers = re.finditer(r'\d+', input_text)
    
    # Iterate through the match objects and print the number and its position
    for match in numbers:
        print(match.group(), match.start(),end=" ")

# Example input string
input_text = "my account number 234567 at Indian bank branch code 111 in Vellore 632001"

# Call the function
find_numbers_and_positions(input_text)
