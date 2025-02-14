def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "cannot divided by zero"
    return a/b
while True:
    print("Options:")
    print("Enter 'add' for additon")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to stop the program")
    user_input=input("Enter your choice: ")
    if user_input=="exit":
        break
    if user_input in ("add","subtract","multiply","divide"):
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        if user_input=="add":
            print("result: ",add(num1, num2))
        elif user_input=="subtract":
            print("result: ",subtract(num1, num2))
        elif user_input=="multiply":
            print("result: ",multiply(num1, num2))
        elif user_input=="divide":
            print("result: ",divide(num1, num2))
    else:
        print("Invalid input")

    


