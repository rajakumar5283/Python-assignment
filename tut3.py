# print("10 + 20 is", 10 + 20)
# print("10 + 20 is", 10 - 20)
# print("10 + 20 is", 10 * 20)
# print("10 + 20 is", 10 / 20)
# print("10 + 20 is", 10 % 20)
# print("10 + 20 is", 10 ** 20)
# print("10 + 20 is", 10 // 20)

# list1 = [100,200,300,400]
# for i in list1:
#     print("list is",i)

# for i in list1:
#     if 100 in list1:
#         print(i)

# guess = 88
# coin = 1
# print("limit only 10 time")
# user = int(input("Guess a number"))
# while coin <= 10:
#     if user > 88:
#         print("Please enter lower number")
#     elif user < 88:
#         print("Please enter bigger number")
#     else:
#         print("You are win")
#     print(,"left only")



# a = True
# b = False
# print(a is not b)


# a = 10
# b = 20

# print(a is not b)


# list1 = ["Kalamadi","Rajakumar","Anil"]
#
# print("Kalamadi" not in list1)

# a = int(input("Enter a number:\n"))
# b = int(input("Enter b number\n"))
# print("num is bigg") if a < b else print("num is small")


# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# c = sum([a,b])
# print(c)


# def myFunc(a,b):
#     # a = int(input("Enter a first number:\n"))
#     # b = int(input("Enter a second number:\n"))
#     c = sum((a,b))
#     print(c)
# myFunc(10,20)


# def myFunc():
#     """This is a function to calculate 2 number find out the avarage"""
#     a = int(input("Enter a number:\n"))
#     b = int(input("Enter b number:\n"))
#     avg = (a+b)//2
#     return avg
# # avarage = myFunc()
# # print("The avarage is ", avarage)
# print(myFunc.__doc__)



# num1 = input("Enter first number:\n")
# num2 = input("Enter second number:\n")
# try:
#     print("The sum is:",int(num1)+int(num2))
# except Exception as a:
#     print(a)
# print("Kalamadi Rajakumar Prakash")



def calCulater():
    num1 = int(input("Enter First number:\n"))
    print("Which type you want:\n")
    print("+", "-", "/", "*", "**", "//", "%")
    op = input()
    num2 = int(input("Enter Second number:\n"))
    if op == "+":
        result = num1 + num2
        print(result)
    elif op == "-":
        result = num1 - num2
        print(result)
    elif op == "/":
        result = num1 / num2
        print(result)
    elif op == "*":
        result = num1 * num2
        print(result)
    elif op == "**":
        result = num1 ** num2
        print(result)
    elif op == "//":
        result = num1 // num2
        print(result)
    else:
        print("Please enter valid number!!!!")


    print("You want repeat it:\n")
    print("Yes/No")
    value = input()
    if value == "Yes":
        calCulater()

calCulater()





