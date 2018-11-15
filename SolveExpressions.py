import LunarArithmetic as lunar

while True:
    expression = input("Input expression:")
    if expression.find("+") == -1 and expression.find("*") == -1:
        "Invalid expression."
        continue
    operatorPos = expression.find("+") if expression.find("+") > -1 else expression.find("*")
    a = int(expression[:operatorPos])
    b = int(expression[operatorPos+1:])

    print("Result: {}".format(lunar.add(a,b))) if expression.find("+") > -1 else print("Result: {}".format(lunar.mul(a,b))) if expression.find("*") > -1 else print("Something went wrong.")
