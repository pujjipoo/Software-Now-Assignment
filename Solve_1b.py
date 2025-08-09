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

# Input validation. This code is inspired by class lecture
try:
    # Input validation
    # Integer -> Pujan 
    sq_size = int(size_input)
    print("\nUser provided an integer number.")
except ValueError:   
    try:
        # Check if float -> Al-Amin
        sq_size = int(round(float(size_input)))
        print("\nUser provided a float value.\nConverting it to integer.\n")
    except ValueError:
        # print("Invalid input: Please enter a numeric value.")
        # Check if char/str -> Ashraf
        if size_input == "":
            sq_size = 5 # default value in case user does not provide any value
            print("\nuser did not provide any value.\nDefault value Assigned.\n")
        else: 
            sq_size = ord(size_input[0])
            print(f"\nuser provided a character or string.\nConverting only first character into Ascii equivalent number.\n")
# ---------------------------------------
# Logical implementation
# Loop -> Imtiaz
print(f"printing the square below (size {sq_size}): \n")
for i in range(sq_size):
    if i == 0 or i == sq_size - 1:
        print("* " * sq_size)
    else:
        print("*" + "  " * (sq_size - 2) + " *")
