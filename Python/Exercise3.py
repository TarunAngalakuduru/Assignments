# 2nd Question
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))

def biggestnum(num1,num2,num3):
    if (num1 > num2) & (num1 > num3):
        print(num1, "is the greatest number")
    elif (num2 > num1) & (num2 > num3):
        print(num2, "is the greatest number")
    else:
        print(num3, "is the greatest number")

biggestnum(num1,num2,num3)

#3rd Question using functions

name = input("enter your name:")
age = int(input("enter your age:"))
def year_of_hundered(age):
    hundred = int((100 - age) + 2021)
    return hundred
h = year_of_hundered(age)
print("Hello %s. You are %s years old. You will turn 100 years old in %s from the year 2021." % (name, age, h))

