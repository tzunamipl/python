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

for x in range(10):
    for y in range(10):
        print(x, y)
        if y == 4: break

print("break?")

for x in range(4):
    if x == 3:
        break
    print(x)
else:
    print("Done")

L = [1,2,3,4,5]
L*2
print(L)