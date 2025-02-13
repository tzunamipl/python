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
print("I like {} and {}".format("apples", "oranges"))
print("I like {1} and {0}".format("apples", "oranges"))
print("I like {second} and {second}".format(first="apples", second="oranges"))

x = 4377745.239536
print("The value of x is %4.2f" % x)