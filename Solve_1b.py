'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230

'''
# taking input from user
size_input = input("Enter the size of the square: ")
sq_size = 0
# Input validation. This code is inspired by class lecture
try:
    # Input validation
    # Integer -> Pujan 
    pass

except ValueError:
    # print(f"An unexpected error occurred: {e}")
    
    try:
        # Check if float -> Al-Amin
        pass
        
    except ValueError:
        # print("Invalid input: Please enter a numeric value.")
        # Check if char/str -> Ashraf
        if size_input == "":
            sq_size = 5 # default value in case user does not provide any value
        else: 
            sq_size = ord(size_input[0])
# ---------------------------------------
# Logical implementation
# Loop -> Imtiaz
for i in range(sq_size):
    if i==0 or i==sq_size-1:
        print(i)
    print("*"*sq_size)
else:
    print("*"+" "*(sq_size-2)+"*")
