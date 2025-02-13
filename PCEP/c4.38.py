a = input("Provide first number: ")
b = input("Provide second number: ")
c = input("Provide third number: ")

if a > b:
    if a > c:
        x = a
    else:
        x = c
elif c > b:
    x = c
else:
    x = b

print("Biggest number is", x)
