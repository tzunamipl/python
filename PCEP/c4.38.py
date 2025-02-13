a = input("Provide first number: ")
b = input("Provide second number: ")
c = input("Provide third number: ")

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif c > b:
    print(c)
else:
    print(b)
