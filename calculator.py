print("please select a operation")
print("press 1 to add")
print("press 2 to subtract")
print("press 3 to divide")
print("press 4 to multiply")
print("press 5 to the power of 2")
operation = input()

    
if int(operation) == 1:
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " + str(int(num1) +int(num2)) )

elif int(operation) == 2:
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " + str(int(num1) -int(num2)) )
    
elif int(operation) == 3:
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " +str(int(num1) /int(num2)) )
    
elif int(operation) == 4:
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " +str(int(num1) *int(num2)))
elif int(operation) == 5:
     num1 = input("enter number:")
     print("your answer is " +str(int(num1) * int(num1)))
else:
    print("please try a different command")
    
    
    