import LunarArithmetic as lunar

number = int(input("How many squares do you want to see?"))

for x in range(0, number):
    print(str(x) + " * " + str(x) + " = {}".format(lunar.mul(x,x)))
