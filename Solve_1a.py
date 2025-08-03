'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

# triangle

# basic input -> Imtiaz
a_input = input("User input 1: ")
b_input = input("User input 2: ")
c_input = input("User input 3: ")

# input validation

try:
    # Try converting inputs to float
    a = float(a_input)
    b = float(b_input)
    c = float(c_input)

    print(f"Inputs converted to float successfully: {a}, {b}, {c}")

    # After this, pass to next team member for logic (a+b>c etc.)
    
except ValueError:
    # If user entered text or invalid number, this block will run
    print("Error: Please enter valid numbers only for triangle sides.")

    
    # char/str -> al-amin
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input: Side lengths must be positive numbers.")
else:
    # a + b > c -> Ashraf
    cond1 = a + b > c
    # b + c > a -> Pujan
    cond2 = b + c > a
    # c + a > b -> Imtiaz
    cond3 = c + a > b

    # Result display -> Ashraf
    if cond1 and cond2 and cond3:
        print("Yes, these three lengths can form a triangle.")
    else:
        print("NO, these three lengths CANNOT form a triangle.")   

# logical implementation

    # a,b,c>0 -> al-amin
    # a+b>c logic -> ashraf
    # b+c>a logic -> pujan
    # c+a>b logic -> imtiaz

# result -> ashraf
