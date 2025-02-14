d1 = {}
print(d1)

d1 = {1:"Python",2:"Java",3:"C++",1:"yton"}
print(d1)

d1 = dict({1:"Python",2:"Java",3:"C+",4:"Groovy",99:"Kobol",5:"Java Script"})
print(d1)

print(d1[99])
print(d1.get(7))

# Updating dictionary

d1[3] = "C++"
print(d1)

d1[6] = "Bash"
print(d1)

# Clearing dictionary

d1.pop(2)
print(d1)

d1.popitem()
print(d1)

del d1[5]
print(d1)

d1.clear()
print(d1)