
def addition(num1, num2):
    return int(num1) +int(num2)

def subtraction(num1, num2):
    return int(num1) -int(num2)

def multiplication(num1, num2):
    return int(num1) *int(num2)

def division(num1, num2):
    return int(num1) /int(num2)

def exponent(num1):
    return int(num1) *int(num1)

if __name__ == "__main__":
    print("please select a operation")
    print("type add to do addition")
    print("type sub to do subtraction")
    print("type mult to do multiplication")
    print("type div to do division")
    print("type expo to do exponents")
    operation = input("Enter your choice: ")
    
    if operation == "add":
        num1= int(input("Enter your first number: "))
        num2= int(input("Enter your second number: "))
    
        print( num1," + " , num2, " = ", addition(num1, num2))
    

    
    if operation == "sub":
        num1= int(input("Enter your first number: "))
        num2= int(input("Enter your second number: "))
    
        print( num1," - " , num2, " = ", subtraction(num1, num2))
        
        
    if operation == "mult":
        num1= int(input("Enter your first number: "))
        num2= int(input("Enter your second number: "))
    
        print( num1," * " , num2, " = ", multiplication(num1, num2))
        
        
    if operation == "div":
         num1= int(input("Enter your first number: "))
         num2= int(input("Enter your second number: "))
     
         print( num1," / " , num2, " = ", division(num1, num2))
         
         
    if operation == "expo":
         num1= int(input("Enter your number: "))
     
         print( num1," to the power of 2 " " = ", exponent(num1))