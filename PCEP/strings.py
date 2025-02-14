a = "Python"
b = "Monty"
print(len(a))
print(a[3])

i = 0
length = len(a)
while i < length:
    print(a[i], end=",")
    i += 1

i = len(a) - 1
while i >= 0:
    print(a[i], end="")
    i -= 1

print(a[1:4:1])
print(a[1:5:3])

s1 = b + " "+ a
print(s1)
s2 = a * 2
print(s2)

print("I love \"Python\"")

str = """I
love
Python programming!
"""

print(str)