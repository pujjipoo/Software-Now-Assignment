""""""

int_n, float_n, list_n, printN = input(), 0, [4]*2, 6
print("printing integer that is named int_n: ", int_n, "its type is ", type(int_n))
try:
    print("in try") 
    int_n=int(int_n)
except ValueError:
    print("in except1")
    #try: 
    float_num=float(int_n)
    integer_num=int(round(float_num))
    int_n=integer_num
    print('its not integer, its a float')
except:
    #take input ointo list and convert each in list to ascii value
    ascii_values=[ord(char) for char in int_n]
    print("ascii_values ", ascii_values)
    rounded_input=int(sum(ascii_values))
    int_n=rounded_input
    if type(rounded_input)!=int:
        int_n=5
        print("default input used = 5")
    if rounded_input>100:
        int_n=rounded_input/10
#printing *
for i in range(int_n):
    if i==0 or i==int_n-1:
        print(i)
    print("*"*int_n)
else:
    print("*"+" "*(int_n-2)+"*")
   
print("type of int_n", type(int_n))   
result_add=int_n + float_n
print("I am adding integer {} to float {} to lead to the result {}".format(int_n,float_n,result_add))
result_div=0
if float_n!=0:
    result_div=int_n/float_n
else:
    result_div=0
print("I am diving integer {} by float {} to lead to the result {}".format(int_n,float_n,result_div))  
