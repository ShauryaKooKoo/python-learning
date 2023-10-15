print("please select a operation")
print("type add to do addition")
print("type sub to subtract")
print("type div to divide")
print("type mult to multiply")
print("type power to put the power of 2")
operation = input()

    
if operation == "add":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " + str(int(num1) +int(num2)) )

elif operation == "sub":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " + str(int(num1) -int(num2)) )
    
elif operation == "div":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " +str(int(num1) /int(num2)) )
    
elif operation == "mult":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("your answer is " +str(int(num1) *int(num2)))
elif operation == "power":
     num1 = input("enter number:")
     print("your answer is " +str(int(num1) * int(num1)))
else:
    print("try a different command")
    
    
    