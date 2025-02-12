a = 10
b = 20
c = 30

d, e, f = 23, 14, 2

print(a, end="")
print(a,b,c, end="dupa")
print(a,b,c,d,e,f)
print(a,b,c,d,e,f, sep=", ", end="")
print("")
a = 3.14
b = 3.14
print(id(a))
print(id(b))
b = 3.15
print(id(b))
