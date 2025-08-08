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
    # Integer -> Pujan
    sq_size = int(size_input) 

except ValueError as e:
    print(f"An unexpected error occurred: {e}")  # Pujan's error message
    
    try:
        # Alamin's Part: check if float and convert to int
        float_num = float(size_input)
        integer_num = int(round(float_num))
        sq_size = integer_num
        print('its not integer, its a float')
    except ValueError:
        # Check if char/str -> Ashraf
        if size_input == "":
            sq_size = 5  # default value in case user does not provide any value
        else: 
            sq_size = ord(size_input[0])

# ---------------------------------------
# Logical implementation
# Loop -> Imtiaz
for i in range(sq_size):
    if i == 0 or i == sq_size - 1:
        print("* " * sq_size)
    else:
        if sq_size == 1 or sq_size == 2:
            print("* " * sq_size)
        else:
            print("*" + "  " * (sq_size - 2) + " *")
