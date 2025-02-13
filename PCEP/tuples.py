t1 = (3,5,7,2,999)
t2 = (3,5,3,7)
t3 = 5,3,3,7
print(t3)

print(t1)
l1 = []
l1.extend(t1)
print(l1)

# Convert list to tuple
t4 = tuple(l1)
print(t4)

t5 = 4,6,[4,8,6],4
print(t5)
print(t5[2][2])
print(t1[1:4:1])
print(t1[2::2])
print(t1[4:1:-1])

t5[2][1] = 99
print(t5)

# Packing
a = 10
b = 20
c = 30
d = 40
t01 = a, b, c, d
print(t01)

# Unpacking
w, x, y, z = t01
x1, x2, x3, x4, x5 = l1
print(w, x, y, z)
print(x1,x2,x3)



