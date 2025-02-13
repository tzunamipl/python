a = 5

while a:
    print(a, end=",")
    a -= 1
    if a == 2:
        break
print("\nOutside while loop")

a = [1,2,3,4,5,6,7]
for x in a:
    print(x, end=",")
    if x == 3:
        break