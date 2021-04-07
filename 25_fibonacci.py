import termcolor2

n = int(input("Enter Number:"))

x = 0
y = 1
list = list()

if n < 0:
    print(termcolor2.colored("Number is Wrong", color="red"))
else:
    for i in range(n):
        list.append(x)
        result = x + y
        y = x
        x = result
    print(termcolor2.colored(tuple(list), color="green"))
