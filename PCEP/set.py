s1 = {3,5,1,2,9,4,2,7,8,"dupa","Python",2.4}
print(s1)

l1 = [3,5,7,2,8,3,5,3,4,7]
s2 = set(l1)
print(s2)

# Set can not have sets, lists, list can have sets

l2 = [3,4,6,{3,6,2,3,7,6,3},2,9]
print(l2)

# Modyfing items in set

s1.add(666)
print(s1)

s1.update([5,9,12,14,15,56])
print(s1)
s1.update(range(20))
print(s1)

s3 = s1.copy()
s4 = s1
print(s3)
print(s4)

# Removing items

print(s1.pop())
print(s1)

s1.remove(6) # Error if element does not exist
print(s1)

s1.discard(11) # No error if element does not exist
print(s1)

s1.clear()
print(s1)

# Mathematical operators on sets

s1 = {1,3,6,5,43}
s2 = {6,3,5,12,14}

print("")
print("s1:", s1)
print("s2:", s2)
print(s1.union(s2),s1.intersection(s2),"-",s1.difference(s2),s2.difference(s1),"-",s1.symmetric_difference(s2))
print(s1 | s2, s1 - s2, s2 - s1)

# Membership test

print("")
print(3 in s1, 7 in s1.union(s2), 7 not in s1)