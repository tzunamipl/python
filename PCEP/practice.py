# Test 2
# 11
print("2.11")

def func(var):
    var = 5

var = 3
func(var)
print(var)

#13
s = "ThanksS"
print(s[3])

l1 = [4,5,7]
l2 = [4,5,6]
print(l1 < l2)

list1 = [10, 5, (8,6)]
list2 = [10, 5, (8,2)]
print(list1 > list2)

for n in range(0,5):
    print(n)
    n =n*n
print(n)

l1 = list1
l2 = l1
l2.append(6)
print(l1, l2)