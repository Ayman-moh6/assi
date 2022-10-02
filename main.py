# firs
name = input("inter your name")
age = input("inter your age")
address = input("inter your address")
if name.isalpha() == True and age.isnumeric() == True and address.isalpha() == True:
    print("Hello Mr/Ms " + name + " age " + str(age) + " located in " + address + ". thanks for being one of our "
                                                                                  "community, Enjoy")
else:
    print("you got an empty value or not valid value")

# second
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ^ y


def pers(x, y):
    return x % y


number1 = input("enter the first number")
if number1.isnumeric():
    print("Select operation")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. ^")
    print("6. %")
    opera = input("Enter choices(1,2,3,4,5,6) or the operation: ")
    if opera in ('1', '2', '3', '4', '5', '6', '+', '-', '*', '/', '^', '%'):
        number2 = input("enter the second number")
        if number2.isnumeric():
            number1 = float(number1)
            number2 = float(number2)
            if opera == '1' or opera == '+':
                res = add(number1, number2)
                print(number1, "+", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    if operation in ('1', '2', '3', '4', '5'):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")


                else:
                    print('wrong input')
            elif opera == '2' or opera ==  '-':
                res = subtract(number1, number2)
                print(number1, "-", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    if operation in ('1', '2', '3', '4', '5'):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")
                else:
                    print('wrong input')

            elif opera == '3' or opera == '*':
                res = multiply(number1, number2)
                print(number1, "*", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    if operation in ('1', '2', '3', '4', '5'):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")
                else:
                    print('wrong input')

            elif opera == '4' or opera == '/':
                res = divide(number1, number2)
                print(number1, "/", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    operation = float(operation)
                    if operation in (1, 2, 3, 4, 5):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")
                else:
                    print('wrong input')

            elif opera == '5' or opera == '^':
                res = power(number1, number2)
                print(number1, "^", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    if operation in ('1', '2', '3', '4', '5'):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")
                else:
                    print('wrong input')

            elif opera == '6' or opera == '%':
                res = pers(number1, number2)
                print(number1, "%", number2, "=", res)
                print("Select operation")
                print("1. round")
                print("2. ceil")
                print("3. floor")
                print("4. turn it into int")
                print("5. exit")
                operation = input("inter operation number")
                if operation.isnumeric():
                    if operation in ('1', '2', '3', '4', '5'):
                        if operation == 1:
                            print(round(res))
                        elif operation == 2:
                            print(math.ceil(res))
                        elif operation == 3:
                            print(math.floor(res))
                        elif operation == 4:
                            print(int(res))
                        elif operation == 5:
                            print("thx :)")
                else:
                    print('wrong input')

        else:
            print("Invalid value")
    else:
        print("Invalid value")
else:
    print("Invalid value")

# third
num1 = input("Inter the 1st number")
num2 = input("Inter the 2ed number")
num3 = input("Inter the 3rd number")
num4 = input("Inter the 4th number")
num5 = input("Inter the 5th number")
if num1.isnumeric() == True and num2.isnumeric() == True and num3.isnumeric() == True and num4.isnumeric() == True and num5.isnumeric() == True:
    array1 = {num1, num2, num3, num4, num5}
    print("Max value is:" + max(array1) + "   , and min value is:" + min(array1))
else:
    print("u got empty or non numerical value")
