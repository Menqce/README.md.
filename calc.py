
operator = input("enter an operator (+ - * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a 2nd number: "))

if operator== "+":
    result = num1 + num2
    print(round(result, 1))
elif operator == "-":
    result = num1 - num2
    print(round(result, 1))
elif operator == "*":
    result = num1 * num2
    print(round(result, 1))
elif operator == "/":
    result = num1 / num2
    print(round(result, 1))
else:
    print(f"(operator) is not a valid operator")
