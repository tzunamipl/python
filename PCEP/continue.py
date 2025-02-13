a = 5
while a:
    print(a, end=",")
    a -= 1
    if a == 3:
        continue
    print("Comp")