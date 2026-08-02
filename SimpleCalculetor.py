print("Simple Calculetor")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator = input("what to do you want to do(+,-,*,/):") 

if operator=="+":
    result = num1 + num2
elif operator=="-":
    result = num1 - num2
elif operator=="*":
    result = num1 * num2
elif operator=="/":
    if num2 != 0:
        result=num1/num2
        
    else:
         result= "error:division by Zero is not allowed"
else:
    result="Invalid operator. Please use +, -, *, or /."


print("Result:", result)
