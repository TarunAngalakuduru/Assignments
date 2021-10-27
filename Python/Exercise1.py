#1st Question:

num1 = 34
num2 = 56
num3 = 90
if (num1 > num2) & (num1 > num3):
    print(num1, "is the greatest number")
elif (num2 > num1) & (num2 > num3):
    print(num2, "is the greatest number")
else:
    print(num3, "is the greatest number")



#3rd Question:

name = input("enter your name:")
age = int(input("enter your age:"))
hundred = int((100 - age) + 2021)
print("Hello %s. You are %s years old. You will turn 100 years old in %s." % (name, age, hundred))
