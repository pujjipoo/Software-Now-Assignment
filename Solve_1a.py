'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

# code for taking input of three side of a triangle, and check if these three sides length can form a triangle.
# -------------------------------------------------------------------------------------------------------------

# This function validate input received form user. Also this code is inspired from class lecture.

def input_validation(x, side_num):
    try:
        # integer -> Ashraf
        # Trying to convert string input from user into a Interger number
        temp_x = int(x)
        x = temp_x
        print(f"\nSide: {side_num}")
        print("User provided an integer number.")
    except ValueError:
        try:
            # float -> Pujan
            float_x = float(x)
            round_x = round(float_x)
            x = int(round_x)
            print(f"\nSide: {side_num}")
            print(f"User provided a float value for the side {side_num}.\nConverting it to integer.\n")
        except ValueError:
            # char/str -> al-amin
            # In case of character input below code will convert it to integer based on Ascii value
            # Below code only take 1st char of a string to convert into integer
            if x == "":
                x = 7 # placing a default value 7
                print(f"\nSide: {side_num}")
                print(f"user did not provide any value for side {side_num}.\nDefault value Assigned.\n")
            else:
                temp_x = ord(x[0])
                x = temp_x
                print(f"\nSide: {side_num}")
                print(f"user provided a character or string for side {side_num}.\nConverting only first character into Ascii equivalent number.\n")
    return x
            


# This code can run repeatedly, until user says "n" or "no" (lower case) when program will ask for another try.
restart = True
while restart:
    # basic input -> Imtiaz
    # Taking 3 sides length from user
    a_input = input("Length of side 1: ")
    b_input = input("Length of side 2: ")
    c_input = input("Length of side 3: ")

    # input validation
    # Here a,b,c are the three sides of a triangle
    a = input_validation(a_input,1)
    b = input_validation(b_input,2)
    c = input_validation(c_input,3)

    # manual debuging
    # print(f"a: {a}\nb: {b}\nc: {c}")
    
    print(f"\nFinal lengths:\nLength of side 1: {a}\nLength of side 2: {b}\nLength of side 3: {c}\n")
    
    print("Final Outcome: ")
    # checking condition for side length,if any one of them is zero or not
    if a <= 0 or b <= 0 or c <= 0:
        print("NO, these three lengths CANNOT form a triangle.")
    # a + b > c -> condition cheking if a + b greater than c (Ashraf)
    elif a + b > c :
        # b + c > a -> (Imtiaz) condition cheking if b + c greater than a
        if b + c > a:
            # c + a > b -> (Alamin) condition cheking if c + a greater than b
            if c + a > b:
                print("YES, these three lengths CAN form a triangle.")
            else:
                print("NO, these three lengths CANNOT form a triangle.")
        else:
            print("NO, these three lengths CANNOT form a triangle.")
    else:
        print("NO, these three lengths CANNOT form a triangle.")

    # asking user if they want to restart the program again. --> (Al-Amin)
    choice = input("\nPress n/no to exit or Press any other button to restart: ")
    if choice == "n" or choice == "no":
        restart = False
        
# End of code
        

