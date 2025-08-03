'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230

'''
try:
    # Input validation
    # Integer -> Pujan
    size_input = input("Enter the size of the square: ")

    # Check if float -> Al-Amin
    try:
        size_float = float(size_input)
        # Check if char/str -> Ashraf
        if not size_float.is_integer():
            print("Invalid input: Please enter a whole number (integer).")
        else:
            size = int(size_float)

            # ---------------------------------------
            # Logical implementation
            # Loop -> Imtiaz

            if size <= 0:
                print("Invalid input: Size must be a positive integer.")
            else:
                # Result -> Al-Amin
                print("Here is your square:")
                for i in range(size):
                    print("* " * size)

    except ValueError:
        print("Invalid input: Please enter a numeric value.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# End of Part b