""" print("What is your name?")
name = input()
print("How old are you?")
y_old = int(input())
print("What is your weight?")
weight = float(input())
print("Are you authorized? (Y/N)")
auth = input() == "Y"
 """

name = input("What is your name?\n")
y_old = int(input("How old are you?\n"))
weight = float(input("What is your weight?\n"))
auth = input("Are you authorized? (Y/N)\n") == "Y"


print("Hello", name)
print(y_old, "years old")
print("Weight", weight)
print("Authorized", auth)
