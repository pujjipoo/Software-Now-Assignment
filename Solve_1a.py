'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

# This function validate input received form user. Also this code is inspired from class lecture.
def input_validation(x):
    try:
        # integer -> Ashraf
        # Trying to convert string input from user into a Interger number
        temp_x = int(x)
        x = temp_x
    except ValueError:
        try:
            # float -> Pujan
            # Trying to convert string input from user into a Floating point number
            temp_x = float(x)
            x = temp_x
        except ValueError:
            # char/str -> al-amin
            # In case of character input below code will convert it to integer based on Ascii value
            # Below code only take 1st char of a string to convert into integer
            if x == "":
                x = 7 # placing a default value 7
                print("user did not provide any value. Default value 7")
            else:
                temp_x = ord(x[0])
                x = temp_x
                print(f"user provided a char or string. Converting first char into Ascii equivalent: {x}")
    return x
            

# code for inputing three numbers, and check if these three numbers can form a triangle.
# This code can run repeatedly. 
restart = True
while restart:
    # basic input -> Imtiaz
    # Taking 3 side input from user
    a_input = input("User input 1: ")
    b_input = input("User input 2: ")
    c_input = input("User input 3: ")

    # input validation
    a = input_validation(a_input)
    b = input_validation(b_input)
    c = input_validation(c_input)

    # manual debuging
    # print(f"a: {a}\nb: {b}\nc: {c}")
    
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

    # asking user if they want to restart the program again.
    # Al-amin
    choice = input("Press n/no to exit or Press any other button to restart: ")
    if choice == "n" or choice == "no":
        restart = False
    
        

