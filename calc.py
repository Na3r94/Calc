import math

op = input()

if op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "factorial":
    a = float(input())

else:
    a = float(input())
    b = float(input())

if op == "+":
    result = a + b

elif op == "-":
    result = a - b

elif op == "*":
    result = a * b

elif op == "/":
    if b == 0:
        result = "Cannot divide by zero!"
    else:
        result = a / b

elif op == "**":
    result = a ** b

elif op == "sqrt":
    if a < 0:
        result = "Number Shoud be 0 or higher"
    else:
        result = math.sqrt(a)

elif op == "sin":
    result = math.sin(a * math.pi / 180)

elif op == "cos":
    result = math.cos(a * math.pi / 180)

elif op == "tan":
    result = math.tan(a * math.pi / 180)

elif op == "cot":
    result = math.cot(a * math.pi / 180)

elif op == "factorial":
    if a >= 0:
        result = math.factorial(a)
    else:
        result = "Number Shoud be 0 or higher"

else:
    result = ("Operation not fonud")


print(result)