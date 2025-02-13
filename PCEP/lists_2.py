l1 = [3,5,7,2,999]
l2 = [3,5,3,7]
l3 = [5,3,3,7]
l4 = l1 + l2
print(l4)

l5 = l1 * 2
print(l5)

print(l2 == l3)
print(l2.sort() == l3.sort(),"\n")

print(3 in l4)
print(55 not in l4)