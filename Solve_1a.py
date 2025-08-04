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
    # integer -> Ashraf
    try:
        # Trying to convert string input from user into a Interger number
        temp_x = int(x)
        x = temp_x
    except ValueError:
        try:
            # float -> Pujan
            pass
        except ValueError:
            # char/str -> al-amin
            pass
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
        # al-amin will implement his code here
        pass # remove this al-amin
       
    else: 
        print("NO, these three lengths CANNOT form a triangle.")

    # asking user if they want to restart the program again.
    # Al-amin
    choice = input("Press n/no to exit or Press any other button to restart: ")
    if choice == "n" or choice == "no":
        restart = False
    
        
        
