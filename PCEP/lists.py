# Creating and printing lists

l1 = [3,5,7,2,8,3,5,3,4,7]
print(l1)

s = "I love Python programming"
l2 = s.split()
print(l2)

l3 = list(range(2,40,3))
print(l3)

l4 = [1,l3,l2,8]
print(l4)
print(l4[2][0])

print(l3[2:10:2])
print(l3[10:2:-2])
print(l3[2:2])

# Editing lists
print("Editing")
l1[2] = 100
print(l1)
l1[1:4] = [33,34,35]
print(l1)

print("Append")
l1.append(290)
print(l1)

l4.append(l1)
print(l4)

print("Extend")
l1.extend([3,98,2])
print(l1)

print("Insert")
l1.insert(2,9999)
print(l1)

# Deleting elements

print("Deleting")
del l1[4:7]
print(l1)

print("Remove")
l1.remove(3) # Removes first found value
print(l1)

print("Pop")
l1.pop(2)
print(l1)
l1.pop() # Removes last object
print(l1)

print(len(l1))
print(l1.count(3)) # Count occurances of 3
l1.sort()
print("Finding in list",l1)
print(l1.index(9999))
l1.reverse()
print(l1)

print("Loops")
i = 0
while i < len(l1):
    print(l1[i], end="-")
    i += 1

print("\nFor")
for x in l1:
    print(x, end="_")

print("\nFor #2")
i = 0
n = len(l1)
for i in range(n):
    print(l1[i], end=":")

print("\nClearing list")
l1.clear()
print(l1)