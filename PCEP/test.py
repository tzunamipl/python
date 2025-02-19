import random

# Task 1

x = [1,2,3]

y = x
y[0] = 10
print(x)

a = 10
b = a
b = 20
print(a)

# Task 2
print("Task 2")

x = 5
y = 2

result = x // y + x % y
print(result)
print((x // y), "+", (x %y ))

# Task 3

l1 = [i * i for i in range(1,6)]
print(l1)

# Task 4
a = [1, 2, 3, 4, 5, 6, 7]
print(a.pop(3))
del a[3]
print(a)

# Task 5
d1 = {"First":"Python","Second":"Java","Third":"C++",1:"yton"}
print(d1)
print(d1.pop("Second"))
del d1["Third"]
print(d1)

# Task 5
print("Task 5")
print(3 & 7)
print(7 & 3)
print(3 or 7)
print(7 or 3)

# Task 7
print("Task 7")
print(ord("5"),chr(876))

# Task 8
name = "Alice"
age = 25
height = 1.650

print(f"{name} is {age} years old and is {height:.2f} meters tall.")

# Test 9
l1 = ["g","r","f","t"]
l2 = ["ws","tg","cb","th"]

result_dict = dict(zip(l1, l2))
print(result_dict)
result_dict.pop("f")
del result_dict["t"]
print(result_dict)

# Test 10
print("Test 10")
l1[3] = [4,5,6]
l2 = l1
l3 = list(l1)
l4 = l1.copy()
l5 = l1[:]
l1[0] = 666
l1[3][2] = 999
def modify_list(l0, x):
    l0[2] = random.randint(x,x+100)
    print(l1, l0)

modify_list(l2, 0)
modify_list(l3, 100)
modify_list(l4, 200)
modify_list(l5, 300)

# Test 11
print("Test 11")
l1 = ["Dupa", "l1", "gosdsdkjsdhgfkj", "Dom"]
print(sorted(l1, key=len, reverse=False))

# Test 12
print("Test 12")
x = 100
a = True
b = False
if x == 1 & (a & b):
    print(x)
    print(x * 2)

x = 100
a = True
b = False
a = x == 100
print(x)
print(a)

# Test 13
print("Test 13")
a = "I Love Python Programming"
print(a.count("o", 2))

# Test 14
print("Test 14")
p = 'n'
def multiply():
    global p
    p *= 3
    print(3 * p)
multiply()
print(p)

# Test 15
print("Test 15")
data = " "
while data:
    print("Data is not Empty")
    data = ""
else:
    print("Data is Empty")

# Test 16
print("Test 16")

inp = 4

if (inp < 3): print("Sandy")
else: print("Monika")

print("Sandy") if (inp < 3) else print("Monika")