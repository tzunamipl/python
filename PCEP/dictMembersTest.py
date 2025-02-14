d1 = dict({1:"Python",2:"Java",3:"C+",4:"Groovy",99:"Kobol",5:"Java Script",6:"Ruby",7:"Bash"})

print(1 in d1, 99 in d1, 22 in d1)
print(99 not in d1, 23 not in d1)

for i in d1:
    print(i, end=",")
for i,j in d1.items():
    print(i, j, end=",")

print("\n",len(d1))
print(d1.get(3, "Dupa"),d1.get(10, "Dupa"),d1.get(66))

print("\n",d1.keys())
for i in d1.keys():
    print(i, end=",")

print("\n\n",d1.values())
print(list(d1.values()))
for i in d1.values():
    print(i, end=",")

print("\n\n",d1.items())